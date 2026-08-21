import pymysql

connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='advance_python')
cursor = connection.cursor()
sql = "update marksheet set maths = 78 where id =1 "
cursor.execute(sql)
connection.commit()
connection.close()
print("data update successfully")
