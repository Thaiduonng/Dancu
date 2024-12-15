import sqlite3

conn = sqlite3.connect("Canbo.db")

"""
conn.execute('''CREATE TABLE manageraccount
                (
                username TEXT NOT NULL,
                mk char(10) NOT NULL
                );'''
            )
"""

x = conn.cursor()
"""x.execute("insert into person(username,age,city)VALUES('tao',19,'hanoi')")
conn.commit()"""
x.execute("select * from person")
data = x.fetchall()
for i in data:
    print(i[1])  # username
conn.close()