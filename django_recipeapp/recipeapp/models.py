from django.db import models
import cx_Oracle
import os

LOCATION = r"C:\oraclexe\instantclient_19_11"
os.environ["PATH"]=LOCATION+";"+os.environ["PATH"]

def getConnection():
    try:
        conn=cx_Oracle.connect("hr/happy@localhost:1521/xe")
    except Exception as e:
        print(e)
    return conn

def recipeListData(page):
    rowSize=12
    start=(rowSize*page)-(rowSize-1)
    end=(rowSize*page)
    #연결
    conn=getConnection()
    cursor=conn.cursor()
    sql=f"""
            SELECT no,title,poster,chef,num 
            FROM (SELECT no,title,poster,chef,rownum as num 
            FROM (SELECT /*+ INDEX_ASC(recipe recipe_no_pk) */ no,title,poster,chef
            FROM recipe))
            WHERE num BETWEEN {start} AND {end}
          """
    cursor.execute(sql)
    list=cursor.fetchall()
    print(list)
    cursor.close()
    conn.close()
    return list

def recipeDetailData(rno):
    conn=getConnection()
    cursor=conn.cursor()
    sql=f"""
            SELECT no,poster,chef,chef_poster,title,content,info1,info2,info3,chef_info
            FROM recipe_make
            WHERE rno={rno}
          """
    cursor.execute(sql)

    detail=cursor.fetchone()

    cursor.close()
    conn.close()
    return detail

def recipeTotalPage():
    conn=getConnection()
    cursor=conn.cursor()
    sql="SELECT CEIL(COUNT(*)/12.0) FROM recipe"

    cursor.execute(sql)
    total=cursor.fetchone()
    print("totalPage:"+str(total[0]))
    # cursor,conn닫기
    cursor.close()
    conn.close()
    return total[0]

#recipeTotalPage()
#recipeListData(1)