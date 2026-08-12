import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='rays')
cursor = connection.cursor()
sql = "INSERT INTO EMPLOYEE VALUES (11, 'Kabir', 'Indore', 101)"
cursor.execute(sql)
connection.commit()
print("Record inserted successfully")