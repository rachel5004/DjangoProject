class StudentVO:
    name=''
    kor=0
    eng=0
    math=0
class StudentManager:
    #f=None
    #def __init__(self):
        #f=open('c:/pythonDev/student.txt','a')
    def fileWrite(self,vo):
        try:
            with open('c:/pythonDev/student.txt','a') as f:
                 data="{},{},{},{},{},{}\n".format(vo.name,vo.kor,vo.eng,vo.math,(vo.kor+vo.eng+vo.math),(vo.kor+vo.eng+vo.math)/3.0)
                 f.write(data)
            print("입력 완료")
        except Exception as e:
            print("입력 에러:",e)

sm=StudentManager()
vo=StudentVO()
vo.name=input('이름 입력:')
vo.kor=int(input("국어 입력:"))
vo.eng=int(input("영어 입력:"))
vo.math=int(input("수학 입력:"))
sm.fileWrite(vo)
                
            
    