from django.db import models
import cx_Oracle
import os

LOCATION = r"C:\oraclexe\instantclient_19_11"
os.environ["PATH"]=LOCATION+";"+os.environ["PATH"]

# Create your models here.

def getConnection():
    try:
        conn=cx_Oracle.connect("hr/happy@localhost:1521/xe")
        #print(conn)
    except Exception as e:
        print(e)
    return conn

def category(no):
    conn=getConnection()
    #print(conn)
    cursor=conn.cursor()
    #print(cursor)
    start=0
    end=0
    if no==1 :
        start=1
        end=12
    elif no==2 :
        start=13
        end=18
    elif no==3:
        start=19
        end=30
    sql=f"""
            SELECT no,title,subject,poster
            FROM food_category
            WHERE no BETWEEN {start} AND {end}
            ORDER BY no ASC
          """
    cursor.execute(sql)
    cate_list=cursor.fetchall()
    print(cate_list)
    cursor.close()
    conn.close()
    return cate_list

def food_list(cno):
    pass

def food_detail(no):
    pass

'''
category(1)
category(2)
category(3)
'''