import sqlite3
conn = sqlite3.connect("Dancuxa.db")

"""
conn.execute('''CREATE TABLE person
                (
                person_id INTEGER PRIMARY KEY AUTOINCREMENT,
                cccd char(12) NOT NULL,
                username TEXT NOT NULL,
                age text NOT NULL,
                city CHAR(50),
                sdt char(10) NOT NULL,
                mk char(10) NOT NULL
                );'''
            )
"""
                

x = conn.cursor()
"""x.execute("insert into person(username,age,city)VALUES('tao',19,'hanoi')")
conn.commit()"""
x.execute("select * from person")
data=x.fetchall()
for i in data:
    print(i) #username
conn.close()