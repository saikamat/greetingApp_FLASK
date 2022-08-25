from urllib.request import urlopen
from flask import Flask, render_template, request, flash
import json
import requests

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"
API_KEY='d55342c9dac491ada6566cbd337c596a7d033f4a35fd7cb93888f2868afb54b6'

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
	# payload = {
	# "receiver": {"id": 11899069},
	# "sender": {"id": 11899005},
	# "source": {
	# 	"to": [
	# 		{
	# 			"name": "Shruti",
	# 			"address": "kuberaspeaking@gmail.com"
	# 		}
	# 	],
	# 	"from": {
	# 		"name": "Sai from Gorgias Support",
	# 		"address": "norwayumfall@gmail.com"
	# 	},
	# 	"type": "email"
	# },
	# "channel": "email",
	# "via": "helpdesk",
	# "body_html": "Ko Koo Koo Koo Koo",
	# "body_text": "Ko Koo Koo Koo Koo",
	# "created_datetime": "2022-08-25T16:42:21.468912",
	# "from_agent": True,
	# "sent_datetime": "2022-08-25T16:42:21.468912",
	# "subject": "Birdemic"
	# }
	# headers = {
	# 	"Accept": "application/json",
	# 	"Content-Type": "application/json",
	# 	"Authorization": "Basic "+API_KEY
	# }

	# response = requests.post(response_url, json=payload, headers=headers)

	# print(response.text)

