import paho.mqtt.client as mqtt
import mysql.connector

# MQTT broker settings
broker_address = "34.93.203.151"
broker_port = 1883
topic = "Sensor/TEMP"

# MySQL database settings
db_host = "0.0.0.0"
db_user = "pi"
db_password = "raspberry"
db_name = "IoTData"

# Define callback function for MQTT client to process incoming messages
def on_message(client, userdata, message):
    # Convert message payload to float
    sensor_data = float(message.payload.decode())

    # Connect to MySQL database
    db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, database=db_name)
    cursor = db.cursor()

    # Insert sensor data into MySQL database
    sql = "INSERT INTO MQTTData (value) VALUES (%s)"
    val = (sensor_data,)
    cursor.execute(sql, val)
    db.commit()

    # Close database connection
    cursor.close()
    db.close()

# Create MQTT client and connect to broker
client = mqtt.Client()
client.connect(broker_address, broker_port)

# Subscribe to MQTT topic
client.subscribe(topic)

# Set MQTT client callback function for incoming messages
client.on_message = on_message

# Start MQTT client loop to receive incoming messages
client.loop_forever()
