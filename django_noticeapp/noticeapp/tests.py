from django.test import TestCase
import MySQLdb
import cx_Oracle
import os

LOCATION = r"C:\oraclexe\instantclient_19_11"
os.environ["PATH"]=LOCATION+";"+os.environ["PATH"]

# Create your tests here.
config={
    'host':'127.0.0.1',
    'user':'root',
    'password':'1234',
    'database':'sist',
    'port':3300,
    'charset':'utf8',
    'use_unicode':True
}
'''
try:
    conn=MySQLdb.connect(**config)
    cursor=conn.cursor()
    sql="SELECT * FROM noticeapp_noticeapp"
    cursor.execute(sql)
    data=cursor.fetchall()
    for row in data:
        print(row)
    cursor.close()
    conn.close()
except Exception as e:
    print(e)
'''

def foodCategory():
    conn=cx_Oracle.connect('hr/happy@localhost:1521/xe')
    cursor=conn.cursor()
    sql="SELECT no,title,subject,poster FROM food_category ORDER BY no"
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        insert(row)
    cursor.close()
    conn.close()
    return data

def insert(row):
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        sql = f"INSERT INTO food_category VALUES(%d,'%s','%s','%s')"%(row[0],row[1],row[2],row[3])
        cursor.execute(sql)
        print("insert!")
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)

foodCategory()