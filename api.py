from flask import Flask,request
import json 
import datetime
app = Flask(__name__)

BAYS=4
RESERVATIONS={}

def rebook(name,date):
	for i in range(1,BAYS):
		if RESERVATIONS[date].get(i) and RESERVATIONS[date][i]["name"]==name:
			return True
	return False


# Routing

@app.route("/book/<int:bay>/<name>/<date>")
def book(bay,name,date): #date -> DD:MM:YYYY
	try:
		parsed_date = datetime.datetime.strptime(date,"%d:%m:%Y")
	except ValueError:
		return "Invalid Date Format. Format Should be DD:MM:YYYY"
	if bay > BAYS:
		return f"{name}, this bay {bay} doesn't exist"
	elif datetime.datetime.strptime(date,"%d:%m:%Y") == datetime.datetime.now().strftime('%d/%m/%Y'):
		return f"{name}, Reservation can't be done on same day"
	elif RESERVATIONS.get(date) and RESERVATIONS[date].get(bay) and RESERVATIONS[date][bay]:
		return f"{name} on {date} bay {bay} is already booked by someone"
	elif RESERVATIONS.get(date) and rebook(name,date):
		return f"{name}, you already booked"
	else:
		if RESERVATIONS.get(date) is None:
			RESERVATIONS[date]={}
		RESERVATIONS[date][bay]={}
		RESERVATIONS[date][bay]["name"]=name
		return f"Congrats! {name}, your reserved bay no. {bay} on {parsed_date.strftime('%d/%m/%Y')}"

@app.route("/dev/<date>")
def dev(date):
	try:
		datetime.datetime.strptime(date,"%d:%m:%Y")
	except ValueError:
		return "Invalid Date Format. Format Should be DD:MM:YYYY"
	if RESERVATIONS.get(date):
		return RESERVATIONS[date]
	return f"No Reservation at {date}"

app.run("0.0.0.0",8080)
