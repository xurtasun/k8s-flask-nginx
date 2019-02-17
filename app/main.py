from flask import Flask
from datetime import datetime
import pytz
# the all-important app variable:
app = Flask(__name__)
localTime = pytz.timezone("Europe/Madrid")

@app.route("/")
def getDate():
    return datetime.now(localTime).strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=3300)
