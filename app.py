from urllib.request import urlopen
from flask import Flask, render_template, request, flash
import json
import requests

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"
API_KEY='9f6686031db64b948313dd194bb4319b76cd5641c6cb6080d16ae494ce063678'
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
		print(ticket_id)
		print('send email response')
		send_email_response(ticket_id)

		print('send internal email')
		# send_internal_mail(ticket_id)
		return 'success', 200
		# return render_template("index.html")


def send_email_response(ticket_id):
	# print(ticket_id)
	response_url = "https://saikamat2.gorgias.com/api/tickets/"+str(ticket_id)+"/messages"
	print(response_url)
	payload = json.dumps({
		"channel": "email",
		"from_agent": True,
		"source": {
			"type": "email",
			"from": {
			"id": 11942663,
			"name": "Saikamat2 Support",
			"address": "nxy04g6pe705zqm2@emails.gorgias.com"
			},
			"to": [
			{
				"id": 11944965,
				"name": "Sai",
				"address": "sai.s.kamat@gmail.com"
			}
			]
		},
		"via": "helpdesk",
		"body_html": "Hello,<br><br>\n\n        I can't place an order on your site, it says: I don't have enough credit.<br>\n        How can I add some credits?<br><br>\n\n        Cheers,<br>\n        John Doe\n        ",
		"body_text": "Hello,\n\n        I can't place an order on your site, it says: I don't have enough credit.\n        How can I add some credits?\n\n        Cheers,\n        John Doe\n        ",
		"created_datetime": "2022-08-25T19:42:21.468912",
		"external_id": "",
		"failed_datetime": None,
		"message_id": "<123345676453.2445.234@web>",
		"receiver": {
			"id": 11944965
		},
		"sender": {
			"id": 11942663
		},
		"sent_datetime": "2022-08-25T19:42:21.468912",
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


def send_internal_mail(ticket_id):
	response_url = "https://saikamat2.gorgias.com/api/tickets/"+str(ticket_id)+"/messages"
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


