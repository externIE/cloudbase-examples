import os
import datetime

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    now = datetime.datetime.now()
    print("北京时间 %s" % now.strftime("%Y-%m-%d %H:%M:%S"))
    delta = datetime.timedelta(hours=-12)
    print("纽约时间 %s" % (now+delta).strftime("%Y-%m-%d %H:%M:%S"))

    delta = datetime.timedelta(hours=-7)
    print("伦敦时间 %s" % (now+delta).strftime("%Y-%m-%d %H:%M:%S"))

    delta = datetime.timedelta(hours=1)
    print("大阪时间 %s" % (now+delta).strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
