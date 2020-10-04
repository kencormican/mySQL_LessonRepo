import os
import pymysql

# Get username from Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')
try:
    # Run a query
    with connection.cursor() as cursor:
        # Updating data using the cursor.execute() method
        cursor.execute("UPDATE Friends SET age = 22 WHERE name = 'bob';")
        connection.commit()

finally:
    # Close the connection, regardless of whether
    # or not the above was successful
    connection.close()
