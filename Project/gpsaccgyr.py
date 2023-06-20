import paho.mqtt.client as mqtt
import json

# MQTT broker settings
broker_address = "0.0.0.0"
broker_port = 1883
mqtt_topic = "gpsaccgyr"

# File to save received data
data_file = "received_data.json"

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    client.subscribe(mqtt_topic)

def on_message(client, userdata, msg):
    try:
        # Decode the received message payload
        data = msg.payload.decode("utf-8")
       
        # Parse the JSON data
        json_data = json.loads(data)
       
        # Save the received data to a file
        with open(data_file, "a") as file:
            file.write(json.dumps(json_data) + "\n")
       
        print("Data saved to file: ", json_data)
    except Exception as e:
        print("Error: ", str(e))

# Create an MQTT client
client = mqtt.Client()

# Set up the MQTT client callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker_address, broker_port, 60)

# Start the MQTT client loop
client.loop_forever()
