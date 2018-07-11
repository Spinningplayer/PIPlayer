from flask import Flask, send_file, request
from omxplayer.player import OMXPlayer
from pathlib import Path
from wand.image import Image
import RPi.GPIO as GPIO
import wand

app = Flask(__name__)
player = None
path = Path("/home/pi/Videos/Video.mp4")
imagePath = Path("./nee.png")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(1, GPIO.IN, pull_up_down = GPIO.PUD_OFF)


@app.route('/')
def test():
    return send_file("index.html", mimetype="text/html")


@app.route('/favicon.ico')
def favicon():
    return send_file("nee.png", mimetype="image/png")


@app.route('/play')
def play():
    try:
        global player
        player = OMXPlayer(path)
        return "success"
    except Exception as e:
        print(e)
        return "error"


@app.route('/stop')
def stop():
    try:
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


GPIO.add_event_detect(1, GPIO.RISING, callback=play)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337)

GPIO.cleanup()
