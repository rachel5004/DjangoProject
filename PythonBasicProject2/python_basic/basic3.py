# 데이터베이스 연결 
import cx_Oracle
#1. 오라클 연결 
conn=cx_Oracle.connect("hr/happy@localhost:1521/XE")
#2. cursor생성 => PreparedStatement
cursor=conn.cursor()
#3. SQL문장 제작 
sql="SELECT no,name,subject,regdate,content,hit FROM freeboard ORDER BY no"
cursor.execute(sql)
#4. 결과값 받기 
# (7499, 'ALLEN', 'SALESMAN', 7698, datetime.datetime(1981, 2, 11, 0, 0), 1600.0, 300.0, 30) 
# Tuple
for row in cursor:
    #print(row)
    for i in range(len(row)):
        print(row[i],end=" ")
    print('')
        
