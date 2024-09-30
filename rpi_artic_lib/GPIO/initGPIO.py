import RPi.GPIO as GPIO


def initGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
