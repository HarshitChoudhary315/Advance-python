import pymysql

def testinsert(data={}):
    customer_id = data['customer_id']
    customer_name = data['customer_name']
    email_id = data['email_id']
    phone_number = data['phone_number']
    address = data['address']
    connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='customer')
    cursor = connection.cursor()
    sql = "insert into customer values (%s,%s,%s,%s,%s)"
    data = (customer_id,customer_name,email_id,phone_number,address)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("inser data successfully")

testinsert({'customer_id':11,
            'customer_name':'arpit',
            'email_id':'arpit22@gmail.com',
            'phone_number':'9988773344',
            'address':'indore'})
