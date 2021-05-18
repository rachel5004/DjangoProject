# default 매개변수 
'''
   형식)
       def func(a,b,c):
          처리문장 
       def func(a,b=10,c=20)
       
       => 호출 
          func(100,200,300)  => a=100 , b=200 , c=300
          func(100)          => a=100 , b=10 , c=20
          func(100,200)      => a=100 , b=200 , c=20
      def func(a=10,b=20)
      
       => 호출 
          func()    ====> a=10 , b=20
          func(100) ====> a=100 , b=20
          func(100,200) => a=100 , b=200
'''
#오류 => 매개변수 맨마지막부터 설정 (고정데이터를 데이터베이스에 첨부)
'''
def func(a=100,b,c):
    print(f"a={a},b={b},c={c}")

#함수 호출
func(10,100,100)
func(100,200,300)
func(100,300)
func(100,300,500)
'''
#가변 데이터형 (매개변수의 갯수가 확장이 안된 경우에 사용)
'''
  def func(*args):
     처리문장 
     
  func()
  func(1,2,3,4,5,6)
  func(1,2,3)
'''
# *args => Tuple () 
# [] => list
# {} , {key:값}
def func(*args):
    print(args)
    print(list(args))
    sum=0
    for i in args:
        sum+=i
    print(f'총합:{sum}')

def func1(*names):
    print(names)
    print(list(names))
    
func1('홍길동')
func1('홍길동','심청이','박문수')
#호출 
'''
func()
func(1,2)
func(1,2,3)
func(1,2,3,4,5)
func(1,2,3,4,5,6,7,8,9,10)
'''








