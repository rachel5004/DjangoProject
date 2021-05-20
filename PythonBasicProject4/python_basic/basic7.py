'''
   프로그램 : 모아서 관리 
            변수 => 배열 (리스트,튜플,딕트)
            명령문 => 메소드(함수)
            변수+메소드 = 클래스 
   1. 클래스 개념 
            변수+메소드 = 클래스 => 재사용이 쉽게(오버라이딩,기능추가,데이터 보호)
   2. 클래스의 구성요소
        변수 (데이터 저장) : 객체마다 따로 메모리 공간이 생긴다 
        메소드 (변수 처리문제)
        생성자 (변수 초기화)
          def __init__(self,.....):
        소멸자 (객체 메모리 해제)
          def __del__(self)
          ===> 모든 클래스는 자신의 객체주소를 가지고 있다 
               파이썬외의 다른 언어 : this
               파이썬 : self
   3. 클래스가 여러개 일 경우 처리
      1) 상속 (is-a) : 수정해서 재사용을 한다 
      2) 포함 (has-a): 클래스를 변경하지 않고 그대로 사용 (라이브러리)
   4. 클래스 종류 (추상클래스,인터페이스)
   5. 응용 
'''
import sqlite3
from _overlapped import NULL
class StudentVO:
    sabun=0
    name=''
    dept=''
    loc=''
    sal=0

class StudentDAO:
    conn=NULL #포함 클래스
    cursor=NULL #포함 클래스 
    def __init__(self):
        print("생성자 호출!!")
    def __del__(self):
        print("소멸자 호출!!")
    def getConnection(self):
        self.conn=sqlite3.connect("sawon.db")
        self.cursor=self.conn.cursor()
    def disConnection(self):
        self.cursor.close()
        self.conn.close()
    def dbCreate(self):
        self.getConnection()
        sql="CREATE TABLE IF NOT EXISTS sawon(sabun int,name text,dept text,loc text,sal int)"
        self.cursor.execute(sql)
        self.disConnection()
    def selectList(self):
        self.getConnection()
        sql="SELECT * FROM sawon"
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
        self.disConnection()
        return data
    def insert(self,vo):
        self.getConnection()
        data=(vo.sabun,vo.name,vo.dept,vo.loc,vo.sal)
        sql="INSERT INTO sawon VALUES(?,?,?,?,?)"
        self.cursor.execute(sql,data)
        self.conn.commit()
        print("사원 등록 완료!!")
        self.disConnection()
    def selectOne(self,sabun):
        self.getConnection()
        sql=f"SELECT * FROM sawon WHERE sabun={sabun}"
        self.cursor.execute(sql)
        data=self.cursor.fetchone()
        self.disConnection()
        return data
    def delete(self,sabun):
        self.getConnection()
        sql=f"DELETE FROM sawon WHERE sabun={sabun}"
        self.cursor.execute(sql)
        self.conn.commit()
        print("삭제 완료")
        self.disConnection()

dao=StudentDAO()
print("dao 객체 생성")
dao.dbCreate()
print("데이터베이스 table 생성")
#dao.delete(1)
data=dao.selectOne(2)
print(data)
'''
vo=StudentVO()
print("vo 객체 생성")
vo.sabun=int(input("사번 입력:"))
vo.name=input("이름 입력:")
vo.dept=input("부서 입력:")
vo.loc=input("근무지 입력:")
vo.sal=int(input("연봉 입력:"))
print("vo에 값을 채우기")
dao.insert(vo)
print("데이터베이스에 vo추가")

data=dao.selectList()
print("추가된 데이터 출력")
for row in data:
    print(row)
'''
        
    








