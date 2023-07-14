import requests
import json
import pandas as pd 
from datetime import datetime,date
import s3fs

def weather_etl():
    api_key='4e028344cc4b267e847c573f328e5d43'
    us_cities = [
    "New York",
    "Los Angeles",
    "Chicago",
    "Houston",
    "Phoenix",
    "Philadelphia",
    "San Antonio",
    "San Diego",
    "Dallas",
    "San Jose",
    "Austin",
    "Jacksonville",
    "San Francisco",
    "Indianapolis",
    "Columbus",
    "Fort Worth",
    "Charlotte",
    "Seattle",
    "Denver",
    "El Paso",
    "Detroit",
    "Washington",
    "Boston",
    "Memphis",
    "Nashville",
    "Portland",
    "Oklahoma City",
    "Las Vegas",
    "Baltimore",
    "Louisville",
    "Milwaukee",
    "Albuquerque",
    "Tucson",
    "Fresno",
    "Sacramento",
    "Kansas City",
    "Long Beach",
    "Mesa",
    "Atlanta",
    "Colorado Springs",
    "Virginia Beach",
    "Raleigh",
    "Omaha",
    "Miami",
    "Oakland",
    "Minneapolis",
    "Tulsa",
    "Wichita",
    "New Orleans",
    "Arlington",
    "Cleveland",
    "Tampa",
    "Bakersfield",
    "Aurora",
    "Honolulu",
    "Anaheim",
    "Santa Ana",
    "Riverside",
    "Corpus Christi",
    "Lexington",
    "Stockton",
    "St. Louis",
    "Saint Paul",
    "Henderson",
    "Pittsburgh",
    "Cincinnati",
    "Anchorage",
    "Greensboro",
    "Plano",
    "Newark",
    "Lincoln",
    "Orlando",
    "Irvine",
    "Toledo",
    "Jersey City",
    "Chula Vista",
    "Durham",
    "Fort Wayne",
    "St. Petersburg",
    "Laredo",
    "Buffalo",
    "Madison",
    "Lubbock",
    "Chandler",
    "Scottsdale",
    "Reno",
    "Glendale",
    "Gilbert",
    "Winston-Salem",
    "North Las Vegas",
    "Norfolk",
    "Chesapeake",
    "Garland",
    "Irving",
    "Hialeah",
    "Fremont",
    "Boise",
    "Richmond"
]

    weather_data = []

    for city in us_cities:
        base_url='http://api.openweathermap.org/data/2.5/weather'
        params={
            'q':city,
            'APPID':api_key
        }

        response = requests.get(base_url,params=params)
        full_weather_data = response.json()
        
        if full_weather_data['cod']==200:
            extracted_data={
            "name": full_weather_data["name"] ,  
            "country":full_weather_data["sys"]["country"] , 
            "temp":full_weather_data["main"]["temp"],
            "humidity":full_weather_data["main"]["humidity"],
            "feels_like":full_weather_data["main"]["feels_like"],
            "wind_speed":full_weather_data["wind"]["speed"],
            }
            
            weather_data.append(extracted_data)
        else:
            print("Unable to retrieve data")

        # today = datetime.today()
        # dt = today.strftime("%m%d%Y")
        # print(dt)
        df = pd.DataFrame(weather_data)
        df.to_csv(f's3://weather-bucket-jaswanth/weather_data.csv')
