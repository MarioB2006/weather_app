import requests
from pathlib import Path
from datetime import date,timedelta
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
         
style.use("dark_background")
path_directory = Path(__file__).resolve().parent
API_Key = (path_directory / "API_key.txt").read_text(encoding="utf-8")
base_url="https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
local_date=date.today()

def get_city(name_city:str,abreviation_country:str)->str:
    url=f"{base_url}{name_city},{abreviation_country}/"
    return url

def get_data_7days()->dict:
    seven_days_ahead=local_date+timedelta(7) 
    city_name,country_name=ask_user ()
    complete_url=f"{get_city(city_name,country_name)}{local_date}/{seven_days_ahead}?key={API_Key}"
    response=requests.get(complete_url) 
    data=response.json()
    return data

def get_important_data(all_data:dict,days_amount:int)->list[list[dict]]:
    all_important_data=[]
    days:list=[]
    temps:list=[]
    celsius=lambda fahrenheit:round((fahrenheit-32)*5/9)
    for i in range(days_amount+1):
        important_data={
            "day":all_data["days"][i]["datetime"],
            "temperature in °C":celsius(all_data["days"][i]["temp"]),
            "humidity in %":all_data["days"][i]["humidity"],
            "desciption":all_data["days"][i]["description"]
        }   
        day={
            "day":all_data["days"][i]["datetime"]
        }
        temp={
            "temperature in °C":celsius(all_data["days"][i]["temp"])
        }
        all_important_data.append(important_data)
        days.append(day)
        temps.append(temp)

    return all_important_data,days,temps
    
def weather_forecast(data:dict)->None:
    for items in data:
        for key,value in items.items():
            print(f"{key}: {value}")
        print(f"\n")

def ask_user()->tuple[str, str]:
    print("Welcome to this text-based weather forecast app")
    print("Please type in the name of the city, the country.")
    city:str=input("city name: \n")
    country:str=input("country name: \n")
    return city,country

def main():
    all_important, days,temps = get_important_data(get_data_7days(), 7)
    weather_forecast(all_important)
    day=np.array([list(d.values()) for d in days]).flatten()
    temp=np.array([list(d.values()) for d in temps]).flatten()
    plt.xlabel("Date")
    plt.ylabel("temperature")
    plt.title("weather forecast",fontsize="25", fontname="Comic Sans MS")
    plt.plot(day,temp,color="red",lw="3")
    plt.show()

if __name__=="__main__":
    main()