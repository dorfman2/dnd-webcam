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

async def move_up(delay, step):
    tilt.motor_run(tilt_gpio_pins, float(delay), int(step), True, False,"half", .05)

async def move_down(delay, step):
    tilt.motor_run(tilt_gpio_pins, float(delay), int(step), False, False,"half", .05)

async def move_left(delay, step):
    pan.motor_run(pan_gpio_pins, float(delay), int(step), True, False,"half", .05)

async def move_right(delay, step):
    pan.motor_run(pan_gpio_pins, float(delay), int(step), False, False,"half", .05)


# Script

async def main():

    while True:


        direction = input('Direction? ')

        if direction == 'exit':
            GPIO.cleanup()
            exit()


        speed = input('Speed (fast/slow)? ')
        steps = input('Steps? ')

        if speed == 'fast':
            speed = 0.001
        elif speed == 'slow':
            speed = 0.01
        else:
            speed = 0.1
        #steps = input('Steps? ')



        asyncio.create_task(move_up(0.001, 50))
        asyncio.create_task(move_down(0.001, 50))
        asyncio.create_task(move_left(0.001, 50))
        asyncio.create_task(move_right(0.001, 50))

        if direction == 'up':
            task = asyncio.create_task(move_up(speed, steps))

        elif direction == 'down':
            task = asyncio.create_task(move_down(speed, steps))

        elif direction == 'left':
            task = asyncio.create_task(move_left(speed, steps))

        elif direction == 'right':
            task = asyncio.create_task(move_right(speed, steps))
        

        

        await task
        time.sleep(0.1)

asyncio.run(main())