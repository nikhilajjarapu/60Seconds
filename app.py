from flask import Flask, request, redirect, send_from_directory
from twilio.rest import Client
import calendar
import datetime


app = Flask(__name__, static_folder='static')
# Try adding your own number to this list!
account_sid = "ACe7c0012d06fc3b85303d8387dffdf672"
auth_token = "a3d0ce1a83f3d9ac352c26a95c46f96e"
client = Client(account_sid, auth_token)
recordinguris = []

@app.route("/", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    call = client.calls.create("+16507136689", "+14692086476", url="https://fathomless-oasis-22928.herokuapp.com/call.xml", status_callback="http://fathomless-oasis-22928.herokuapp.com/callback", record=True)
    rec = client.recordings.list()[-1]
    rec = rec[:-4] + "mp3"
    print(rec)

    rec = client.recordings.list()[0]
    rec = rec[:-4] + "mp3"
    print(rec)

    return "Hello nikhil u boosted ape"

@app.route("/callback", methods=['GET', 'POST'])
def callback():
    print(len(client.recordings.list()))

    for i in client.recordings.list():
        print(i.uri)

    return "callback func boiz"



@app.route("/call.xml", methods=['GET', 'POST'])
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


if __name__ == "__main__":
    app.run(debug=True)


