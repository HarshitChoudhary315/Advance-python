import pymysql




class collegeModel:
    def nextpk(self):
        pk = 0
        connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='demo')

        cursor = connection.cursor()
        sql = "select max(id) from college"
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.commit()
        connection.close()
        return pk + 1


    def add(self,data):
        id = collegeModel.nextpk(self)
        name = data['name']
        address = data['address']
        state = data['state']
        city = data['city']
        phoneNo = data['phoneNo']
        connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='demo')
        cursor = connection.cursor()
        sql = "insert into college values(%s,%s,%s,%s,%s,%s)"
        data = (id,name,address,state,city,phoneNo)
        cursor.execute(sql,data)
        connection.commit()
        connection.close()
        print("data inserted")


    def update(self,data):
        id = data['id']
        name = data['name']
        address = data['address']
        state = data['state']
        city = data['city']
        phoneNo = data['phoneNo']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='demo')
        cursor = connection.cursor()
        sql = "update collage set name = %s,address= %s,state =%s,city =%s,phoneNo =%s where id = %s"
        data = (name,address,state,city,phoneNo,id)
        cursor.execute(sql,data)
        connection.commit()
        connection.close()
        print("data updated")

    def delete(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='demo')
        cursor = connection.cursor()
        sql = "delete from college where id = %s"
        data = (id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data deleted successfully')


    def read(self, data):

      id = data.get('id', 0)
      name = data.get('name', '')
      address = data.get('address', '')
      state = data.get('state', '')
      city = data.get('city', '')
      phoneNo = data.get('phoneNo', '')
      pageNo = data.get('pageNo', 1)
      pageSize = data.get('pageSize', 0)

      connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='demo')
      cursor = connection.cursor()
      sql = "select * from college where 1=1"
      if id != 0:
        sql += " and id = " + str(id)
      if name != '':
        sql += " and name like '" + name + "%'"

      if address != '':
        sql += " and address like '" + address + "%'"

      if state != '':
        sql += " and state like '" + state + "%'"

      if city != '':
        sql += " and city like '" + city + "%'"

      if phoneNo != '':
        sql += " and phoneNo like '" + phoneNo + "%'"

      if pageSize > 0:
        offset = (pageNo - 1) * pageSize
        sql += " limit " + str(offset) + "," + str(pageSize)

      print("sql =>", sql)

      cursor.execute(sql)

      result = cursor.fetchall()

      for row in result:
        print(
            row[0], '\t',
            row[1], '\t',
            row[2], '\t',
            row[3], '\t',
            row[4], '\t',
            row[5]
        )

      connection.close()
