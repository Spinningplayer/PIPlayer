from flask import Flask, send_file
from omxplayer.player import OMXPlayer
from pathlib import Path

app = Flask(__name__)
player = None
path = Path("/home/pi/Videos/Girl.mp4")


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


if __name__ == '__main__':
    app.run()
