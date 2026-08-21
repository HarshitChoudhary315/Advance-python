import pymysql




def testUpdate1():
 connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='advance_python')
 cursor = connection.cursor()
 sql = "update marksheet set name = 'aaa' where id = 13"
 cursor.execute(sql)
 connection.commit()
 connection.close()
 print("data updated successfully")

#testUpdate1()

def testUpdate2():
    connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='advance_python')
    cursor = connection.cursor()
    sql = "update marksheet set maths = %s,rollNo= %s,name =%s,physics = %s,chemistry =%s where id = %s"
    data = (55,105,'Harsh',85,94,5)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("data update successfully")
#testUpdate2()

def testUpdate3(rollNo,name,maths,physics,chemistry,id):
    connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='advance_python')
    cursor = connection.cursor()
    sql = "update marksheet set rollNo= %s,name = %s,maths= %s,physics = %s,chemistry= %s where id = %s "
    data = (rollNo,name,maths,physics,chemistry,id)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("update successfully")
#testUpdate3(104,'arpit',87,89,90,4)

def testUpdate4(data):
    id = data['id']
    rollNo = data['rollNo']
    name = data['name']
    maths = data['maths']
    physics = data['physics']
    chemistry = data['chemistry']
    connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='advance_python')
    cursor = connection.cursor()
    sql = "update marksheet set rollNo = %s,name = %s,maths= %s,physics=%s,chemistry=%s where id = %s"
    data = (rollNo,name,maths,physics,chemistry,id)
    cursor.execute(sql,data)
    connection.commit()
    connection.commit()
    connection.close()
    print("data updated")

params = {}
params['id'] = 3
params['rollNo'] = 103
params['name'] = 'harshit'
params['maths'] = 100
params['physics'] = 100
params['chemistry'] = 100
testUpdate4(params)