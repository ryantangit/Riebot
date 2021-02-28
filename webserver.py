from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return "cheesing the system"

def run():
  app.run(host= '0.0.0.0', port = 8080)

def cheese():
  t = Thread(target = run)
  t.start()