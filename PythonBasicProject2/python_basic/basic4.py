#오라클 연결 => import cx_Oracle
#오라클 설치 => 드라이버 => pip install cx_Oracle , pip install django
import cx_Oracle
'''
   오라클 
    SQL종류 
    DML
     = SELECT (데이터 검색)
       형식)
           SELECT * | column1,column2...
           FROM table명|view명|SELECT~    ===> 필수 
           [
               WHERE 컬럼명(함수명) 연산자 값
               GROUP BY 그룹컬럼
               HAVING 그룹컬럼
               ORDER BY 컬럼명 (ASC|DESC) => ASC생략이 가능 
                        =====
                        번호로 대체
           ]
           => ORDER BY => /*+ INDEX_ASC(테이블명,PK) */
           1) WHERE 
              = 연산자
                산술연산자 
                논리연산자
                비교연산자 
                = BETWEEN ~ AND 
                = LIKE => REGEXP_LIKE
                  name => '홍' , '이' ,'김' , '박' , '강'
                  WHERE name LIKE '%홍%' 
                        OR name LIKE '%이%'
                        OR name LIKE '%김%'
                        OR name LIKE '%박%'
                        OR name LIKE '%강%'
                  WHERE REGEXP_LIKE(name,'홍|이|김|박|강')
                = IN 
                = NULL : IS NULL , IS NOT NULL
                = NOT : NOT BETWEEN~AND , NOT LIKE , NOT IN
           2) 내장함수 
                = 문자열 : SUBSTR , LENGTH , RPAD 
                = 숫자 : CEIL , ROUND , TRUNC , MOD
                = 날짜 : SYSDATE
                = 변환 : TO_CHAR
                = 일반 : NVL
                = 집합함수 : COUNT,MAX
           3) 조인 
                = INNER JOIN
                   = Oracle 조인
                   = ANSI 조인 
                = OUTER JOIN
                   = LEFT OUTER JOIN
                   = RIGTH OUTER JOIN
           4) 서브쿼리 
                = 단일행 서브쿼리 () 서브쿼리의 값이 1개인 경우
                = 다중행 서브쿼리 값이 여러개 (IN,MAX,MIN) => IN , ANY , ALL
                = 조인 (SELECT에서만 사용) , 모든 DML에서 사용이 가능 
           5) View
                = 인라인뷰 (페이지 설정)
           6) Index  
                = 최적화 (속도)
     = INSERT (데이터 추가)
       형식)
            INSERT INTO table VALUES(값....)
            INSERT INTO table(컬럼명...) VALUES(값...)  default값이 있는 경우 
     = UPDATE (데이터 수정)
       형식)
            UPDATE table SET
            컬러명=값,컬럼명=값...
            [WHERE]
     = DELETE (데이터 삭제)
       형식)
            DELETE FROM table
            [WHERE]
    DDL (COMMIT)
      = CREATE 
        = 제약조건 (PRIMARY KEY,FOREIGN KEY,CHECK,UNIQUE,NOT NULL)
      = ALTER : ADD , MODIFY , DROP
      = DROP
      = TRUNCATE
      = RENAME
    DCL (GRANT: 권한부여,REVOKE:권한해제) => DBA
    TCL
      = COMMIT
      = ROLLBACK
      
      ==> CURSOR = 자바(ResultSet)
'''
#1. 오라클 연결 
conn=cx_Oracle.connect("hr/happy@localhost:1521/xe")
#2. SQL문장 전송
cursor=conn.cursor()
#3. 결과값을 받아서 출력
#empno=int(input("사번 입력:"))
'''sql=f"""
      SELECT * FROM emp 
      WHERE empno={empno}
    """
#오라클 조인 
sql=f"""
       SELECT empno,ename,job,hiredate,sal,dname,loc
       FROM emp,dept
       WHERE emp.deptno=dept.deptno
     """

sql=f"""
       SELECT empno,ename,job,hiredate,sal,dname,loc,grade
       FROM emp JOIN dept
       ON emp.deptno=dept.deptno
       JOIN salgrade
       ON sal BETWEEN losal AND hisal
     """

empno=int(input("사번 입력:"))
sql=f"""
      SELECT ename,RPAD(SUBSTR(ename,1,2),LENGTH(ename),'*')
      FROM emp
      WHERE empno={empno}
    """
'''
page=int(input("페이지 입력:"))
rowSize=5
start=(rowSize*page)-(rowSize-1)
end=rowSize*page

sql=f"""
      SELECT empno,ename,job,sal,dname,loc,num
      FROM (SELECT empno,ename,job,sal,dname,loc,rownum as num
      FROM (SELECT empno,ename,job,sal,dname,loc 
      FROM emp,dept
      WHERE emp.deptno=dept.deptno
      ))
      WHERE num BETWEEN {start} AND {end}
    """
cursor.execute(sql)
#출력 
for row in cursor:
    print(row)
#4. 오라클 닫기
cursor.close()
conn.close()
 







