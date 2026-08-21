import pymysql

connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='advance_python')
cursor = connection.cursor()
sql = "insert into marksheet values(12,112,'abc',76,35,76)"
cursor.execute(sql)
connection.commit()
connection.close()
print("data insert data successfully")