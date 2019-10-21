# Import Dependancies

import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BOARD)
GPIO.setwarnings(False)

# Enable switches and pull up resistors

GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # Motor 1 Forward
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # Motor 1 Backwards


# Stepper 1 Pins

coil_A_1_pin = 7    # IN1
coil_A_2_pin = 11   # IN2
coil_B_1_pin = 13   # IN3
coil_B_2_pin = 15   # IN4

GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

# Half Step Sequence

StepCount = 8
Seq = range(0, StepCount)
Seq[0] = [1,0,0,0]
Seq[1] = [1,1,0,0]
Seq[2] = [0,1,0,0]
Seq[3] = [0,1,1,0]
Seq[4] = [0,0,1,0]
Seq[5] = [0,0,1,1]
Seq[6] = [0,0,0,1]
Seq[7] = [1,0,0,1]

def setStep(w1, w2, w3, w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)

def forward(delay, steps):
    for i in range(steps):
        for j in range(StepCount):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)

def backwards(delay, steps):

    for i in range(steps):
        for j in reversed(range(StepCount)):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)

if __name__ == '__main__':

    # Set speed and reactiveness of motors

    delay = 1           # Speed of motor in ms (time between steps)
    steps = 8           # Steps per interation

    while True:

        motor_1_forward = GPIO.input(12)
        motor_1_backward = GPIO.input(16)

        if motor_1_forward == False:
            forward(int(delay)/1000.0, int(steps))
        if motor_1_backward == False:
            backwards(int(delay)/1000.0, int(steps))
        time.sleep(0.001)