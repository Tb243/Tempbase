from hardware import buzzer

BUZZER_PIN = 26

b = buzzer.Buzzer(BUZZER_PIN)
b.buzz_for(1.0)