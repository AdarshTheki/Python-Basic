import sqlite3
conn = sqlite3.connect("sqlite.db")
# Insert Value 
ins = '''
    insert into student (st_id, st_name, st_class, st_email) values 
    (10,'ravi1','12th','ravi4=ram@gmail.com'),
    (11,'ravi2','12th','ravi4=ram@gmail.com'),
    (12,'ravi3','12th','ravi4=ram@gmail.com'),
    (13,'ravi4','12th','ravi4=ram@gmail.com'),
    (14,'ravi5','12th','ravi4=ram@gmail.com')  
'''
conn.execute(ins)
conn.commit()
conn.close()