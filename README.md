<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Waving%20Hand.png" width="35" /> AirTouch AINext-Generation Computer Vision Peripheral Control<div align="center"></div>💎 The ExperienceAirTouch AI is not just a mouse replacement; it's a spatial interface. By utilizing the BlazePalm ML model, we track 21 high-fidelity landmarks in 3D space, translating micro-gestures into macro-system actions.🌌 Visual HUD LogicActive Tracking: Real-time skeleton overlay for user feedback.Gesture Verification: Dynamic color-coded lines (Green for Click, Yellow for Drag) verify actions before execution.Edge-Flow: Coordinate interpolation allows the user to reach a 4K monitor's corners with only 5 inches of physical hand movement.🕹️ Command Registry<details open><summary><b>展开 View Gesture Documentation</b></summary>TriggerActionKeypointslogic🖱️ CursorNavigation9Palm-center anchor for zero-jitter movement.⚡ L-ClickPrimary4 + 8Thumb and Index Tip convergence.📑 R-ClickContext3 + 5Thumb IP to Index MCP contact.🎨 DragDraw/Move8 + 12Index and Middle tips joined.📸 SnapScreenshot20 + 16Pinky and Ring finger pinch.✊ FistDoubleFistGlobal tip proximity to wrist.</details>🚀 Rapid Deployment⚡ Prerequisites[!IMPORTANT]This project requires Python 64-bit. The 32-bit architecture will fail to initialize the MediaPipe graph.Bash# 1. Environment Isolation
python -m venv .venv
source .venv/bin/activate  # Or .\.venv\Scripts\activate on Windows

# 2. Dependency Injection
pip install opencv-python mediapipe pyautogui numpy

# 3. Initialize Engine
python hio.py
🛠️ Architecture Deep-DiveThe Smoothing Algorithm (Lerp)To achieve "Paint-Ready" stability, we use a Linear Interpolation formula:$$P_{current} = P_{prev} + \frac{P_{target} - P_{prev}}{Smoothing}$$This ensures that even if your hand has micro-tremors, the cursor path remains mathematically fluid.<div align="center"><sub>Built with ❤️ by Shaju & Gemini AI</sub></div>
