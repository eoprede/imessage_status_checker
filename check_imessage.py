import os
import urllib.request
import json
import smtplib, ssl
import datetime
from email.message import EmailMessage

def send_email(imessage_status_text, config):
	msg = EmailMessage()
	msg['Subject'] = f"iMessage status report"
	msg['From'] = config["sender_email"]
	msg['To'] = config["receiver_email"] 
	msg.set_content(f"{imessage_status_text}\niMessage status checked on {datetime.datetime.now()}")

	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(config["smtp_server"], config["smpt_server_port"], context=context) as server:
	    server.login(config["sender_email"], config["email_password"])
	    server.send_message(msg)

# load config
with open('config.json') as f:
    config = json.load(f)

# check iMessage status
print("Checking iMessage status")
imessage_status = {}
for address in config["check_imessage_for"]:
	req = urllib.request.Request(f"{config['bubbles_server']}/api/v1/handle/availability/imessage?password={config['bubbles_pw']}&address={address}", headers={'User-Agent': 'Mozilla/5.0'})
	contents = urllib.request.urlopen(req).read()
	json_response = json.loads(contents.decode('utf-8'))
	if json_response["status"] == 200:
		if json_response["data"]["available"]:
			imessage_status.update({address:"Registered"})
		else:
			imessage_status.update({address:"Not Registered"})
	else:
		print("Got non-200 response")

imessage_status_text = json.dumps(imessage_status,sort_keys=True, indent=2)
print(imessage_status_text)
if config["send_email"]:
	send_email(imessage_status_text, config)
	print("Email sent")