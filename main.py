from flask import Flask, send_file
app = Flask(__name__)

@app.route('/')
def test():
    return send_file("index.html", mimetype="text/html")

@app.route('/favicon.ico')
def favicon():
    return send_file("nee.png", mimetype="image/png")

if __name__ == '__main__':
    app.run()
