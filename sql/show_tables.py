
import pymysql
 
mydb = pymysql.connect(
  host="localhost",
  user="root",
  passwd="123456",
  database="runoob_db"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW tables")

for x in mycursor:
  print(x)

mydb.close()