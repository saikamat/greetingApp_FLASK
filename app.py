from urllib.request import urlopen
from flask import Flask, render_template, request, flash
import json
import requests

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"
API_KEY='b8d9dc5526a4bf3a2a0bd04a53e71565289f2bd562cc716e55d66a9ab5a6c38b'
API_KEY_BASE64='dmVub204OTE0QG1haWwuY29tOjlmNjY4NjAzMWRiNjRiOTQ4MzEzZGQxOTRiYjQzMTliNzZjZDU2NDFjNmNiNjA4MGQxNmFlNDk0Y2UwNjM2Nzg='

@app.route("/hello")
def index():
	flash("what's your name?")
	return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
	json_data = json.loads(request.data)
	if json_data['message']['ticket_id']:
		ticket_id = json_data['message']['ticket_id']
		user = json_data['ticket']['assignee_user']['email']
		email_text = 'Hi, our agent will be with you shortly.'
		sender_id = json_data['message']['sender']['id']
		receiver_id= json_data['message']['receiver']['id']
		receiver_email= json_data['message']['receiver']['email']
		sender_name = json_data['message']['sender']['firstname']
		receiver_name = json_data['message']['receiver']['firstname']
		# password = API_KEY_BASE64
		print(ticket_id)
		print('send email response')
		# ideally I'd have preferred passing as a JSON object.
		send_email_response(ticket_id, user, email_text, sender_id, receiver_id, receiver_email, sender_name, receiver_name)

		#print('send internal email')
		# send_internal_mail(ticket_id)
		return 'success', 200
		# return render_template("index.html")


def send_email_response(ticket_id, user, email_text, sender_id, receiver_id, receiver_email, sender_name, receiver_name):
	# print(ticket_id)
	response_url = "https://saikamat3.gorgias.com/api/tickets/"+str(ticket_id)+"/messages"
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
				"name": receiver_name,
				"address": receiver_email
			}
			]
		},
		"via": "helpdesk",
		"body_html": email_text,
		"body_text": email_text,
		"created_datetime": "2022-08-25T19:28:21.468912",
		"external_id": "",
		"failed_datetime": None,
		"message_id": "<123345676453.2445.234@web>",
		"receiver": {
			"id": receiver_id
		},
		"sender": {
			"id": sender_id
		},
		"sent_datetime": "2022-08-25T19:28:21.468912",
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


def send_internal_mail(ticket_id):
	response_url = "https://saikamat3.gorgias.com/api/tickets/"+str(ticket_id)+"/messages"
	print('in internal emailL:****' + response_url)
	payload = json.dumps({
		"channel": "email",
		"from_agent": True,
		"source": {
			"type": "internal-note",
			"from": {
			"id": 11942663,
			"name": "Sai from Gorgias Support",
			"address": "nxy04g6pe705zqm2@emails.gorgias.com"
			},
			"to": [
			{
				"id": 11942663,
				"name": "Sai from Gorgias Support",
				"address": "nxy04g6pe705zqm2@emails.gorgias.com"
			}
			]
		},
		"via": "helpdesk",
		"body_html": "This client needs to be take care of quickly.",
		"body_text": "This client needs to be take care of quickly.",
		"created_datetime": "2022-08-25T18:18:21.468912",
		"external_id": "",
		"failed_datetime": None,
		"message_id": "<123345676453.2445.234@web>",
		"receiver": {
			"id": 11942663
		},
		"sender": {
			"id": 11942663
		},
		"sent_datetime": "2022-08-25T18:18:21.468912",
		"subject": "Re:Refund request"
	})
	headers = {
		"Accept": "application/json",
		"Content-Type": "application/json",
		"Authorization": "Basic "+API_KEY_BASE64
	}

	# response = requests.post(response_url, json=payload, headers=headers)
	response = requests.request("POST", response_url, headers=headers, data=payload)


	print(response.text)


