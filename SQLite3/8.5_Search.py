import sqlite3
conn = sqlite3.connect("sqlite.db")

data = conn.execute("select * from student")

# Print and Execute for table
print("st_id","st_name","st_class","st_email")
for n in data:
    print(n[0]," ",n[1]," ",n[2]," ",n[3])

print("")

# Searching Name:
st_name=input("Enter the Student Name:- ")

# data = conn.execute("select * from student where st_name='"+st_name+"'")  exect_match_name
data = conn.execute("select * from student where st_name like '%"+st_name+"%'")   # one_two_words_name
for n in data:
    print(n[0]," ",n[1]," ",n[2]," ",n[3])
