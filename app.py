from urllib.request import urlopen
from flask import Flask, render_template, request, flash
# import logging
app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/hello")
def index():
	flash("what's your name?")
	return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
	data = urlopen('https://webhook-test-sai.herokuapp.com/greet').read()
	if data:
		flash("Data here!")
	else:
		flash("No data sorry!!!")
		# flash("Hi  , great to see you!")
	return render_template("index.html")
