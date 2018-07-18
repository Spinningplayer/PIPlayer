from omxplayer.player import OMXPlayer
from pathlib import Path
import RPi.GPIO as GPIO
import time
path = Path("/home/pi/Videos/Video.mp4")

player = None
state = 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

while True:
    if not GPIO.input(4):
        if state == 0:
            print("Play")
            try:
                global player
                player = OMXPlayer(path)
		state += 1
		time.sleep(2)
            except Exception as e:
                print('Exception in play loop')
                print(e)
        elif state == 1:
            print("Pause")
            try:
                player.pause()
		state += 1
		time.sleep(2)
            except Exception as e:
                print('Exception in pause loop')
                print(e)
        elif state == 2:
            print("Stop")
            try:
                player.quit()
		state = 0
		time.sleep(2)
            except Exception as e:
                print('Exception in stop loop')
                print(e)
