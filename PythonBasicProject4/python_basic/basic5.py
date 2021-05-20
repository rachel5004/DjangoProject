kor=100 #전역변수 

def score():
    print("여기는 함수 영역")

class Student:
    kor=90 #멤버변수 
    def score(self):
        print(f"국어 점수:{self.kor}")
        print(f"국어 점수:{kor}")
        score()
    def score2(self):
        kor=80 #지역변수 
        print(f"국어 점수:{kor}")
        score()
        self.score()
#객체 생성 
'''
   변수 영역 
   => 1. 지역변수 
      2. 객체변수(멤버변수) = 반드시 self.
      3. 전역변수 
'''
s=Student()
#score()
s.score()
s.score2()
