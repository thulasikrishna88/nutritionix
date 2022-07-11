import os
from dotenv import load_dotenv
import requests
import datetime as dt

load_dotenv()
NUTRITION_APPID=os.getenv("NUTRITION_APPID")
NUTRITION_APIKEY=os.getenv("NUTRITION_APIKEY")
EXCERCISE_ENDPOINT=os.getenv("EXCERCISE_ENDPOINT")
SHEETY_ENDPOINT=os.getenv("SHEETY_ENDPOINT")
SHEETY_TOKEN=os.getenv("SHEETY_TOKEN")

today=dt.datetime.now()
today_date=today.strftime("%d/%m/%Y")
today_time=today.strftime("%X")


exercise_params = {
    "query": f"{input('which exercise you did')}",
    "gender": "female",
    "weight_kg": 65,
    "height_cm": 158,
    "age": 34
}
exersise_headers={
    "x-app-id":NUTRITION_APPID,
    "x-app-key":NUTRITION_APIKEY
    }
# sheety_header={}

exercise_response = requests.post(url=EXCERCISE_ENDPOINT,json=exercise_params,headers=exersise_headers)
data_list = exercise_response.json()['exercises']
sheety_header={"Authorization": f"Bearer {SHEETY_TOKEN}"}

for data in data_list:
    sheety_params={
        "workout":{
            "date":today_date,
            "time":today_time,
            "exercise":f'{data["name"]}'.title(),
            "calories":f'{data["nf_calories"]}',
            "duration":f'{data["duration_min"]}'
        }
    }
    sheety_response = requests.post(url=SHEETY_ENDPOINT,json=sheety_params,headers=sheety_header)

