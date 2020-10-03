import os
import datetime
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
        # Insert single row with "row" and cursor.execute() method
        row = ("bob", 21, "1990-02-06 23:04:56")
        cursor.execute("INSERT INTO Friends VALUES (%s,%s,%s);", row)
        connection.commit()

finally:
    # Close the connection, regardless of whether
    # or not the above was successful
    connection.close()
