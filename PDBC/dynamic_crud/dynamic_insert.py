import pymysql


def testInsert1():
  connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='advance_python')
  cursor = connection.cursor()
  sql = "insert into marksheet values(13,113,'abc',87,78,54)"
  cursor.execute(sql)
  connection.commit()
  connection.close()
  print("data insert successfully")
#testInsert1()

def testInsert2():
    connection =pymysql.connect(host='localhost',port=3306,user='root',password='root',database='advance_python')
    cursor = connection.cursor()
    sql = "insert into marksheet values(%s,%s,%s,%s,%s,%s)"
    data = (14,114,'xyz',35,53,64)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("data insert successfully")
#testInsert2()

def testInsert3(id,rollNo,name,maths,physics,chemistry):
    connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='advance_python')
    cursor= connection.cursor()
    sql = "insert into marksheet values(%s,%s,%s,%s,%s,%s)"
    data = (id,rollNo,name,maths,physics,chemistry)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("data insert successfully")

#testInsert3(15,115,'huijk',46,57,76)
def testInsert4(data={}):
    id = data['id']
    rollNo = data['rollNo']
    name = data['name']
    maths = data['maths']
    physics = data['physics']
    chemistry = data['chemistry']
    connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='advance_python')
    cursor = connection.cursor()
    sql = "insert into marksheet values(%s,%s,%s,%s,%s,%s)"
    data= (id,rollNo,name,maths,physics,chemistry)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("insert data successfully")

params = {}
params['id'] = 20
params['rollNo'] =210
params['name'] = 'harshit'
params['maths'] = 78
params['physics'] = 78
params['chemistry'] = 97
print(params)
testInsert4(params)