import sqlite3

# Kết nối tới cơ sở dữ liệu (hoặc tạo mới nếu chưa có)
conn = sqlite3.connect('zl.db')

# Tạo bảng với cú pháp sửa lỗi
""" conn.execute('''CREATE TABLE nguoi_dan(
        person_id INTEGER PRIMARY KEY AUTOINCREMENT,  
        Username TEXT NOT NULL UNIQUE,
        Tuoi INTEGER NOT NULL,
        dia_chi CHAR(50)
);''') """
x=conn.cursor()

x.execute("insert into nguoi_dan(person_id,Username,Tuoi,dia_chi)VALUES('03','dũng','19','hoa binh')")
conn.commit()
# Đóng kết nối
conn.close()


