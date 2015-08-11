from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template("home.html")


app.run(debug=True, port=3000, host='0.0.0.0')
