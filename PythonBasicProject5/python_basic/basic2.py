#예외처리 
def display(fname):
    try:
        f=open(fname)
        print("정상수행") #정상 수행하는 문장 
    except Exception as e:
        print("에러메세지:",e) #사전에 예상되는 에러 처리
    finally:
        print("무조건 수행!!") #서버종료,데이터베이스 종료 
    print("메소드 정상 종료") 

def display2():
    print(1) 
    print(2)
    # 무조건 수행 
    try:
        print(3) #정상수행
        print(4) #정상수행
        print(10/0) # 오류 발생 => except로 이동 
        print(5) #수행하지 못한다 
    except ZeroDivisionError as e:
        print("6.에러:",e) # 수행
    finally:
        print(7) #수행
    print(8) #수행 
    
#display("./basic1.py")
display2()
    