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
        # Update multiple rows with "rows" and cursor.executemany()
        # method and string interpolation
        rows = [(23, 'bob'),
                (24, 'jim'),
                (25, 'fred')]
        cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;",
                           rows)
        connection.commit()

finally:
    # Close the connection, regardless of whether
    # or not the above was successful
    connection.close()
