from flask import Flask,request
import json 

app = Flask(__name__)

BAYS=4
RESERVATIONS={}

def check_rebooking(name,date):
	for i in BAYS:
		if RESERVATIONS[date][i]["name"]==name:
			return False
	return True

def check_bays(spot,name,date):
	if spot > BAYS:
		return f"{name}, this spot {spot} doesn't exist"
	elif date[2] != ":" and date[5] != ":" :
		return "Invalid Date Format. Format Should be DD:MM:YYYY"
	elif RESERVATIONS.get(date) and RESERVATIONS[date][spot]:
		return f"{name} on {date} spot {spot} is already booked"
	elif RESERVATIONS.get(date) and (lambda name,data: any(RESERVATIONS[date][i]["name"]==name for i in BAYS)):
		return f"{name}, you already booked"
	else:
		if RESERVATIONS.get(date) is None:
			RESERVATIONS[date]={}
		RESERVATIONS[date][spot]={}
		RESERVATIONS[date][spot]["name"]=name
		return f"Congrats! {name}, your reserved spot no. {spot} for {date.replace(':','/')}"
	print(RESERVATIONS) #DEBUG

@app.route("/book/<int:spot>/<name>/<date>",methods=['POST'])
def book(spot,name,date): #date -> DD:MM:YYYY
	return check_bays(spot,name,date)

app.run("0.0.0.0",8080)