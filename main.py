import cv2
import serial
import time
import pyttsx3

# Arduino connection
arduino = serial.Serial('COM5', 9600)
time.sleep(2)

# Voice engine part
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


# Variables
eye_closed_counter = 0
last_blink_timestamp = 0

# Haar cascades part
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    eyes_open_flag = False

    for (x, y, w, h) in faces:

        if w > 100 and h > 100:

            roi_gray = gray[y:y + h, x:x + w]

            eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 6)

            if len(eyes) > 0:
                eyes_open_flag = True

            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Detect if eyes are closed for multiple frames (to confirm real blink)
    if len(faces) > 0:

        if not eyes_open_flag:
            eye_closed_counter += 1

        else:
            if eye_closed_counter > 3:

                current_time = time.time()

                # Prevent multiple triggers (debounce)
                if current_time - last_blink_timestamp > 1:
                    print("Blink detected → toggling LED")
                    speak("Toggle")

                    arduino.write(b'1')

                    last_blink_timestamp = current_time

            eye_closed_counter = 0

    cv2.putText(frame, f"Closed: {eye_closed_counter}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Advanced Control", frame)

    time.sleep(0.08)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
