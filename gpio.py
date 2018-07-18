from omxplayer.player import OMXPlayer
from pathlib import Path
import RPi.GPIO as GPIO
import time

path = Path("/home/pi/Videos/Video.mp4")

player = None
state = 0

green = 14
yellow = 17
red = 27
trigger = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.output(green, GPIO.HIGH)

while True:
    if not GPIO.input(trigger):
        if state == 0:
            print("Play")
            try:
                global player
                player = OMXPlayer(path)
                state += 1
                GPIO.output(yellow, GPIO.HIGH)
                GPIO.output(red, GPIO.LOW)
                GPIO.output(green, GPIO.LOW)
                time.sleep(2)
            except Exception as e:
                print('Exception in play loop')
                print(e)
        elif state == 1:
            print("Pause")
            try:
                player.pause()
                state += 1
                GPIO.output(red, GPIO.HIGH)
                GPIO.output(yellow, GPIO.LOW)
                GPIO.output(green, GPIO.LOW)
                time.sleep(2)
            except Exception as e:
                print('Exception in pause loop')
                print(e)
        elif state == 2:
            print("Stop")
            try:
                player.quit()
                state = 0
                GPIO.output(green, GPIO.HIGH)
                GPIO.output(red, GPIO.LOW)
                GPIO.output(yellow, GPIO.LOW)
                time.sleep(2)
            except Exception as e:
                print('Exception in stop loop')
                print(e)
