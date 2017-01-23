#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

class _LedChannel() :
    RED_CHANNEL = 14
    GREEN_CHANNEL = 15
    BLUE_CHANNEL = 18

class LedController:
    def __init__(self) :
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(_LedChannel.RED_CHANNEL, GPIO.OUT)
        GPIO.setup(_LedChannel.GREEN_CHANNEL, GPIO.OUT)
        GPIO.setup(_LedChannel.BLUE_CHANNEL, GPIO.OUT)

        GPIO.output(_LedChannel.RED_CHANNEL, GPIO.LOW)
        GPIO.output(_LedChannel.GREEN_CHANNEL, GPIO.LOW)
        GPIO.output(_LedChannel.BLUE_CHANNEL, GPIO.LOW)

        # start a loop with RGB in 3 seconds
        self.rPWM = GPIO.PWM(_LedChannel.RED_CHANNEL, 1)
        self.rPWM.start(30)
        time.sleep(1)
        self.rPWM.stop()

        self.gPWM = GPIO.PWM(_LedChannel.GREEN_CHANNEL, 1)
        self.gPWM.start(30)
        time.sleep(1)
        self.gPWM.stop()

        self.bPWM = GPIO.PWM(_LedChannel.BLUE_CHANNEL, 1)
        self.bPWM.start(30)
        time.sleep(1)
        self.bPWM.stop()

        GPIO.output(_LedChannel.RED_CHANNEL, GPIO.LOW)
        GPIO.output(_LedChannel.GREEN_CHANNEL, GPIO.LOW)
        GPIO.output(_LedChannel.BLUE_CHANNEL, GPIO.LOW)
