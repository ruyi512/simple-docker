import pymysql
import os

def test_mysql():
    connection = pymysql.connect(
        host='192.168.1.130',
        database='37ww',
        user='root',
        password='QyYLa7P6FAyzih3P'
    )
    cursor = connection.cursor()
    try:
        sql = 'select * from cq_user limit 10'
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
    except Exception as e:
        print(e)

    cursor.close()
    connection.close()