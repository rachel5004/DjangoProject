from django.db import models
# DAO
import cx_Oracle
import os

LOCATION = r"C:\oraclexe\instantclient_19_11"
os.environ["PATH"]=LOCATION+";"+os.environ["PATH"]
# Create your models here.
def getConnection():
    try:
        conn=cx_Oracle.connect("hr/happy@localhost:1521/xe")
    except Exception as e:
        print(e)
    return conn

# home
def movieListData(page):
    #cursor 생성
    conn=getConnection()
    cursor=conn.cursor()
    rowSize=12
    start=(rowSize*int(page))-(rowSize-1)
    end=rowSize*int(page)
    sql=f"""
            SELECT mno,title,poster,num 
            FROM (SELECT mno,title,poster,rownum as num
            FROM (SELECT /*+ INDEX_ASC(daum_movie dm_mno_pk) */ mno,title,poster
            FROM daum_movie))
            WHERE num BETWEEN {start} AND {end}
          """
    cursor.execute(sql)
    movie_list=cursor.fetchall()
    #print(movie_list)
    cursor.close() #cursor = PreparedStatement (sql문장을 전송후 데이터 받기)
    # fetchall(selectList) fetchone(selectOne)
    conn.close()
    return movie_list

def movieDetailData(mno):
    conn=getConnection()
    cursor=conn.cursor()
    sql=f"""
            SELECT mno,title,poster,genre,grade FROM daum_movie
            WHERE mno={mno}
          """
    cursor.execute(sql)
    movie_detail=cursor.fetchone()
    print(movie_detail)
    cursor.close()
    conn.close()
    return movie_detail







