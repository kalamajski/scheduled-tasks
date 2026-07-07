import requests
from twilio.rest import Client
import os

# data for openweather
LATITUDE = 55.7
LONGITUDE = 13.2
COUNTS = 4
OW_API_KEY = os.environ.get("OW_API_KEY")

#data for Twilio
ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
print(OW_API_KEY)
print(AUTH_TOKEN)
weather_params = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": OW_API_KEY,
    "cnt" : COUNTS,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params = weather_params)
response.raise_for_status()
data = response.json()

will_it_rain = False
for item in data['list']:
    for weather in item['weather']:
        if weather['id'] < 700:
            will_it_rain = True

if will_it_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
      from_="whatsapp:+14155238886",
      body="It's going to rain today. Remember to bring an umbrella",
      to="whatsapp:+46763983827"
    )
    print(message.status)
