from flask import Flask, render_template, request, flash
import logging
app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/hello")
def index():
	flash("what's your name?")
	return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
	data = request.json
	if data:
		logging.info("Received Data = ")
	flash("Hi  , great to see you!")
	return render_template("index.html")
