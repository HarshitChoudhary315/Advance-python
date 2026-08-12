import pymysql
connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='advancepython')
connection.autocommit(True)
cursor = connection.cursor()
sql1 = "insert into students values(1,101,'Harshit',75,73,78)"
sql2 = "insert into students values(2,102,'Arpit',67,74,73)"
sql3 = "insert into students values(3,103,'Hariom',78,87,76)"

cursor.execute(sql1)
cursor.execute(sql2)
cursor.execute(sql3)
connection.close()
print("Data Get Succcessfully")