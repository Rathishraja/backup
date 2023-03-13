import sqlite3

conn=sqlite3.connect('text.db')

c=conn.cursor()
#c.execute("CREATE TABLE student(id INTEGER PRIMARY KEY, name text, age INTEGER) ")

#c.execute("INSERT INTO student values(1,'rathish',17)")
c.execute("select * from student")
print(c.fetchall())
#print("table created")
#print("values inserted")s
conn.commit()
conn.close()