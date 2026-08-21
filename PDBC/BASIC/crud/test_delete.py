import pymysql

connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='advance_python')
cursor = connection.cursor()
sql = "delete from marksheet where id = 12"
cursor.execute(sql)

connection.commit()
connection.close()
print("data deleted")