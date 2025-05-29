from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def get_time():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>Current Time of the Day</h1><p>{current_time}</p>"

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)

