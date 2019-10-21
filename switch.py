import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)   #Enable switch and pull up resistors
while True:
    input_state = GPIO.input(12)    #Read and store value of switch to var
    if input_state == False:
        print('button pressed')
        time.sleep(0.3)