#!/usr/bin/env python

import subprocess
import time
import os

import RPi.GPIO as GPIO

GPIO_PIN = 18  # Which GPIO pin you're using to control the fan.

GPIO.setmode(GPIO.BOARD)
GPIO.setup(GPIO_PIN, GPIO.OUT)
GPIO.output(GPIO_PIN, False)
