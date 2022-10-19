"""
main.py send_text gets weather info from the next 12 hours and sends a text to my number indicating 
if it will be cold (says to bring a coat) and if it will rain (says to bring an umbrella)
"""

import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

# Load env variables
load_dotenv()
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
api_key_weather = os.getenv("API_KEY_WEATHER")
twilio_from_number = os.getenv("MY_TWILIO_NUMBER")
my_number= os.getenv("MY_NUMBER")

client = Client(account_sid, auth_token)

# Location: Charlotte NC
parameters = {
    "lat": 35.227085,
    "lon": -80.843124,
    "units": "imperial",
    "appid": api_key_weather,
    "exclude": "current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
# Uncomment below to check error codes 
# print(response.status_code)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
is_cold = False

for hour_data in weather_slice:
    rain_condition_code = hour_data["weather"][0]["id"]
    temp_imperial = hour_data["temp"]

    if int(rain_condition_code) < 700:
        will_rain = True

    if temp_imperial < 50:
        is_cold = True

# Write message
if will_rain and is_cold:
    send_content = "Bring an umbrella and a coat!"
elif will_rain:
    send_content = "Bring an umbrella!"
elif is_cold:
    send_content = "Bring a coat!"
else:
    send_content = "Looks clear today!"


def send_text(content, client=client, from_=twilio_from_number, to_num=my_number):
    message = client.messages.create(
        body=content,
        from_=from_,
        to=to_num
    )

send_text(content=send_content)
print(send_content)
