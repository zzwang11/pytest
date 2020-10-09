import pymysql

db = pymysql.connect("localhost", "root", "123456", "runoob_db")

cursor = db.cursor()

sql = """INSERT INTO EMPLOYEE VALUES ('jack', 'ma', 50, 'M', 20000000)"""

cursor.execute(sql)
db.commit()
db.close()