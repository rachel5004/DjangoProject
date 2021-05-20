'''
    클래스 : 객체지향프로그램 (OOP)
            면접) OOP
    1) 클래스 구성 
       1. 멤버변수 : 상태 (state) 
          Back-End , Front-End => 프로그램은 데이터(상태) 관리
       2. 멤버함수(멤버메소드) : 행위(동작) => 요청 => 메세지 (통신할수 있는 상태)
          면접) 함수 VS 메소드 
               Function VS Procedure
          예)
               A   <=========>    B
                     message(주고 받기) : 함수호출 (값을 매개변수에 첨부)
                     사용 => 메소드 
       3. 생성자 : 멤버변수를 초기화 
    2) 클래스 선언 
       = 클래스명 식별 
         = 알파벳으로 시작 (대소문자 구분), _ , 한글사용 ( _는 임시 클래스)
         = 숫자는 사용 가능(앞에 사용금지) 
         = 예약어는 사용 할 수 없다
       class 클래스명 <(상속클래스)>:
             멤버변수 
             def 메소드명(self):
                메소드 처리 
'''
class Member:
    id=''
    name=''
    sex=''
    addr=''
    tel=''

# 메모리 할당
mem=Member()
mem.id='hong'
mem.name='홍길동'
mem.sex='남자'
mem.addr='서울'
mem.tel='010-1111-1111'

mem1=Member()
mem1.id='shim'
mem1.name='심청이'
mem1.sex='여자'
mem1.addr='부산'
mem1.tel='010-2222-2222'

#출력 
print(f"ID:{mem.id}")
print(f"Name:{mem.name}")
print(f"Sex:{mem.sex}")
print(f"Addr:{mem.addr}")
print(f"Tel:{mem.tel}")
print("=============")
print(f"ID:{mem1.id}")
print(f"Name:{mem1.name}")
print(f"Sex:{mem1.sex}")
print(f"Addr:{mem1.addr}")
print(f"Tel:{mem1.tel}")














