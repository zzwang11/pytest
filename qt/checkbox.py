from PyQt5.QtSql import QSqlDatabase

db = QSqlDatabase.addDatabase('QSQLITE')
db.setDatabaseName('d:/sqlite/mydb.db')
db.open()

