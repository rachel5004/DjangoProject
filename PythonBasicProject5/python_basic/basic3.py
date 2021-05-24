'''
  파일 입출력 (업로드 , 다운로드)
  파이썬 특화언어 (데이터 수집) => 데이터베이스에 첨부하는 것은 아니다
  Jsoup : 이미 데이터베이스에 존재하는 내용 
  => 채팅문자열 , 트위터 .... => 분석 , 통계 (통계낸 데이터를 DB에 설정)
  파일 입출력 
  형식)
      1. 파일 열기 
         f=open('파일명(경로명)','모드')
      2. 조작 (읽기,쓰기,첨부)
              모드 : r(읽기모드) , w(쓰기모드) , a(추가모드)
      3. 파일 닫기 
         f.close()
'''
#쓰기 
def writedata():
    try:
        f=open('c:/pythonDev/student.txt','a') #w => create (파일 생성하고 내용을 저장)
        for i in range(1,11):
            data="홍길동 %d\n" %i
            f.write(data)
        f.close()
        print("데이터 저장 완료")
    except Exception as e:
        print("파일 에러:",e)

#readline
def readdata():
    try:
        f=open('c:/pythonDev/student.txt','r') #r => 읽기 => create(X) : 파일리 존재해야 된다
        #값을 읽어오기
        while 1: #0이 아닌 모든 수는 True (0,0.0=>False)
           line=f.readline() #한줄식 읽어올때
           if not line:
               break
           print(line,end='')
        f.close()
    except Exception as e:
        print("파일 에러:",e)
#readlines
def readdatas():
    try:
        f=open('c:/pythonDev/student.txt','r')
        liens=f.readlines() #전체를 읽어 온다 => [] list형식으로 읽는다 
        '''
          데이터가 여러개를 가지고 올때 
           = 데이터베이스 => () : 튜플
           = 파일 (일반파일) => [] : 리스트
           = 파일(JSON) => {"key":"값"} : 딕트
        '''
        print(liens)
        for line in liens:
            print(line,end='')
        f.close()
    except Exception as e:
        print('에러:',e)

def readdata2():
    try:
        f=open('c:/pythonDev/student.txt','r')
        data=f.read() #파일 내용전체를 문자열로 리턴하는 함수 
        print(data)
        f.close()
    except Exception as e:
        print('에러:',e)  

# with => 자동으로 파일을 닫아 준다  (f.close()) = 프로그래머가 편리성
def readWithdata():
    try:
        with open('c:/pythonDev/student.txt','r') as f:
            line=f.readlines()
            print(line)
        #f.close()
    except Exception as e:
        print('에러:',e)

#함수 호출 
#writedata()
#readdata()
#readdatas()
#readdata2()
readWithdata()







