import paho.mqtt.client as paho
import pymysql
#pip3 install paho-mqtt
global mqttclient;
global broker;
global port;


broker = "0.0.0.0";
port = 1883;

client_uniq = "pubclient_123"

mqttclient = paho.Client(client_uniq, True) 

def test(client, userdata, message):
  print("client:"+ str(client))
  print("userdata:"+ userdata)
  print("message:"+ message.payload)

def _on_message(client, userdata, msg):
# 	print("Received: Topic: %s Body: %s", msg.topic, msg.payload)
	print(msg.topic+" "+str(msg.payload))

#Create a connection to MySQL Database 
# conn =pymysql.connect(database="databasename",user="user",password="password",host="localhost")
conn =pymysql.connect(database="IOTData",user="pi",password="raspberry",host="localhost")
#Create a MySQL Cursor to that executes the SQLs
cur=conn.cursor()
#Create a dictonary containing the fields, name, age and place
# data={'name':'hello','age':10,'place':'kollam'}
# data={`ID`:'7','TimeStamp':current_timestamp(),'Topic':'Sensor/TEMP','Data':'40'}
#Execute the SQL to write data to the database
cur.execute("INSERT INTO `MQTTData` (`ID`, `TimeStamp`, `Topic`, `MyData`) VALUES ('9', current_timestamp(), 'Sensor/TEMP', '36');")
#Close the cursor
cur.close()
#Commit the data to the database
conn.commit()
#Close the connection to the database
conn.close()

#Open phpMyAdmin and see how the data is stored to the database
	 
#Subscribed Topics 
def _on_connect(mqttclient, userdata, flags, rc):
# 	print("New Client: "+str(mqttclient)+ " connected")
# 	print(rc)
	mqttclient.subscribe("Sensor/TEMP", qos=0)	
  
mqttclient.message_callback_add("Sensor/TEMP", test)

mqttclient.connect(broker, port, keepalive=1, bind_address="")
  
mqttclient.on_connect = _on_connect

mqttclient.loop_forever()
