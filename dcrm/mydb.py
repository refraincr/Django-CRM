# pip install mysql-connector
# pip install mysql-connector-python


import mysql.connector

# 创建连接
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
)

# 创建游标对象
cursorObject = dataBase.cursor()

# 执行sql语句
cursorObject.execute('CREATE DATABASE IF NOT EXISTS dcrmdb')

print('All done!')