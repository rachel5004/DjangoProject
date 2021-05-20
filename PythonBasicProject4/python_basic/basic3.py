# 생성자 
'''
     C++ : 소멸자 
           생성자
           class A
           {
              A(){}
              ~A(){}
           }
     Java : 생성자 , 가비지켈렉션 () => System.gc() => finalize()
     Python 
           class A:
             def __init__(self)
             def __del__(self)
           
'''
class Nice:
    name=''
    def __init__(self,name): #생성자
        self.name=name
        print('생성자 메소드에 의해 '+name+'객체 생성 됨')
    def __del__(self):  #소멸자 
        del self.name
        print('소멸자 메소드 수행')
# 생성자를 호출하는 부분 
# 객체 자신 : this , 객체 자신 : self
Nice('홍길동') # __init__ 호출 , __del__ 소멸 

class Member:
    name='홍길동'
    sex=''
    def __init__(self,name,sex):
        self.name=name
        self.sex=sex
    def __del__(self):
        print("객체 메모리 해제:소멸자함수")

name=input('이름 입력:')
sex=input('성별 입력:')
hong=Member(name,sex)
#출력 
print(f"이름:{hong.name}")
print(f"성별:{hong.sex}")








