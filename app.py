from flask import Flask, request, redirect
from twilio.rest import Client
import calendar
import datetime


app = Flask(__name__)
# Try adding your own number to this list!
account_sid = "ACe7c0012d06fc3b85303d8387dffdf672"
auth_token = "a3d0ce1a83f3d9ac352c26a95c46f96e"
client = Client(account_sid, auth_token)
recordinguris = []

@app.route("/", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    call = client.api.account.calls.create(to="+16507136689", from_="+14692086476", url="https://raw.githubusercontent.com/TheCurryMan/60Seconds/master/call.xml")
    #if calendar.monthrange(datetime.datetime.now().year,datetime.datetime.now().month)[1] == datetime.datetime.now().day:
    for recording in client.recordings.list():
        recordinguris.append(recording.uri)
    return recordinguris

if __name__ == "__main__":
    app.run(debug=True)


