#오라클 (sqlite)
import cx_Oracle
# 1. 연결 
conn=cx_Oracle.connect("hr/happy@localhost:1521/XE")
# 2. 전송하고 데이터를 받는 객체 
cursor=conn.cursor()
item=[
  ('홍길자2',90,80,70),
  ('을지문덕2',80,80,67),
  ('이순신2',90,90,90),
  ('김두한2',80,80,70),
  ('춘향이2',70,78,90)
]
# 1. 갯수를 확인 
cursor.arraysize=len(item)
sql="INSERT INTO python_student VALUES(ps_no_seq.nextval,:1,:2,:3,:4)"
cursor.executemany(sql,item)
print("전체 데이터 첨부 완료")
conn.commit()
cursor.close()
conn.close()