import requests
from datetime import datetime
import os
GENDER = "male"
WEIGHT_IN_KG =60
HEIGHT_IN_CM= 175
AGE= 17

API_KEY ="c4a15d32dca87dd91ad1591c85dac250"
APP_ID ="db70cb92"
api_endpoint= "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/5d5da77f21a37c34e9c61491334073e4/newProject/workouts"


exercise_input = input("What was the exercise you did? ")

headers ={
    "x-app-id":APP_ID,
    "x-app-key":API_KEY
}


parameters ={
    "query": exercise_input,
    "gender":GENDER,
    "weight_kg":WEIGHT_IN_KG,
    "height_cm":HEIGHT_IN_CM,
    "age":AGE
}

response = requests.post(url=api_endpoint,json = parameters,headers = headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    headers = {"Authorization": "Bearer secrettoken@@@123"}

    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs,headers=headers)

    print(sheet_response.text)
