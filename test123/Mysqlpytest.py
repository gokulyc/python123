import pymysql

db = pymysql.connect("localhost", "root", "", "test")

cursor = db.cursor()

sql = """select * from
        testtb"""

try:
    cursor.execute(sql)

    results = cursor.fetchall()
    num = cursor.rownumber
    print(num)

    for row in results:
        print(row[0], "||", row[1], "||", row[2])


except:
    print("unknown error")

db.close()
