'''
    함수 만드는 방법 (자바 = 메소드)
    = 명령문을 모아서 처리(재사용) 
    = 변수,제어문,연산자
    = 기능 한개만 수행이 가능 
    = 함수의 종류 
       = 사용자 정의
       = 라이브러리  (print,str)
    = 사용자 정의 함수 (리턴형,매개변수) 
      1) 리턴형(X) , 매개변수(X)
         형식)
             def 함수명():
                처리문장
      2) 리턴형(X) , 매개변수(O)
          형식)
            def 함수명(매개변수,매개변수..):
                처리문장 
      3) 리턴형(O) , 매개변수(X)
          형식) 
            def 함수명():
              처리문장 
              return 값
      4) 리턴형(O) , 매개변수(O)
           형식)
             def 함수명(매개변수,매개변수..):
               처리문장 
               return 값
      5) 매개변수 => default매개변수 => 매개변수는 뒤에서부터 설정
           형식)
             def 함수명(매개변수,매개변수=값,매개변수=값)
             예) print(value,end='\n')
             def 함수명(a=10,b=10,c=10) (a,b,c=20)
                                       (1,10)
             => 함수명(1,2) => error
      6) 매개변수 => 가변 매개변수 (자바 : ...)
           형식)
             def 함수명(*args) => 포인터 (C)
             함수명(1)
             함수명(1,2,3)
             함수명(1,2,3,4,5,6)   
            
'''
from random import randrange
'''
# 함수 (리턴형이 없고 , 매개변수가 없는 함수)
# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
def gugudan():
    for i in range(1,10):
        for j in range(2,10):
            print(f"{j}*{i}={j*i}",end="\t")
        print('')

#호출 
gugudan()
print('')
gugudan()
'''
'''
     for(int i=0;i<data.length-1;i++)
     {
        for(int j=i;j<data.length;j++)
        {
        }
     }
'''
import random
#  range(start, stop[, step]) range(1,10,2)
def sort():
    #지역변수 (리스트:중복데이터 설정 , 수정이 가능) => () => 데이터 수정이 불가능 (데이터베이스에서 데이터 읽기)
    data=[30,40,10,50,20]
    print(data)
    for i in range(len(data)-1):
        for j in range(i,len(data)):
            if(data[i]>data[j]):
                temp=data[i]
                data[i]=data[j]
                data[j]=temp
    print(data)
sort()

#리턴형이 없고 매개변수가 존재 
'''
  def func(매개변수...)  ==> void (함수영역안에서 처리)
      처리문장 
'''
# 리스트 데이터 설정 
data=[1,2,3,4,5]
for i in range(5):
    k=random.randrange(1,100)
    data[i]=k
print(data)

#함수 
def sort1(list):
    #print(list)
    for i in range(len(list)):
        for j in range(i,len(list)):
            if list[i]<list[j]:
                temp=list[i]
                list[i]=list[j]
                list[j]=temp
    print(list)

sort1(data) #함수 호출

#리턴형이 있는 함수 , 매개변수 (X)
'''
  형식)
       def func():
           처리문장
           return 값
'''
def getName():
    return '홍길동'

name=getName()
print(f'이름은 {name}')
print(getName())

def getRand():
    return random.randrange(1, 100)
num=getRand()
print(num)

#리턴형(O),매개변수(O)
'''
   자료형 , 기본문법 
   함수 
   클래스 (객체지향)
   에러처리,파일입출력 (데이터 수집 , 데이터 통계) => Spring
   데이터베이스 
   Socket프로그램
   웹프로그램(장고)
'''
'''
  데이터베이스 SELECT    ====> MVC (MVT:models,views.py,template)
  def func(매개변수,매개변수...):
      처리문장 
      return 값
'''
def plus(a,b):
    c=a+b #처리
    return c
def minus(a,b):
    c=a-b
    return c
def gop(a,b):
    c=a*b
    return c
def div(a,b):
    c=0
    if b==0:
        c=0
    c=a//b
    return c    

a=10
b=2
print(plus(a,b))
print(minus(a, b))
print(gop(a, b))
print(div(a, b))











