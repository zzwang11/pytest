import mysql.connector

mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 passwd="123456",
 database="runoob_db"
)

mycursor = mydb.cursor()

mycursor.execute("drop table sit")