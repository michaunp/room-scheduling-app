import pyrebase

from flask import Flask, flash, redirect, render_template, \
request, url_for

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

#Your web app's Firebase configuration
firebaseConfig = {
	"apiKey": "AIzaSyA-Ueu9QRqP3m-Su5h-w-C1iKlC4cwRvtc",
	"authDomain": "room-sched-cloudcomp.firebaseapp.com",
	"databaseURL": "https://room-sched-cloudcomp.firebaseio.com",
	"projectId": "room-sched-cloudcomp",
	"storageBucket": "room-sched-cloudcomp.appspot.com",
	"messagingSenderId": "1092960328863",
	"appId": "1:1092960328863:web:cdb679dac22f6894c716aa",
	"measurementId": "G-1ELV6G08MK"
}

#Initialize Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/landing/<username>')
def landingPage():
	return render_template('landing.html', username=username)

@app.route('/login', methods=['GET', 'POST'])
def login():

	error = None
	unsuccessful = 'Please check your credentials'

	if request.method == 'POST':
		email = request.form['username']
		password = request.form['password']

		try:
			auth.sign_in_with_email_and_password(email, password)
			return render_template('dashboard.html', username=email)
		except:
			return render_template('login.html', us=unsuccessful)

	return render_template('login.html', error=error)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	error = None
	mesg = 'Please enter your credentials'
	unsuccessful = 'Username Exist, or password must be 6 characters'

	if request.method == 'POST':

		email = request.form['username']
		password = request.form['password']

		try:
			user = auth.create_user_with_email_and_password(email, password)
			return render_template('landing.html', username=email)

		except Exception as e:
			print(e)
			return render_template('signup.html', us=unsuccessful)

	return render_template('signup.html', error=error)

@app.route('/hello')
def hello():
	return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
	app.run(host='0.0.0.0')
