from urllib.request import urlopen
from flask import Flask, render_template, request, flash
import json
app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/hello")
def index():
	flash("what's your name?")
	return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
	# data = request.form['ticket_id']
	# print("\nrequest.data={}".format(request.data))
	json_data = json.loads(request.data)
	if json_data['message']['ticket_id']:
		ticket_id = json_data['message']['ticket_id']
		print("Ticket_is is : ",format.ticket_id)
		# flash("Hi "+str(ticket_id)+ ", great to see you!" )
		render_template("index.html")
		return 'success', 200
		# return render_template("index.html")
