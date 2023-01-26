import sqlite3
conn = sqlite3.connect("sqlite.db")
# Print and Execute for table
data = conn.execute("select * from student")
print("st_id","st_name","st_class","st_email")
for n in data:
    print(n[0]," ",n[1]," ",n[2]," ",n[3])
    