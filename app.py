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
	print("\nrequest.data={}".format(request.data))
	json_data = json.loads(request.data)
	print(json_data['ticket_id'])
	return request.data
	# flash("Hi " +json.dumps(request.json)+ ", great to see you!")
	# if data:
	# 	flash("Data here!")
	# else:
	# 	flash("No data sorry!!!")
		# flash("Hi  , great to see you!")
	# return render_template("index.html")
