import sqlite3

conn = sqlite3.connect('studentdata.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE studentdata
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  phone TEXT,
                  mail TEXT,
                  fees_status TEXT)''')


cursor.execute("INSERT INTO studentdata (id, name, phone, mail, fees_status) VALUES ('1','Rathish', '9999999999', 'rathish@sample.com', 'yes')")


conn.commit()

cursor.execute("INSERT INTO studentdata (id, name, phone, mail, fees_status) VALUES ('2','vishwa', '9999999998', 'vishwa@sample.com', 'no')")

conn.commit()


cursor.execute("INSERT INTO studentdata (id, name, phone, mail, fees_status) VALUES ('3','gokul', '9999999997', 'gokul@sample.com', 'yes')")


conn.commit()


conn.close()