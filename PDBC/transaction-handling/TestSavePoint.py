import pymysql

connection = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='root',
    database='advancepython',
    autocommit=False
)

cursor = connection.cursor()

try:
    print("starting transaction.....")

    cursor.execute(
        "insert into students values(4,104,'Harsh',78,76,75)"
    )

    print("creating savepoint sp1...")
    cursor.execute("savepoint sp1")

    try:
        cursor.execute(
            "insert into students values(5,105,'Arsh',78,76,75)"
        )

        print("creating savepoint sp2...")
        cursor.execute("savepoint sp2")

    except Exception as e:
        print("Error in second insert, rolling back to savepoint sp1...")
        cursor.execute("rollback to savepoint sp1")

        try:
            cursor.execute(
                "insert into students values(6,106,'Harsh',78,76,75)"
            )

            print("second insert successful.")
            print("creating savepoint sp3...")
            cursor.execute("savepoint sp3")

        except Exception as e:
            print("Error in third insert, rolling back to savepoint sp1...")
            cursor.execute("rollback to savepoint sp1")

    connection.commit()
    print("Transaction committed successfully.")

except Exception as e:
    print("Error in transaction:", e)
    connection.rollback()

finally:
    cursor.close()
    connection.close()