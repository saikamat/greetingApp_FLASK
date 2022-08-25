from urllib.request import urlopen
from flask import Flask, render_template, request, flash
import json
import requests

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"
API_KEY='cb40d7ff4d62b0b0115fdfccd947494b475599a395adb28d89032b1346888f34'
API_KEY_BASE64='a2Fpc2hhbWF0ODlAZ21haWwuY29tOmNiNDBkN2ZmNGQ2MmIwYjAxMTVmZGZjY2Q5NDc0OTRiNDc1NTk5YTM5NWFkYjI4ZDg5MDMyYjEzNDY4ODhmMzQ='

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
		send_internal_mail(ticket_id)
		return 'success', 200
		# return render_template("index.html")


def send_email_response(ticket_id):
	# print(ticket_id)
	response_url = "https://saikamat89.gorgias.com/api/tickets/"+str(ticket_id)+"/messages"
	print(response_url)
	payload = json.dumps({
		"channel": "email",
		"from_agent": True,
		"source": {
			"type": "email",
			"from": {
			"id": 11921348,
			"name": "Sai from Gorgias Support",
			"address": "n2kmlgdyme1gde16@emails.gorgias.com"
			},
			"to": [
			{
				"id": 11922192,
				"name": "Shruti",
				"address": "kuberaspeaking@gmail.com"
			}
			]
		},
		"via": "helpdesk",
		"body_html": "Hello,<br><br>\n\n        I can't place an order on your site, it says: I don't have enough credit.<br>\n        How can I add some credits?<br><br>\n\n        Cheers,<br>\n        John Doe\n        ",
		"body_text": "Hello,\n\n        I can't place an order on your site, it says: I don't have enough credit.\n        How can I add some credits?\n\n        Cheers,\n        John Doe\n        ",
		"created_datetime": "2022-08-25T16:42:21.468912",
		"external_id": "",
		"failed_datetime": None,
		"message_id": "<123345676453.2445.234@web>",
		"receiver": {
			"id": 11922192
		},
		"sender": {
			"id": 11921348
		},
		"sent_datetime": "2022-08-25T16:42:21.468912",
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
	response_url = "https://saikamat89.gorgias.com/api/tickets/"+str(ticket_id)+"/messages"
	print(response_url)
	payload = json.dumps({
		"channel": "email",
		"from_agent": True,
		"source": {
			"type": "internal-note",
			"from": {
			"id": 11921348,
			"name": "Sai from Gorgias Support",
			"address": "n2kmlgdyme1gde16@emails.gorgias.com"
			},
			"to": [
			{
				"id": 11921348,
				"name": "Shruti",
				"address": "kaishamat89@gmail.com"
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
			"id": 11921348
		},
		"sender": {
			"id": 11921348
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


