from flask import Flask, send_file, request
from omxplayer.player import OMXPlayer
from pathlib import Path
from wand.image import Image
import RPi.GPIO as GPIO
import wand
import os
import time

app = Flask(__name__)
path = Path("/home/pi/Videos/Video.mp4")
imagePath = Path("./nee.png")

player = None

state = False

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

@app.route('/')
def test():
    return send_file("index.html", mimetype="text/html")


@app.route('/favicon.ico')
def favicon():
    return send_file("nee.png", mimetype="image/png")


@app.route('/play')
def play():
    try:
	os.system('killall omxplayer.bin')
        global player
        player = Player(path)
        return "success"
    except Exception as e:
        print(e)
        return "error"


@app.route('/stop')
def stop():
    try:
	global player
        player.quit()
        return "success"
    except Exception as e:
        print(e)
        return "error"

@app.route('/display')
def display():
    # try:
    #     image = request.args.get('path')
    #     imagePath = Path(image)
    # except:
    #     return "Invalid input"

    try:
        with Image(filename='nee.png') as img:
            wand.display.display(img)
        return "success"
    except Exception as e:
        print(e)
        return "error: couldn't display image"

def playVideo(pin):
	global state
	global player
	if not state:
    		try:
			print("Starting video")
        		player = OMXPlayer(path)
			state = False
			time.sleep(5)
        		return "success"
    		except Exception as e:
        		print(e)
        		return "error"
	else:
		try:
			print("Stopping video")
			player.quit
			os.command('killall omxplayer')
			state = True
			time.sleep(5)
			return "success"
		except Exception as e:
 			print(e)
			return "error"


def stopVideo(pin):
    try:
	global player
	player.quit()
        return "success"
    except Exception as e:
        print(e)
        return "error"


GPIO.add_event_detect(4, GPIO.FALLING, callback=playVideo, bouncetime=5000)
GPIO.add_event_detect(17, GPIO.RISING, callback=stopVideo, bouncetime=5000)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337)

GPIO.cleanup()
