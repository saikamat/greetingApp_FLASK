from urllib.request import urlopen
from flask import Flask, render_template, request, flash
import json
import requests
from datetime import datetime

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"
API_KEY='a60565fcf573bc674908bbbd0f1c10cd96f29f6dd7b16f2a6d91374288bda3e7'
API_KEY_BASE64='c2FpLnMua2FtYXQrMDhAZ21haWwuY29tOmE2MDU2NWZjZjU3M2JjNjc0OTA4YmJiZDBmMWMxMGNkOTZmMjlmNmRkN2IxNmYyYTZkOTEzNzQyODhiZGEzZTc='

@app.route("/hello")
def index():
	flash("what's your name??")
	return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
	json_data = json.loads(request.data)
	if json_data['message']['ticket_id']:
		ticket_id = json_data['message']['ticket_id']
		user = json_data['message']['sender']['email']
		email_text = 'Hi, our agent will be with you shortly .'
		message_text = 'Priority #1'
		sender_id = json_data['message']['sender']['id']
		receiver_id= json_data['message']['receiver']['id']
		receiver_email= json_data['message']['receiver']['email']
		sender_name = json_data['message']['sender']['firstname']
		# receiver_name = json_data['message']['receiver']['firstname']
		# password = API_KEY_BASE64
		print(ticket_id)
		print('send email response')
		# ideally I'd have preferred passing as a JSON object.
		send_email_response(ticket_id, user, email_text, sender_id, receiver_id, receiver_email, sender_name)

		#print('send internal email')
		# send_internal_mail(ticket_id, user, message_text, sender_id)
		return 'success', 200
		# return render_template("index.html")

def send_email_response(ticket_id, user, email_text, sender_id, receiver_id, receiver_email, sender_name):
	# print(ticket_id)
	response_url = "https://saikamat8.gorgias.com/api/tickets/"+str(ticket_id)+"/messages"
	print(response_url)
	payload = json.dumps({
		"channel": "email",
		"from_agent": True,
		"source": {
			"type": "email",
			"from": {
			"id": sender_id,
			"name": sender_name,
			"address": user
			},
			"to": [
			{
				"id": receiver_id,
				#"name": receiver_name,
				"address": receiver_email
			}
			]
		},
		"via": "helpdesk",
		"body_html": email_text,
		"body_text": email_text,
		"created_datetime": "2022-08-26T17:16:41.966927",
		"external_id": "",
		"failed_datetime": None,
		"message_id": "<123345676453.2445.234@web>",
		"receiver": {
			"id": receiver_id
		},
		"sender": {
			"id": sender_id
		},
		"sent_datetime": "2022-08-26T17:16:41.966927",
		"subject": "Thank you for reaching out"
	})
	headers = {
		"Accept": "application/json",
		"Content-Type": "application/json",
		"Authorization": "Basic "+API_KEY_BASE64
	}
	print('before sending')
	# response = requests.post(response_url, json=payload, headers=headers)
	response = requests.request("POST", response_url, headers=headers, data=payload)
	print('after sending')

	print(response.text)


def send_internal_mail(ticket_id, user, message_text, sender_id):
	response_url = "https://saikamat8.gorgias.com/api/tickets/"+str(ticket_id)+"/messages"
	print(response_url)
	payload = json.dumps({
		"channel": "email",
		"from_agent": True,
		"source": {
			"type": "internal-note",
			"from": {
			"id": sender_id,
			# "name": sender_name,
			"address": user
			},
			"to": [
			{
				"id": sender_id,
				#"name": receiver_name,
				"address": user
			}
			]
		},
		"via": "helpdesk",
		"body_html": message_text,
		"body_text": message_text,
		"created_datetime": "2022-08-26T17:16:41.966927",
		"external_id": "",
		"failed_datetime": None,
		"message_id": "<123345676453.2445.234@web>",
		"receiver": {
			"id": sender_id
		},
		"sender": {
			"id": sender_id
		},
		"sent_datetime": "2022-08-26T17:16:41.966927",
		"subject": "Thank you for reaching out"
	})
	headers = {
		"Accept": "application/json",
		"Content-Type": "application/json",
		"Authorization": "Basic "+API_KEY_BASE64
	}

	# response = requests.post(response_url, json=payload, headers=headers)
	response = requests.request("POST", response_url, headers=headers, data=payload)


	print(response.text)


