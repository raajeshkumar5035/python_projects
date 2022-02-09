import mysql.connector
# 'mydb = mysql.connector.connect(host='18.217.17.102', user='root', password='MysqlRoot1')'
mydb = mysql.connector.connect(host='18.217.17.102', user='python_user', password='Python_user1', database='python_db')
my_cursor = mydb.cursor()
my_cursor.execute("show databases")
for i in my_cursor:
    print(i)
