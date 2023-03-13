from flask import Flask, request
import sqlite3
conn = sqlite3.connect('studentdata.db', check_same_thread=False)
 app=Flask(_name_)
 @app.route('/')
 def home():
     return 'welcome'
 @app.route('/insert', methods=['GET', 'POST'])
 def insert():
     conn.execute("INSERT INTO studentdata (id , name , phone , mail, fees_status         ) values (2, 'Sivasree', 987654356, 'Chennai', 50000)")
     conn.commit()
     values = read()
     return values
 @app.route('/update')
 def update():
     id = request.args.get("id")
     contact=request.args.get("phone")
     conn.execute(f"UPDATE studentdata SET phone = {contact} where id = {id}")
     conn.commit()
     values = read()
     return values
 @app.route('/delete')
 def delete():
     conn.execute("DELETE FROM studentdata where id = 4")
     conn.commit()
     values = read()
     return values
 def read():
     values = conn.execute("SELECT * FROM studentdata")
     emp_list=[]
     for value in values:
         emp_list.append(value)
     return emp_list
 # def startpy():
 #     print("Tact101")
 if _name_ == '_main_':
     app.run(debug = True)