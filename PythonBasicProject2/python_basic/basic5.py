# insert(데이터 추가)
import cx_Oracle
# 1. 오라클 연결
conn=cx_Oracle.connect("hr/happy@localhost:1521/xe")
cursor=conn.cursor() # PreparedStatement ps=conn.preparedStatement()
name=input("이름 입력:")
kor=int(input("국어 점수 입력:"))
eng=int(input("영어 점수 입력:"))
math=int(input("수학 점수 입력:"))
# 2. SQL문장 
sql="""
       INSERT INTO python_student VALUES(
         ps_no_seq.nextval,:1,:2,:3,:4
       )
     """
#  튜플형태로 묶어서 한번에 처리 ()=> 튜플
data=(name,kor,eng,math)
# 3. 오라클로 전송 
cursor.execute(sql,data)
# 4. comm을 전송 
conn.commit()
print("데이터베이스 저장 완료") 
# 5. conn닫기
cursor.close()
# 5-1 출력 
cursor=conn.cursor()
sql="""
      SELECT hakbun,name,kor,eng,math,(kor+eng+math),ROUND((kor+eng+math)/3.0,2),
      RANK() OVER(ORDER BY  (kor+eng+math) DESC)
      FROM python_student
    """
cursor.execute(sql)
for row in cursor:
    print(row)
conn.close()










