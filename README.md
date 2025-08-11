# Cursor-by-hands

This Python project enables you to control your mouse cursor using hand gestures detected via your webcam. Ideal for touchless interaction!
---
##  Overview
The script captures your webcam feed, uses MediaPipe to detect hand landmarks, and translates your finger positions into corresponding cursor movements and actions.
---

##  Features
- **🖱 Click Gesture**  
  Bring your **index finger and thumb together** to perform a mouse click.

- **❌ Exit Gesture**  
  Cross your **index and middle fingertips** (or use both hands to cross fingers) to gracefully close the application.

---

##  Technologies Used
- **OpenCV** – Webcam imaging and frame processing  
- **MediaPipe Hands** – Hand landmark recognition in real time  
- **PyAutoGUI** – Mouse movement and click simulation

---

##  How It Works
1. **Capture**: Webcam captures real-time video, mirrored for intuitive control.  
2. **Detect**: MediaPipe identifies hand landmarks, especially fingertips.  
3. **Track**:
   - **Index + Thumb**: Close together → **Mouse click**
   - **Crossed Index & Middle**: Fingers meet → **Exit program**
   - Else → **Move cursor** based on index fingertip position mapped to screen coordinates.
4. **Quit**: Application terminates on gesture or by pressing **`q`**.

---

##  Getting Started

```bash
# Clone the repo
git clone https://github.com/mohtashamali/Cursor-by-hands.git

# Enter directory
cd Cursor-by-hands

# Install dependencies
pip install opencv-python mediapipe pyautogui
