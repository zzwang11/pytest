import pymysql

db = pymysql.connect("localhost", "root", "123456", "runoob_db")

cursor = db.cursor()

sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)

db.close()