import cv2
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from hardware_alert import trigger_alert


# ----------- Email Setup -----------
EMAIL_ADDRESS = "sreeyaa1905@gmail.com"      # Your Gmail
EMAIL_PASSWORD = "mjtd wfgg bhwv rmaf"         # Gmail App Password
TO_EMAIL = "SriSur2006@gmail.com"      # Recipient email

def send_email_alert(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print("✅ Email alert sent successfully!")
    except Exception as e:
        print("❌ Failed to send email:", e)

# ----------- Video Input -----------
video_path = r"C:\Users\sreeyaa raaman\AppData\Local\Programs\Python\Python310\streetpro\VioPeru-main\val\Fight\f15tala.avi"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video. Check the path!")
    exit()

# ----------- Motion Detection Setup -----------
fgbg = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50)
suspicious_detected = False

while True:
    ret, frame = cap.read()
    if not ret:
        break  # End of video

    frame = cv2.resize(frame, (640, 480))
    fgmask = fgbg.apply(frame)

    _, thresh = cv2.threshold(fgmask, 250, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        if cv2.contourArea(cnt) > 500:  # Large motion
            suspicious_detected = True
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    status_text = "Suspicious" if suspicious_detected else "Normal"
    cv2.putText(frame, status_text, (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                (0, 255, 0) if not suspicious_detected else (0, 0, 255), 2)

    cv2.imshow("Suspicious Activity Detection", frame)
    key = cv2.waitKey(30)
    if key == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()

# ----------- Send Email Alert if Suspicious -----------
if suspicious_detected:
    # Example fixed location
    latitude = 17.3850
    longitude = 78.4867
    maps_link = f"https://maps.google.com/?q={latitude},{longitude}"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    subject = "ALERT: Suspicious Activity Detected!"
    body = f"Suspicious activity detected!\nLocation: {maps_link}\nTime: {timestamp}"

    send_email_alert(subject, body)
        # ✅ Trigger Arduino Alert
    trigger_alert()

else:
    print("No suspicious activity detected in the video.")