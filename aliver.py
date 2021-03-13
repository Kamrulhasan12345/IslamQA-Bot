from flask import Flask, render_template
from threading import Thread

from gevent.pywsgi import WSGIServer

app = Flask("IslamQA Bot")

@app.route('/')
def main():
    return render_template('index.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])

def run():
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    http_server.serve_forever()

def aliver():
    server = Thread(target=run)
    server.start()