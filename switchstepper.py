# Import Dependancies

import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BOARD)
GPIO.setwarnings(False)

# Enable switches and pull up resistors

GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # Motor 1 Forward
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # Motor 1 Backwards
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # Motor 2 Forwards
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # Motor 2 Backwards

# Stepper 1 Pins

M1_coil_A_1_pin = 7    # IN1
M1_coil_A_2_pin = 11   # IN2
M1_coil_B_1_pin = 13   # IN3
M1_coil_B_2_pin = 15   # IN4

GPIO.setup(M1_coil_A_1_pin, GPIO.OUT)
GPIO.setup(M1_coil_A_2_pin, GPIO.OUT)
GPIO.setup(M1_coil_B_1_pin, GPIO.OUT)
GPIO.setup(M1_coil_B_2_pin, GPIO.OUT)

# Stepper 2 Pins

M2_coil_A_1_pin = 31   # IN1
M2_coil_A_2_pin = 33   # IN2
M2_coil_B_1_pin = 35   # IN3
M2_coil_B_2_pin = 37   # IN4

GPIO.setup(M2_coil_A_1_pin, GPIO.OUT)
GPIO.setup(M2_coil_A_2_pin, GPIO.OUT)
GPIO.setup(M2_coil_B_1_pin, GPIO.OUT)
GPIO.setup(M2_coil_B_2_pin, GPIO.OUT)

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


# Functions

def setStep(motor, w1, w2, w3, w4):
    if motor == 1:
        GPIO.output(M1_coil_A_1_pin, w1)
        GPIO.output(M1_coil_A_2_pin, w2)
        GPIO.output(M1_coil_B_1_pin, w3)
        GPIO.output(M1_coil_B_2_pin, w4)
    elif motor == 2:
        GPIO.output(M2_coil_A_1_pin, w1)
        GPIO.output(M2_coil_A_2_pin, w2)
        GPIO.output(M2_coil_B_1_pin, w3)
        GPIO.output(M2_coil_B_2_pin, w4)

def forward(motor, delay, steps):
    for i in range(steps):
        for j in range(StepCount):
            setStep(motor, Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)

def backwards(motor, delay, steps):
    for i in range(steps):
        for j in reversed(range(StepCount)):
            setStep(motor, Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)


# Script

if __name__ == '__main__':

    # Set speed and reactiveness of motors

    delay = 1           # Speed of motor in ms (time between steps)
    steps = 1           # Steps per interation

    # With steps = 1, there's no jitter when moving two axis at the same time. However, movement speed is halved.

    while True:

        motor_1_forward = GPIO.input(12)
        motor_1_backward = GPIO.input(16)
        motor_2_forward = GPIO.input(18)
        motor_2_backward = GPIO.input(22)

        if motor_1_forward == False:
            forward(1, int(delay)/1000.0, int(steps))
        elif motor_1_backward == False:
            backwards(1, int(delay)/1000.0, int(steps))
        else:
            setStep(1,0,0,0,0)

        if motor_2_forward == False:
            forward(2, int(delay)/1000.0, int(steps))
        elif motor_2_backward == False:
            backwards(2, int(delay)/1000.0, int(steps))
        else:
            setStep(2,0,0,0,0)

        time.sleep(0.001)