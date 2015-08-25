# encoding=utf8 
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# all tha imports
import sqlite3
import random
from deskDB import desks

from flask import (Flask, render_template, redirect, url_for, request, make_response, flash)


app = Flask(__name__)
app.config.from_object(__name__)



@app.route('/')
def home():
	desk = 'static/' + random.choice(desks) + '.jpg'
	return render_template("home.html", NextDesks = desk)


app.run(debug=True, port=3000, host='0.0.0.0')
