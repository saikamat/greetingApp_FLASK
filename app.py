from urllib.request import urlopen
from flask import Flask, render_template, request, flash
import json
import requests

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"
API_KEY='3dbcf0f84c9aab441c96a87394560384698f2fbf319eace0155e22effef0737f'

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
		send_email_response(ticket_id)
		return 'success', 200
		# return render_template("index.html")


def send_email_response(ticket_id):
	# print(ticket_id)
	response_url = "https://saikamat.gorgias.com/api/tickets/"+str(ticket_id)+"/messages"
	print(response_url)
	payload = {
		"channel": "email",
		"from_agent": true,
		"source": {
			"type": "email",
			"from": {
				"id": 11899005,
				"name": "Sai from Gorgias Support",
				"address": "pqe41g4kn4d58yl3@emails.gorgias.com"
			},
			"to": [
				{
					"id": 11899069,
					"name": "Shruti",
					"address": "kuberaspeaking@gmail.com"
				}
			]
		},
		"via": "helpdesk",
		"body_html": "Hello,<br><br>\n\n        I can't place an order on your site, it says: I don't have enough credit.<br>\n        How can I add some credits?<br><br>\n\n        Cheers,<br>\n        John Doe\n        ",
		"body_text": "Hello,\n\n        I can't place an order on your site, it says: I don't have enough credit.\n        How can I add some credits?\n\n        Cheers,\n        John Doe\n        ",
		"created_datetime": "2022-08-25T16:42:21.468912",
		"external_id": null,
		"failed_datetime": null,
		"message_id": null,
		"receiver": {
			"id": 11899069
		},
		"sender": {
			"id": 11899005
		},
		"sent_datetime": "2022-08-25T16:42:21.468912",
		"subject": "Re:Refund request"
	}
	headers = {
		"Accept": "application/json",
		"Content-Type": "application/json",
		"Authorization": "Basic "+API_KEY
	}

	response = requests.post(response_url, json=payload, headers=headers)

	print(response.text)

