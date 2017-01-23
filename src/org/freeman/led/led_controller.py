#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

class LedController:
    RED_CHANNEL = 14
    GREEN_CHANNEL = 15
    BLUE_CHANNEL = 18

    def __init__(self) :
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(RED_CHANNEL, GPIO.OUT)
        GPIO.setup(GREEN_CHANNEL, GPIO.OUT)
        GPIO.setup(BLUE_CHANNEL, GPIO.OUT)

        GPIO.output(RED_CHANNEL, GPIO.LOW)
        GPIO.output(GREEN_CHANNEL, GPIO.LOW)
        GPIO.output(BLUE_CHANNEL, GPIO.LOW)

        # start a loop with RGB in 3 seconds
        self.rPWM = GPIO.PWM(RED_CHANNEL, 1)
        self.rPWM.start(30)
        time.sleep(1)
        self.rPWM.stop()

        self.gPWM = GPIO.PWM(GREEN_CHANNEL, 1)
        self.gPWM.start(30)
        time.sleep(1)
        self.gPWM.stop()

        self.bPWM = GPIO.PWM(BLUE_CHANNEL, 1)
        self.bPWM.start(30)
        time.sleep(1)
        self.bPWM.stop()
