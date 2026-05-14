# Vision-Based Blink Control System

##  Overview
This project uses a trained AI model and computer vision to detect eye blinks and control an Arduino-based system. It is designed as an assistive technology for paralysis patients.

---

##  System Architecture

```mermaid
 flowchart TD
    A[Webcam Input] --> B[OpenCV Face Detection\nHaar Cascade Classifier]
    B --> C[Eye Region Extraction]
    C --> D[Blink Detection\nEye Aspect Ratio - EAR]
    D --> E{Blink Detected?}
    E -- Yes --> F[Python Serial Communication\npyserial]
    E -- No --> C
    F --> G[Arduino Uno]
    G --> H[Device Control Output\nLED / Relay / Assistive Device]
`---

Latency: ~30-50ms (webcam frame rate dependent)
Detection Method: Eye Aspect Ratio (EAR) threshold
Communication: USB Serial at 9600 baud

---

##  Working

- OpenCV captures frames at ~30 FPS and applies Haar Cascade for face detection
- Eye Aspect Ratio (EAR) calculated per frame; blink triggered when EAR <0.25 
- Arduino receives HIGH/LOW signal via pyserial at 9600 baud to toggle device


---

##  Hardware Used
- Arduino Uno
- LED
- Resistors
- USB Serial Communication
- Jumper wiresw
---

##  Software Used
- Python (OpenCV / AI model)
- Arduino IDE

---

##  Demo Video
[Click here to watch demo](https://youtu.be/gwS6qdLiZgE?si=icCfXYAVZBwI7J9p)

---

##  Features
- Real-time blink detection
- Hands-free control
- Assistive technology application

---

##  Files
- `advance_paralysis_control.py` → Python code
- `blink_control.ino` → Arduino code