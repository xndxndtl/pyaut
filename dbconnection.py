import pymssql


# Open database connection
db = MySQLdb.connect("10.208.199.142", "pms", "211@dmin01", "view1")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to select the database.
sql = "SELECT * FROM board_basic"


try:
    cursor.execute(sql)
results = cursor.fetchall()
for row in results:
    value1 = row[1]
    value2 = row[2]
    value3 = row[3]
    print
    "name: " + value1, "password: " + value2, "email: " + value3

except:
print
"Error: unable to fecth data"





# disconnect from server
db.close()
