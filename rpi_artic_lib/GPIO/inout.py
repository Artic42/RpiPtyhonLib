import RPi.GPIO as GPIO
from rpi_artic_lib.GPIO.input import Input
from rpi_artic_lib.GPIO.output import Output


INPUT = 1
OUTPUT = 2


class InOut(Input, Output):
    def __init__(self, pin: int, direction:  int, initial_state: bool = False,
                 pull_up_down: int = GPIO.PUD_UP, ):
        self.pin = pin
        self.direction = direction
        self.pull_up_down = pull_up_down
        self.state = initial_state
        if self.direction == INPUT:
            self.setAsInput(self.pin, pull_up_down=self.pull_up_down)
        else:
            self.setAsOutput(self.pin, initial_state=initial_state)

    def setAsInput(self, pin: int, pull_up_down: int = GPIO.PUD_UP):
        GPIO.setup(pin, GPIO.IN, pull_up_down=pull_up_down)

    def setAsOutput(self, pin: int, initial_state: bool = False):
        GPIO.setup(pin, GPIO.OUT)
        self.write(initial_state)
