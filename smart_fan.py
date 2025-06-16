import RPi.GPIO as GPIO
import Adafruit_DHT
import time


DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 14

TRIG_PIN = 23
ECHO_PIN = 24

SERVO_PIN = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(SERVO_PIN, GPIO.OUT)

servo = GPIO.PWM(SERVO_PIN, 50)
servo.start(0)

def read_distance():
 
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()

    duration = pulse_end - pulse_start
    distance = duration * 17150
    return round(distance, 2)

def servo_spin_loop():

    servo.ChangeDutyCycle(15)
    time.sleep(0.3)
    servo.ChangeDutyCycle(0)

try:
    while True:
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
        distance = read_distance()

        if temperature is not None:
            print(f"Sicaklik: {temperature}°C, Mesafe: {distance} cm")

            if temperature > 27:
                print("Sicaklik Asildi!")
            
                if distance > 10:
                    print("Mesafe Guvenli")
                    servo_spin_loop()
                else:
                    print("Dikkat, Lutfen uzak durunuz!")
                    servo.ChangeDutyCycle(0)
            else:
                print("Sicaklik dusuk, klima calismiyor.")

            time.sleep(1)

except KeyboardInterrupt:
    print("Program durduruldu.")
    servo.stop()
    GPIO.cleanup()