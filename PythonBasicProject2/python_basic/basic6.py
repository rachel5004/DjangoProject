import sqlite3
 
# SQLite DB 연결
conn = sqlite3.connect("test.db")
 
# Connection 으로부터 Cursor 생성
cur = conn.cursor()
#cur.execute("insert into customer values (:name, :score)", {'name':'c', 'score':99})
#conn.commit()
#cur.execute("insert into customer values (?, ?)", ('b', 1))
#conn.commit()
#cur.execute("create table customer (name text, score int)")
#cur.execute("insert into customer values ('a', 100)")
#conn.commit()
'''
data = [
 ('d', 93),
 ('e', 11)
]   

cur.executemany("insert into customer values (?, ?)", data)
conn.commit()
'''
# SQL 쿼리 실행
cur.execute("select * from customer")
 
# 데이타 Fetch
rows = cur.fetchall()
for row in rows:
    print(row)
 
# Connection 닫기

conn.close()