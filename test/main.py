
#!/usr/bin/python3

import pymysql

# Open database connection
db = pymysql.connect( host="sql111.epizy.com", user="epiz_31243903",password="kJw99Rs8rsmKZA",database="epiz_31243903_w654", port=3306 )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)

# disconnect from server
db.close()