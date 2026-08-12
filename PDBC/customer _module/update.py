import pymysql

connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='rays')
cursor = connection.cursor()
sql = "update employee set name = 'Harshit' where id = 1"
cursor.execute(sql)
connection.commit()
print("record update successfully")