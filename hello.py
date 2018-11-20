# import os
# from flask import Flask, g, render_template
# import flask_sijax

# path = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')
# app = Flask(__name__)

# app.config['SIJAX_STATIC_PATH'] = path
# app.config['SIJAX_JSON_URI'] = '/static/js/sijax/json2.js'
# flask_sijax.Sijax(app)

# @app.route('/')
# def index():
#    return 'Index'
	
# @flask_sijax.route(app, '/hello')
# def hello():
#    def say_hi(obj_response):
#       obj_response.alert('Hi there!')
#    if g.sijax.is_sijax_request:
#       # Sijax request detected - let Sijax handle it
#       g.sijax.register_callback('say_hi', say_hi)
#       return g.sijax.process_request()
#    return render_template('sijaxexample.html')

# if __name__ == '__main__':
#    app.run(debug = True)

from flask import Flask, redirect, url_for, render_template, request
# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('log_in.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST' and
   request.form['username'] == 'admin' :
   return redirect(url_for('success'))
   return redirect(url_for('index'))

@app.route('/success')
def success():
   return 'logged in successfully'
	
if __name__ == '__main__':
   app.run(debug = True)
