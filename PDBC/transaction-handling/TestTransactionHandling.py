import pymysql

connection = pymysql.Connect(host='localhost',port=3306,user='root',password='root',database='advancepython')
try:
    connection.autocommit(False)
    cursor = connection.cursor()
    sql1 = "insert into students values(4,104,'Harsh',78,76,75)"
    sql2 = "insert into students values(5,105,'raj',76,67,69)"
    sql3 = "insert into students values(5,106,'ankit',98,34,45,)"

    cursor.execute(sql1)
    cursor.execute(sql2)
    cursor.execute(sql3)
    connection.commit()
    print("Transaction comitted successfully")
except Exception as e :
    connection.rollback()
    print("Transaction rollback to due to error:",e)