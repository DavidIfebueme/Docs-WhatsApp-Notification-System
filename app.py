# this script is meant to interact with the google apps to detect the changes
import os
from flask import Flask, request
from twilio.rest import Client

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# gotta load Twilio credentials from env

client = Client(os.getenv('TWILIO_ACCOUNT_SID'), ost.getenv('TWILIO_AUTH_TOKEN'))

@app.route('/update', methods=['POST'])
def update():
    data = request.json
    changes = data['changes']
    timestamp = data['timestamp']

    return 'Success', 200

@app.route('/sendWhatsApp', methods=['POST'])
def send_whatsapp():
    data = request.json
    changes = data['changes']
    timestamp = data['timestamp']
    message_body = f"Document updated at {timestamp}.\nChanges:\n{changes}" #probably dont need this as the whatsapp messge woud have a timmetamp

    message = client.messages.create(
        body=message_body,
        from_=os.getenv('WHATSAPP_FROM'),
        to=os.getenv('WHATSAPP_TO')
    )

    return 'WhatsApp message sent', 200

if __name__ == '__main__':
    app.run(debug=True)
