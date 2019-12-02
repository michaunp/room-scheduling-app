import json
import logging
import os
import pyrebase

from flask import Flask, flash, redirect, render_template, \
request, url_for, jsonify
import sqlalchemy
#from flask_sqlalchemy import SQLAlchemy

db_user = os.environ.get("DB_USER")
db_pass = os.environ.get("DB_PASS")
db_name = os.environ.get("DB_NAME")
cloud_sql_connection_name = os.environ.get("CLOUD_SQL_CONNECTION_NAME")
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

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

db = sqlalchemy.create_engine(
    sqlalchemy.engine.url.URL(
        drivername='mysql+pymysql',
        username= 'root',
        password= '20CloudComp19!',
        database= 'roomscheddb',
        query={
            'unix_socket': '/cloudsql/{}'.format('room-sched-cloudcomp:us-east4:room-sched-db')
        }
    ),
    pool_size=5,
    max_overflow=2,
    pool_timeout=30,  # 30 seconds
    pool_recycle=1800,  
)


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
			with db.connect() as conn:
				room_data = conn.execute('select * from ROOM;').fetchall()
				rooms = []
				for row in room_data:
					rooms.append({
					"Room Number": row[1],
					"Capacity": row[4],
					"Room Types": row[0].split(','),
					"Status": row[5]
					})
				json_rooms = json.dumps(rooms)
			return render_template('dashboard.html', room_data=json_rooms)
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

'''@app.route('/events/create', methods=['GET', 'POST'])
def createEvent():
	#TODO: method to handle input from user in the form of the
	 '''

if __name__ == "__main__":
    	app.run(host='0.0.0.0')
