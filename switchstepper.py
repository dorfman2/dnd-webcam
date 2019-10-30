#!/usr/bin/env python3

# This code is written by Jeff Dorfman.

# Import Dependancies

import RPi.GPIO as GPIO
import time, asyncio
from RpiMotorLib import RpiMotorLib

# Stepper 1 Pins

tilt_gpio_pins = [4, 17, 27, 22]

tilt = RpiMotorLib.BYJMotor('Tilt', '28BYJ')

# Stepper 2 Pins

pan_gpio_pins = [6, 13, 19, 26]

pan = RpiMotorLib.BYJMotor('Pan', '28BYJ')

# Functions

async def move_up():
    tilt.motor_run(tilt_gpio_pins,.001,50,False,False,"half", .05)

async def move_down():
    tilt.motor_run(tilt_gpio_pins,.001,50,True,False,"half", .05)

async def move_left():
    pan.motor_run(pan_gpio_pins,.001,50,False,False,"half", .05)

async def move_right():
    pan.motor_run(pan_gpio_pins,.001,50,True,False,"half", .05)


# Script

async def main():

    while True:


        direction = input('Direction? ')
        #steps = input('Steps? ')


        if direction == 'up':
            task = asyncio.create_task(move_up())
        elif direction == 'down':
            task = asyncio.create_task(move_down())

        if direction == 'left':
            task = asyncio.create_task(move_left())
        elif direction == 'right':
            task = asyncio.create_task(move_right())

        

        await task
        time.sleep(0.1)

asyncio.run(main())