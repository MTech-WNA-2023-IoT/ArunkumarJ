import json
from urllib.request import urlopen

# Create user account and obtain API key from https://www.weatherapi.com

url = "https://api.weatherapi.com/v1/current.json?key=ff20c525398c4d97ae640555232905&q=kollam&aqi=no"

api_page = urlopen(url)
api = api_page.read()
json_api = json.loads(api)

# Save the data to MySQL

import MySQLdb

# Connect to the database

db = MySQLdb.connect(host='localhost', user='root', passwd='password', db='weather')

# Create a cursor

cursor = db.cursor()

# Insert the data into the table

sql = """
INSERT INTO weather_data (timestamp, temperature, humidity, wind_speed, wind_direction, pressure, cloudiness, precipitation)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

cursor.execute(sql, (json_api['timestamp'], json_api['temperature'], json_api['humidity'], json_api['wind_speed'], json_api['wind_direction'], json_api['pressure'], json_api['cloudiness'], json_api['precipitation']))

# Commit the changes

db.commit()

# Close the connection

db.close()
