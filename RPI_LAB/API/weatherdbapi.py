import json
from flask import Flask, request

# Create a Flask app

app = Flask(__name__)

# Get the weather data from MySQL

import MySQLdb

# Connect to the database

db = MySQLdb.connect(host='localhost', user='root', passwd='password', db='weather')

# Create a cursor

cursor = db.cursor()

# Select all the data from the weather_data table

sql = """
SELECT * FROM weather_data
"""

cursor.execute(sql)

weather_data = cursor.fetchall()

# Close the connection

db.close()

# Define a route to get the weather data

@app.route('/weather', methods=['GET'])
def get_weather():

# Get the city from the request

city = request.args.get('city')

# If no city is specified, return the weather data for the current location

if city is None:

city = 'current_location'

# Get the weather data for the specified city

weather_data_for_city = [weather_data for weather_data in weather_data if weather_data[0] == city]

# Return the weather data as JSON

return json.dumps(weather_data_for_city)

# Run the Flask app

if __name__ == '__main__':

app.run(host='0.0.0.0')
