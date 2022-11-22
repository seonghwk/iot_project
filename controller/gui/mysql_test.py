import mysql.connector

db = mysql.connector.connect(host='52.78.179.144', user='seonghwk', password='1234', database='minDB', auth_plugin='mysql_native_password')
cur = db.cursor()

#query
cur.execute("select * from command")

#print
for (id, time, cmd_string, arg_string, is_finish) in cur:
    print(id, time, cmd_string, arg_string, is_finish)

cur.close()
db.close()