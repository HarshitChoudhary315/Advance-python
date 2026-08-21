import pymysql
from RoleBean import *
class RoleModel:
     def nextPK(self):
         PK = 0
         connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='rays')
         cursor = connection.cursor()
         sql = "select max(id) from Role"
         cursor.execute(sql)
         result = cursor.fetchone()
         if result[0] is not None:
             pk = result[0]
         connection.commit()
         connection.close()
         return PK + 1

     def add(self,bean:RoleBean):
         id = RoleModel.nextPK(self)
         name = bean.get_name()
         description = bean.get_description()
         connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='rays')
         cursor = connection.cursor()
         sql = "insert into role values(%s,%s,%s)"
         data = (id,name,description)
         cursor.execute(sql,data)
         connection.commit()
         connection.close()
         print("data insert successfully")
