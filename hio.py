import os
import cv2
import pyautogui
import math
import numpy as np
import time

# Direct imports to bypass audio hangs
from mediapipe.python.solutions import hands as mp_hands
from mediapipe.python.solutions import drawing_utils as mp_draw

# --- CONFIG ---
screen_width, screen_height = pyautogui.size()
pyautogui.FAILSAFE = False

# Sensitivity/Smoothing
SMOOTHING = 3 
plocX, plocY = 0, 0
clocX, clocY = 0, 0

# Click Debouncing
last_click_time = 0
click_delay = 0.4 

# Setup Tracking
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.8)
cap = cv2.VideoCapture(0)
dragging = False

def get_dist(p1, p2, w, h):
    """Calculates pixel distance to make thresholding easier to understand"""
    x1, y1 = int(p1.x * w), int(p1.y * h)
    x2, y2 = int(p2.x * w), int(p2.y * h)
    return math.hypot(x2 - x1, y2 - y1)

print("System Active. Mapping: 4+8=Left Click | 8+12=Drag")

while cap.isOpened():
    success, img = cap.read()
    if not success: break
    
    img = cv2.flip(img, 1)
    h, w, c = img.shape
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_lms in results.multi_hand_landmarks:
            lm = hand_lms.landmark
            curr_time = time.time()
            
            # --- 1. MOVEMENT (Point 9) ---
            fr = 140 
            tx = np.interp(lm[9].x * w, (fr, w - fr), (0, screen_width))
            ty = np.interp(lm[9].y * h, (fr, h - fr), (0, screen_height))
            clocX = plocX + (tx - plocX) / SMOOTHING
            clocY = plocY + (ty - plocY) / SMOOTHING
            pyautogui.moveTo(clocX, clocY, _pause=False)
            plocX, plocY = clocX, clocY

            # --- 2. GESTURE LOGIC ---

            # DISTANCE CALCS (Pixel based for better accuracy)
            dist_4_8 = get_dist(lm[4], lm[8], w, h)   # Left Click
            dist_8_12 = get_dist(lm[8], lm[12], w, h) # Drag
            dist_3_5 = get_dist(lm[3], lm[5], w, h)   # Right Click

            # LEFT CLICK (4 and 8 meet)
            if dist_4_8 < 35: # Tightened threshold
                if curr_time - last_click_time > click_delay:
                    pyautogui.click(button='left')
                    last_click_time = curr_time
                cv2.line(img, (int(lm[4].x*w), int(lm[4].y*h)), (int(lm[8].x*w), int(lm[8].y*h)), (0, 255, 0), 3)
                cv2.putText(img, "LEFT CLICK", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # DRAG (8 and 12 meet)
            # Threshold is set to 30 pixels. If it's still "always dragging," increase this to 20.
            if dist_8_12 < 30: 
                if not dragging:
                    pyautogui.mouseDown()
                    dragging = True
                cv2.line(img, (int(lm[8].x*w), int(lm[8].y*h)), (int(lm[12].x*w), int(lm[12].y*h)), (0, 255, 255), 3)
                cv2.putText(img, "DRAGGING", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
            else:
                if dragging:
                    pyautogui.mouseUp()
                    dragging = False

            # RIGHT CLICK (3 and 5 meet)
            if dist_3_5 < 35:
                if curr_time - last_click_time > click_delay:
                    pyautogui.click(button='right')
                    last_click_time = curr_time
                cv2.putText(img, "RIGHT CLICK", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # SCREENSHOT (20 and 16 meet)
            if get_dist(lm[20], lm[16], w, h) < 30:
                if curr_time - last_click_time > 1.0:
                    pyautogui.hotkey('win', 'prtscr')
                    last_click_time = curr_time

            mp_draw.draw_landmarks(img, hand_lms, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Hand Control Debugger", img)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()