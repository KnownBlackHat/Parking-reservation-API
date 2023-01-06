from flask import Flask,request
import json 

app = Flask(__name__)

BAYS=4
RESERVATIONS={}

def rebook(spot,name,date):
	for i in range(1,BAYS):
		if RESERVATIONS[date].get(i) and RESERVATIONS[date][i]["name"]==name:
			return True
	return False
		


def check_bays(spot,name,date):
	if spot > BAYS:
		return f"{name}, this spot {spot} doesn't exist"
	elif len(date) < 8:
		return "Invalid Date Format. Format Should be DD:MM:YYYY"
	elif date[2] != ":" and date[5] != ":" :
		return "Invalid Date Format. Format Should be DD:MM:YYYY"
	elif RESERVATIONS.get(date) and RESERVATIONS[date].get(spot) and RESERVATIONS[date][spot]:
		return f"{name} on {date} spot {spot} is already booked by someone"
	elif RESERVATIONS.get(date) and rebook(spot,name,date):
		return f"{name}, you already booked"
	else:
		if RESERVATIONS.get(date) is None:
			RESERVATIONS[date]={}
		RESERVATIONS[date][spot]={}
		RESERVATIONS[date][spot]["name"]=name
		return f"Congrats! {name}, your reserved spot no. {spot} for {date.replace(':','/')}"



# Routing

@app.route("/book/<int:spot>/<name>/<date>")
def book(spot,name,date): #date -> DD:MM:YYYY
	if spot > BAYS:
		return f"{name}, this spot {spot} doesn't exist"
	elif len(date) <= 8:
		return "Invalid Date Format. Format Should be DD:MM:YYYY"
	elif date[2] != ":" or date[5] != ":" :
		return "Invalid Date Format. Format Should be DD:MM:YYYY"
	elif RESERVATIONS.get(date) and RESERVATIONS[date].get(spot) and RESERVATIONS[date][spot]:
		return f"{name} on {date} spot {spot} is already booked by someone"
	elif RESERVATIONS.get(date) and rebook(spot,name,date):
		return f"{name}, you already booked"
	else:
		if RESERVATIONS.get(date) is None:
			RESERVATIONS[date]={}
		RESERVATIONS[date][spot]={}
		RESERVATIONS[date][spot]["name"]=name
		return f"Congrats! {name}, your reserved spot no. {spot} for {date.replace(':','/')}"

@app.route("/dev")
def dev():
	return RESERVATIONS

app.run("0.0.0.0",8080,debug=True)