Street Sentinel – AI-Powered Women's Safety and Smart Surveillance System

Technologies: Python | CNN-LSTM | Deep Learning | OpenCV | Arduino UNO R3 | IoT

Project Overview

Street Sentinel is an AI-powered women's night-safety and smart surveillance system designed to identify potentially suspicious activities through CCTV video monitoring.

The system uses a CNN-LSTM-based deep learning approach to analyze surveillance footage and detect abnormal activities. When suspicious activity is detected, the system communicates with an Arduino UNO R3 microcontroller to activate automated safety mechanisms, including streetlight brightness enhancement and an emergency buzzer.

By combining Artificial Intelligence with Internet of Things (IoT), Street Sentinel aims to transform traditional surveillance into an intelligent and automated safety solution.

Key Features

- AI-Based Activity Detection: Uses a CNN-LSTM deep learning model to identify suspicious activities from video sequences.
- Video Processing: Uses OpenCV for video frame extraction and preprocessing.
- Smart Streetlight Automation: Automatically increases streetlight brightness using Arduino PWM control.
- Emergency Alert System: Activates a buzzer when suspicious activity is detected.
- IoT Integration: Establishes serial communication between the Python-based AI system and Arduino UNO R3.
- Location-Based Alerts: Supports communicating incident information and location to designated authorities.

AI and Deep Learning Architecture

The system follows a video-based activity detection pipeline:

1. CCTV video input is collected.
2. OpenCV extracts and preprocesses video frames.
3. Processed frame sequences are passed to the CNN-LSTM model.
4. The model analyzes spatial and temporal patterns.
5. Suspicious activity detection triggers an alert.
6. Python communicates with Arduino through serial communication.
7. Arduino activates the streetlight and emergency buzzer.

IoT Hardware Integration

The project integrates AI-based detection with physical hardware using Arduino UNO R3.

Hardware Component| Function
Arduino UNO R3| Main microcontroller
PWM Pin 9| Streetlight brightness control
Digital Pin 8| Emergency buzzer activation
Serial Communication| Python-to-Arduino communication

Hardware Workflow:

AI Detection → Python Alert → Serial Communication → Arduino UNO → Streetlight Enhancement and Buzzer Activation

Technologies Used

- Programming Language: Python
- Artificial Intelligence: CNN, LSTM, Deep Learning
- Computer Vision: OpenCV
- IoT and Hardware: Arduino UNO R3, Embedded Systems, Serial Communication
- Libraries: NumPy, OpenCV, PySerial, TensorFlow/Keras

Project Structure

Street-Sentinel/
│
├── MyArduinoProject/
│   └── arduino_alert/
│
├── VioPeru-main/
│
├── hardware_alert.py
├── inference.py
├── train.py
├── suspicious_activity_cnn_lstm.h5
│
└── README.md

Installation and Setup

1. Clone the Repository

git clone https://github.com/Sreeyaa-Raaman/Street-Sentinel.git

2. Navigate to the Project Directory

cd Street-Sentinel

3. Install Dependencies

pip install opencv-python numpy tensorflow pyserial

4. Connect Arduino

- Connect Arduino UNO R3 to your computer.
- Upload the Arduino alert-control program from the Arduino project folder.
- Connect the streetlight control circuit to PWM pin 9.
- Connect the buzzer circuit to digital pin 8.
- Configure the correct serial communication port in the Python hardware integration script.

5. Run the Detection System

python inference.py

Ensure the trained model and required video inputs are available before execution.
## Project Demonstration

Watch the Street Sentinel project demonstration:

[Watch Street Sentinel Demo](https://drive.google.com/file/d/1QfD-Trt3_nRweyyL6VJo634zb22_OErd/view)
Challenges and Technical Learning

- Integrating deep learning-based video analysis with physical IoT hardware.
- Processing sequential video frames for activity classification.
- Establishing serial communication between Python and Arduino.
- Coordinating automated hardware responses based on AI detection.
- Connecting software intelligence with real-world safety mechanisms.

Future Enhancements

- Integration with cloud-based CCTV monitoring.
- Improved detection using larger and more diverse video datasets.
- GPS-enabled incident location tracking.
- Mobile application for emergency notifications.
- Multi-camera monitoring and centralized alert management.

Developed By

J. Sreeyaa Raaman

B.Tech – Artificial Intelligence and Data Science

GitHub: https://github.com/Sreeyaa-Raaman

LinkedIn: https://linkedin.com/in/sreeyaa-raaman-226b4926b

---

Street Sentinel – Combining Artificial Intelligence and IoT to build smarter and safer environments.
