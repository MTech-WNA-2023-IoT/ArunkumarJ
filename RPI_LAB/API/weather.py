import json
from urllib.request import urlopen
#Create user account and obtain API key from https://www.weatherapi.com

url = "https://api.weatherapi.com/v1/current.json?key=ff20c525398c4d97ae640555232905&q=kollam&aqi=no"

api_page = urlopen(url)
api=api_page.read()
json_api=json.loads(api)

print("Raw Data")
print(json_api)

print("Parsed Data")
data=json_api['current']['temp_c']
print(data)
