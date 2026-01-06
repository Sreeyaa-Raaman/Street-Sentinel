// Pins
int ledPin = 9;      // LED connected to pin 9 (PWM)
int buzzerPin = 8;   // Buzzer connected to pin 8

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  Serial.begin(9600);

  // Start LED in dim mode
  analogWrite(ledPin, 80);  // dim glow
}

void loop() {
  if (Serial.available()) {
    String data = Serial.readStringUntil('\n');

    if (data == "ALERT") {
      // Brighten LED
      analogWrite(ledPin, 255);      // full brightness
      digitalWrite(buzzerPin, HIGH); // buzzer on
      delay(3000);                    // alert duration
      // Reset to dim LED and buzzer off
      analogWrite(ledPin, 80);       
      digitalWrite(buzzerPin, LOW);
    }
  }
}
