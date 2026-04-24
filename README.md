# Vision-Based Blink Control System

##  Overview
This project uses a trained AI model and computer vision to detect eye blinks and control an Arduino-based system. It is designed as an assistive technology for paralysis patients.

---

##  System Architecture
![System Diagram](images/diagram.png)

---

##  Working
- Python detects eye blink using camera
- Sends signal via serial communication
- Arduino receives signal and controls LED/device

---

##  Hardware Used
- Arduino Uno
- LED
- Resistors
- USB Serial Communication
- Jumper wires
---

##  Software Used
- Python (OpenCV / AI model)
- Arduino IDE

---

##  Demo Video
[Click here to watch demo](YOUR_YOUTUBE_LINK)

---

##  Features
- Real-time blink detection
- Hands-free control
- Assistive technology application

---

##  Files
- `advance_paralysis_control.py` → Python code
- `blink_control.ino` → Arduino code