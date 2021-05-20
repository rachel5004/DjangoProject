'''
    DB정리 
    1. function
       def 함수명(매개변수...):
           처리 
           #결과값이 있는 경우
           return 값 
    2. class => 자바와 비슷하다 
       class 클래명:
         생성자 
         멤버함수 
         멤버변수 
    DB 연습 
      = sqlite
      = oracle 
      ===========================
         id     name    sex       =====> Attribute
      ===========================
        aaa    홍길동    남자        ===== Tuple
      ===========================
        bbb    심청이    여자
      ===========================
      SELECT 
      
        => 조건 
        empno=7788
        => param=(7788,)  => () 튜플 , 프로그램 (record) , row
           execute("SELECT * FROM emp WHERE empno=?",param)
           param=7788
           execute("SELECT * FROM emp WHERE empno=%d" %param)  
           execute("SELECT * FROM emp WHERE empno=:empno",{"empno":7788})
           두개 이상 
           execute("SELECT * FROM emp WHERE empno IN('%d','%d')" %(7788,7794)
           execute("SELECT * FROM emp WHERE ename=:ename,empno=:empno",{"ename":'값',"empno":값})
           
      INSERT
           emp=(값,값....) => 브라우저에서 읽기 
             <input type=text name=name size=15>
             name=request.TextField('name')  = 장고
             <textarea name=content>
             content=request.CharactorField('content') = 장고
             data=(name,content)
           execute("INSERT INTO emp VALUES(?,?,?,?,?,...)",emp)
      UPDATE
           execute("UPDATE table1 SET name=? WHERE id=?",('홍길동','hong'))
           execute("UPDATE table1 SET name=:name WHERE id=:id",{'name':값,"id":값})
           execute("UPDATE table1 SET name=%s WHERE id=%s",%('값','값')
      DELETE
           execute("DELETE FROM table WHERE id=:id",{"id":'aaa'})
           execute("DELETE FROM table WHERE id=%s",%('값'))
'''
import sqlite3
'''
conn=sqlite3.connect("member.db")
cur=conn.cursor()
sql="CREATE TABLE member(id text,name text,sex text,addr text,tel text)"
cur.execute(sql)
print("테이블 생성 완료")
cur.close()
conn.close()
'''
#1. insert
def insert():
  #getConnection
  conn=sqlite3.connect("member.db")
  cur=conn.cursor()
  id=input("ID 입력:")
  name=input("이름 입력:")
  sex=input("성별 입력:")
  addr=input("주소 입력:")
  tel=input("전화번호 입력:")
  data=(id,name,sex,addr,tel)
  sql="INSERT INTO member VALUES(?,?,?,?,?)"
  #실행 
  cur.execute(sql,data)
  conn.commit()
  print("데이터 추가 완료!!")
  #disConnection
  cur.close()
  conn.close()

def selectList():
    conn=sqlite3.connect("member.db")
    cur=conn.cursor()
    sql="SELECT * FROM member"
    cur.execute(sql)
    #출력
    for row in cur:
        print(row)
    cur.close()
    conn.close()

def selectOne():
    conn=sqlite3.connect("member.db")
    cur=conn.cursor()
    id=input("ID를 입력:")
    sql="SELECT * FROM member WHERE id=:id"
    cur.execute(sql,{"id":id})
    data=cur.fetchone()
    print(data)
    cur.close()
    conn.close() 

def update():
    conn=sqlite3.connect("member.db")
    cur=conn.cursor()
    id=input("ID 입력:")
    name=input("이름 입력:")
    sex=input("성별 입력:")
    addr=input("주소 입력:")
    tel=input("전화번호 입력:")
    data=(name,sex,addr,tel,id)
    sql="""
         UPDATE member SET
         name=?,sex=?,addr=?,tel=?
         WHERE id=?
        """
    cur.execute(sql,data)
    conn.commit()
    print("수정 완료!!")
    cur.close()
    conn.close()

def delete():
    conn=sqlite3.connect("member.db")
    cur=conn.cursor()
    id=input("ID 입력:")
    sql=f"""
           DELETE FROM member
           WHERE id='{id}'
         """
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()
    
#insert()
#selectList()
#selectOne()
#update()
#selectList()
delete()
selectList()















