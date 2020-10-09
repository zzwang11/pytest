import pymysql
 
mydb = pymysql.connect("localhost", "root", "123456", "runoob_db")
 
mycursor = mydb.cursor()
try:
    mycursor.execute("select * from employee")
    for x in mycursor:
        print(x)
except:
    mydb.rollback()

mydb.close()