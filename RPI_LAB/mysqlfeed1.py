import pymysql

# establish connection to remote MySQL database
connection = pymysql.connect(
    host='0.0.0.0',
    port=3306,
    user='pi',
    password='raspberry',
    db='IoTData'
)

# create a cursor to execute SQL commands
cursor = connection.cursor()

# execute a SQL command to insert data into a table
sql_command = ("INSERT INTO `MQTTData` (`ID`, `TimeStamp`, `Topic`, `MyData`) VALUES ('8', current_timestamp(), 'Sensor/TEMP', '38');")
#values = ("value1", "value2", "value3")
cursor.execute(sql_command, values)

# commit the changes to the database
connection.commit()

# close the cursor and connection
cursor.close()
connection.close()
