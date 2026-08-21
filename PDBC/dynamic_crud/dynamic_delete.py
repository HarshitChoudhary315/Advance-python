import pymysql
def testDelete1():
    connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='advance_python')
    cursor = connection.cursor()
    sql = "delete from marksheet where id = 5"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("data deleted")
#testDelete1()

def testDelete2():
    connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='advance_python')
    cursor = connection.cursor()
    sql = "delete from marksheet where id = %s"
    data = (20)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("data deleted")
#testDelete2()

def testDelete3(id):
    connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='advance_python')
    cursor = connection.cursor()
    sql = "delete from marksheet where id = %s"
    data = (id)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("data deleted")
testDelete3(15)