import pymysql

def testRead1():
    connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='advance_python')
    cursor = connection.cursor()
    sql = "select * from marksheet "
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0],'\t',data[1],'\t',data[2],'\t',data[3],'\t',data[4],'\t',data[5])
    connection.commit()
    connection.close()
# testRead1()

def testRead2():
    connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='advance_python')
    cursor =connection.cursor()
    sql = "select * from marksheet"
    cursor.execute(sql)
    result = cursor.fetchall()
    columnName = ('id','rollNo','name','maths','physics','chemistry')
    for x in result:
        print({columnName[i]: x[i] for i, _ in enumerate(x)})
    connection.commit()
    connection.close()
#testRead2()

def testRead3():
    connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='advance_python')
    cursor = connection.cursor()
    #sql = "select * from marksheet"
    #sql = "select * from marksheet where id =1"
    #sql = "select * from marksheet where name like  '%a'"
    sql = "select * from marksheet where maths = 55"
    print('sql =>',sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0],'\t',data[1],'\t',data[2],'\t',data[3],'\t',data[4],'\t',data[5])
    connection.commit()
    connection.close()
#testRead3()

def testRead4(id,rollNo,name,maths,physics,chemistry):
    connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='advance_python')
    cursor = connection.cursor()
    sql = "select * from marksheet"
    if id !=0:
        sql+= " where id = "+ str(id)
    if rollNo !=0:
        sql+= " where rollNo = "+ str(rollNo)
    if name !='':
        sql+= " where name like'"+ name+"%'"
    if maths !=0:
        sql+= " where maths ="+ str(maths)
    if physics !=0:
        sql+= " where physics ="+ str(physics)
    if chemistry !=0:
        sql+= " where chemistry="+ str(chemistry)
    print('sql =>',sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result :
        print(data[0],'\t',data[1],'\t',data[2],'\t',data[3],'\t',data[4],data[5])
    connection.commit()
    connection.close()
#testRead4(1,0,'',0,0,0)

def testRead5(param={}):
    id =param.get('id',0)
    rollNo = param.get('rollNo',0)
    name = param.get('name','')
    maths = param.get('maths',0)
    physics = param.get('physics',0)
    chemistry = param.get('chemistry',0)

    connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='advance_python')
    cursor = connection.cursor()
    sql = "select * from marksheet where 1=1"
    if id != 0:
        sql += " and id = " + str(id)
    if rollNo != 0:
        sql += " and rollNo = " + str(rollNo)
    if name != '':
        sql += " and name like '"+name+ "%'"
    if maths != 0:
        sql += "and maths = " +str(maths)
    if physics != 0:
        sql += "and physics = " +str(physics)
    if chemistry != 0:
        sql += " and chemistry = " +str(chemistry)

    print('sql=>',sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0],'\t',data[1],'\t',data[2],'\t',data[3],'\t',data[4],'\t',data[5])
    connection.commit()
    connection.close()
# param={}
#
# param['name'] = 'h'
# param['maths'] = 78

#testRead5(param)

def testRead6(param={}):
    id = param.get('id',0)
    rollNo = param.get('rollNo',0)
    name = param.get('name','')
    maths = param.get('maths',0)
    physics = param.get('physics',0)
    chemistry = param.get('chemistry',0)
    pageNo = param.get('pageNo',0)
    pageSize = param.get('pageSize',0)

    connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='advance_python')
    cursor = connection.cursor()
    sql = "select * from marksheet where 1=1 "
    if id != 0:
        sql += " and id" + str(id)
    if rollNo != 0 :
        sql += " and rollNo" + str(rollNo)
    if name != '':
        sql += " and name like '" + name + "%'"
    if maths != 0:
        sql += " and maths " + str(maths)
    if physics != 0:
        sql += " and physics " + str(physics)
    if chemistry != 0:
        sql += " and chemistry " +str(chemistry)
    if pageSize > 0:
        pageNo = (pageNo-1)*pageSize

    print('sql =>',sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0],'\t',data[1],'\t',data[2],'\t',data[3],'\t',data[4],'\t',data[5])
    connection.commit()
    connection.close()
param = {}
param['name'] = 'h'
#param['rollNo'] = 101

param['pageNo'] = 1
param['pageSize'] = 5

testRead6(param)