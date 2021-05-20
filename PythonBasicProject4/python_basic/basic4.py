'''
    class Member {
       String name;
       public void display(this){ => 모든 멤버 메소드에는 this를 가지고 있다
         name=""
         => this.name ==> this를 생략할 수 있다 
       }
       public void init(this){
       }
       public static void disp(){
       }
    }
'''
#멤버메소드 
class Sawon:
    #멤버변수 선언
    sabun=1
    name=''
    dept=''
    job=''
    sal=0
    #초기화 (생성자)
    def __init__(self): #default 생성자 (만들지 않을 경우에 자동으로 생성)
        print("생성자 함수 호출!!")
    #소멸자 
    def __del__(self):
        print("소멸자 함수 호출!!")
    #기능 설정 : 멤버메소드 
    def setSabun(self,sabun):
        self.sabun=sabun
    def getSabun(self):
        return self.sabun
    def sawonPrint(self):
        print(f"사번:{self.sabun}")
        print("이름:"+self.name)
        print("부서:"+self.dept)
        print("직위:"+self.job)
        print(f"급여:{self.sal}")
#호출 
hong=Sawon()
hong.setSabun(1)
hong.name="홍길동"
hong.dept="개발부"
hong.job="사원"
hong.sal=3000
hong.sawonPrint()
        
        
        
        
        
        
        
    