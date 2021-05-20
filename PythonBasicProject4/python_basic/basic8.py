# 오라클 연결 
import cx_Oracle
from _overlapped import NULL
class DeptVO:
    deptno=0
    dname=''
    loc=''
    
class EmpVO:
    empno=0
    ename=''
    job=''
    sal=0
    dvo=NULL #포함 클래스 (has-a)
    def __init__(self):
        dvo=DeptVO()
class EmpDAO:
    
    conn=NULL
    cursor=NULL
    def getConnection(self):
        self.conn=cx_Oracle.connect("hr/happy@localhost:1521/xe")
        self.cursor=self.conn.cursor() 
    def disConnection(self):
        self.cursor.close()
        self.conn.close()
    def selectOne(self,empno):
        self.getConnection()
        sql=f"""
              SELECT empno,ename,job,sal,dname,loc 
              FROM emp,dept 
              WHERE emp.deptno=dept.deptno
              AND empno={empno}
            """
        #실행 
        self.cursor.execute(sql)
        data=self.cursor.fetchone()
        print(data)
        vo=EmpVO()
        vo.empno=int(data[0])
        vo.ename=data[1]
        vo.job=data[2]
        vo.sal=int(data[3])
        #vo.dvo.deptno=int(data[4])
        #vo.dvo.dname=data[4]
        #vo.dvo.loc=data[5]   
        self.disConnection()
        return vo
       
dao=EmpDAO()
vo=dao.selectOne(7788)
print(f"사번:{vo.empno}")
print("이름:"+vo.ename)
print("직위:"+vo.job)
print("부서명:"+vo.dvo.dname)
print("근무지:"+vo.dvo.loc)









