'''
   예외처리 : 에러를 방지하는 프로그램 
   =======  강제종료를 방지하고 정상 종료를 할 수 있게 만드는 프로그램 
   형식)
        try:
          정상수행 문장이 들어간다 
        except: ====> 여러개를 사용 할 수 있다 (수정이 가능한 에러만 처리)
          에러가 발생시에 처리 
        finally:
          try,excpet와 관련없이 무조건 수행되는 문장 (서버 종료, 데이터베이스 종료)
          
        1. Python에서 제공하는 예외처리 클래스 
           BaseException (Throwable)
              |
        -----------------------------------------------
        |              |                              |
     SystemExit  KeyboardInterrupt               Exception(수정가능)
     =============================                   |
         Error(수정이 불가능)                        ArithmeticError (산술에러)
                                                      = FloatingPointError
                                                      = OverflowError
                                                      = ZeroDivisionError
'''
'''
def div(a,b):
    return a/b

try:
    c=div(5,2)
    print(c)
    d=div(5,0) #오류 발생 (모든 프로그램은 0으로 나눌 경우에 오류 발생) => 오류발생시 = except찾는다 밑에 있는 문장하지 않는다 
    print(d)
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다') #오류가 났을 경우에 복구
finally:
    print("정상 종료!!")
print("프로그램 종료")
'''
'''
     <c:forEach var="vo" items="${list}">
        
     </c:forEach>
     
     <%
         for(MovieVO vo:list)
         {
     %>
             <tr>
             <td></td>
             </tr>
     <%
         }
     %>
     
     {<% for vo in list %>}
     
     문법 오류  : 프로그래머의 실수 (자동으로 이클립스에서 잡아 준다) => 들여쓰기
     예외 오류 : 사용자의 입력값 , 프로그래머의 실수 
'''
def div(a,b):
    return a/b
try:
    c=div(10,3)
    print(c)
    d=div(10,0)
    print(d) #출력이 안된다 
    
    e=[2,3]
    print(e[0])
    print(e[1])
    print(e[3]) #IndexError
    
    f=open('c:/pythonDev/upload.txt') #Exception
    
except Exception as e:
    print('에러메세지:',e)
    
except ZeroDivisionError:
    print("0으로 나눌 수 없다")
except IndexError as e:
    print("에러메세지:",e) #ex.getMessage()

finally:
    print("여기는 무조건 수행 문장")
print("작업 완료")
    
    
    














