import paho.mqtt.client as mqtt
import mysql.connector

# MQTT broker settings
broker_address = "0.0.0.0"
broker_port = 1883
topic = "Sensor/TEMP"

# MySQL database settings
db_host = "0.0.0.0"
#db_port = "3306"
db_user = "pi"
db_password = "raspberry"
db_name = "IOTData"

# Connect to the MQTT broker
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code "+str(rc))
    client.subscribe(topic)

# Process incoming messages
def on_message(client, userdata, msg):
    print("Received message on topic "+msg.topic+" with payload "+msg.payload.decode())
    sensor_data = float(msg.payload.decode())

    # Connect to the MySQL database
    db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, database=db_name)
    cursor = db.cursor()

    # Insert sensor data into the database
    sql = "INSERT INTO `MQTTData` (MyData) VALUES (%d);"
    val = (sensor_data,)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "record inserted.")

    # Close the database connection
    cursor.close()
    db.close()

# Connect to the MQTT broker and start the main loop
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address, broker_port)
client.loop_forever()

