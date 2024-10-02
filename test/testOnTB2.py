from rpi_artic_lib.GPIO import input
from rpi_artic_lib.GPIO import output
from rpi_artic_lib.GPIO import inout
import rpi_artic_lib.screenLCD as screenLCD
from rpi_artic_lib.GPIO.initGPIO import initGPIO
import testPinout as pinout
import time


def main():
    initGPIO()

    greenLED = output.Output(pinout.GREENLED_PIN, initial_state=False)
    redLED = output.Output(pinout.REDLED_PIN, initial_state=False)
    yellowLED = inout.InOut(pinout.YELLOWLED_PIN, inout.OUTPUT, initial_state=False)

    button1 = input.Input(pinout.BUTTONENTER_PIN)
    button2 = input.Input(pinout.BUTTONUP_PIN)
    button3 = input.Input(pinout.BUTTONDOWN_PIN)
    button4 = inout.InOut(
        pinout.BUTTONBACK_PIN, inout.INPUT, pull_up_down=input.GPIO.PUD_UP
    )

    screenDataBus = [
        pinout.SCREEND0_PIN,
        pinout.SCREEND1_PIN,
        pinout.SCREEND2_PIN,
        pinout.SCREEND3_PIN,
        pinout.SCREEND4_PIN,
        pinout.SCREEND5_PIN,
        pinout.SCREEND6_PIN,
        pinout.SCREEND7_PIN,
    ]

    screenLCD1 = screenLCD.LCDScreen(
        pinout.SCREENRS_PIN, pinout.SCREENRW_PIN, pinout.SCREENE_PIN, screenDataBus
    )
    screenLCD1.screenInit()
    screenLCD1.sendChar("H")
    screenLCD1.sendChar("e")
    screenLCD1.sendChar("l")
    screenLCD1.sendChar("l")
    screenLCD1.sendChar("o")
    screenLCD1.sendChar(" ")
    screenLCD1.sendChar("W")
    screenLCD1.sendChar("o")
    screenLCD1.sendChar("r")
    screenLCD1.sendChar("l")
    screenLCD1.sendChar("d")
    screenLCD1.sendChar("!")

    while True:
        if not button1.read():
            greenLED.setHIGH()
            redLED.setLOW()
        elif not button2.read():
            greenLED.setLOW()
            redLED.setHIGH()
        elif not button3.readByte() == 0x01:
            greenLED.writeByte(0x01)
            redLED.write(True)
        elif not button4.readByte() == 0x01:
            greenLED.writeByte(0x00)
            redLED.write(False)
        time.sleep(0.5)
        yellowLED.toggle()


if __name__ == "__main__":
    main()
