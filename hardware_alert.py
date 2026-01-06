import serial
import time

# Replace 'COM4' with your Arduino port
arduino = serial.Serial(port="COM3", baudrate=9600, timeout=2)
time.sleep(2)

def trigger_alert():
    print("🚨 Suspicious activity detected! Sending alert to Arduino...")
    arduino.write(b'ALERT\n')
    time.sleep(1)

