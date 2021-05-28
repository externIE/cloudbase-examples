import os
import datetime

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    now = datetime.datetime.now()
    s = "北京时间 %s\n" % now.strftime("%Y-%m-%d %H:%M:%S")
    delta = datetime.timedelta(hours=-12)
    s += "纽约时间 %s\n" % (now+delta).strftime("%Y-%m-%d %H:%M:%S")
    delta = datetime.timedelta(hours=-7)
    s += "伦敦时间 %s\n" % (now+delta).strftime("%Y-%m-%d %H:%M:%S")
    delta = datetime.timedelta(hours=1)
    s += "大阪时间 %s\n" % (now+delta).strftime("%Y-%m-%d %H:%M:%S")
    return s

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
