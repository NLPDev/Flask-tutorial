import os
from flask import Flask, g, render_template
import flask_sijax

path = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')
app = Flask(__name__)

app.config['SIJAX_STATIC_PATH'] = path
app.config['SIJAX_JSON_URI'] = '/static/js/sijax/json2.js'
flask_sijax.Sijax(app)

@app.route('/')
def index():
   return 'Index'
	

if __name__ == '__main__':
   app.run(debug = True)


