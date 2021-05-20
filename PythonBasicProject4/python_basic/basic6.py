'''
  객체 지향 프로그램 
  = is-a : 상속
  = has-a : 포함 
'''
from _overlapped import NULL
'''
  class Emp {
     private Dept dvo=new Dept();
  }
  class Dept {
  }
'''
# has-a : Join 
class Dept:
    deptno=0
    dname=''
    loc=''
    def setDeptno(self,deptno):
        self.deptno=deptno
    def getDeptno(self):
        return self.deptno
    def setDname(self,dname):
        self.dname=dname
    def getDname(self):
        return self.dname
    def setLoc(self,loc):
        self.loc=loc
    def getLoc(self):
        return self.loc
    def showDept(self,deptno,dname,loc):
        self.setDeptno(deptno)
        self.setDname(dname)
        self.setLoc(loc)
    
class Emp:
    empno=0
    ename=''
    handler=NULL
    def __init__(self,empno,ename):
        self.empno=empno
        self.ename=ename
        self.handler=Dept()
        self.handler.showDept(10, '개발부', '서울')
    def show(self):
        print(f"사원번호:{self.empno}") # + (숫자+숫자) (문자열+문자열) , (숫자+문자열)(X)
        print("사원이름:"+self.ename)
        print(f"부서번호:{self.handler.getDeptno()}")
        print("부서명:"+self.handler.getDname())
        print("근무지:"+self.handler.getLoc())
        
emp=Emp(7788,'홍길동')
emp.show()   
    
    
    
    
    
    
    
    
    
    
    
