<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=venom&color=0:0F2027,50:203A43,100:00E5FF&height=230&section=header&text=AirTouch%20AI&fontSize=50&fontColor=FFFFFF&animation=twinkling&fontAlignY=32&desc=Next-Generation%20Computer%20Vision%20Peripheral%20Control&descAlignY=56&descSize=18&descColor=00E5FF" />

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Waving%20Hand.png" width="35" />

<a href="#">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3000&pause=800&color=00E5FF&center=true&vCenter=true&width=650&lines=Tracking+21+Hand+Landmarks+in+3D...;Turning+Micro-Gestures+into+Macro-Actions...;No+Mouse.+No+Touch.+Just+Air.+%E2%9C%8B" alt="Typing SVG" />
</a>

<br/>

<img src="https://img.shields.io/badge/Python-64--bit-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/MediaPipe-BlazePalm-00E5FF?style=for-the-badge&logo=google&logoColor=white" />
<img src="https://img.shields.io/badge/OpenCV-Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" />
<img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" />

</div>

---

## 💎 The Experience

AirTouch AI is not just a mouse replacement — it's a **spatial interface**. By utilizing the **BlazePalm** ML model, we track 21 high-fidelity landmarks in 3D space, translating micro-gestures into macro-system actions.

---

## 🌌 Visual HUD Logic

- **Active Tracking** — Real-time skeleton overlay for user feedback.
- **Gesture Verification** — Dynamic color-coded lines (Green for Click, Yellow for Drag) verify actions before execution.
- **Edge-Flow** — Coordinate interpolation allows the user to reach a 4K monitor's corners with only 5 inches of physical hand movement.

---

## 🕹️ Command Registry

<details open>
<summary><b>👉 View Gesture Documentation</b></summary>

<br/>

| Trigger | Action | Keypoints | Logic |
|---|---|---|---|
| 🖱️ **Cursor** | Navigation | `9` | Palm-center anchor for zero-jitter movement |
| ⚡ **L-Click** | Primary | `4 + 8` | Thumb and Index Tip convergence |
| 📑 **R-Click** | Context | `3 + 5` | Thumb IP to Index MCP contact |
| 🎨 **Drag** | Draw / Move | `8 + 12` | Index and Middle tips joined |
| 📸 **Snap** | Screenshot | `20 + 16` | Pinky and Ring finger pinch |
| ✊ **Fist** | Double Fist | Global | Tip proximity to wrist |

</details>

---

## 🚀 Rapid Deployment

### ⚡ Prerequisites

> [!IMPORTANT]
> This project requires **Python 64-bit**. The 32-bit architecture will fail to initialize the MediaPipe graph.

```bash
# 1. Environment Isolation
python -m venv .venv
source .venv/bin/activate  # Or .\.venv\Scripts\activate on Windows

# 2. Dependency Injection
pip install opencv-python mediapipe pyautogui numpy

# 3. Initialize Engines
python hio.py
```

---

## 🛠️ Architecture Deep-Dive

### The Smoothing Algorithm (Lerp)

To achieve "Paint-Ready" stability, we use a Linear Interpolation formula:

$$P_{current} = P_{prev} + \frac{P_{target} - P_{prev}}{Smoothing}$$

This ensures that even if your hand has micro-tremors, the cursor path remains mathematically fluid.

---

<div align="center">

<sub>Built with ❤️ by <b>AHSAAN</b></sub>

<img width="100%" src="https://capsule-render.vercel.app/api?type=venom&color=0:00E5FF,50:203A43,100:0F2027&height=150&section=footer&animation=twinkling" />

</div>
