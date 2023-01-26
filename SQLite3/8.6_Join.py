import sqlite3
conn = sqlite3.connect("sqlite.db")
print("st_id","st_name","st_fees")
data = conn.execute("select * from fees as F inner join student as S on F.st_id = S.st_id")
# data = conn.execute("select F.fees_id, S.st_name, F.fees_amount from fees as F inner join student as S on F.st_id = S.st_id")

# inner join = full both match join
# left join = full left and right match join
# right join = left match and full right join
# full join = not support in SQLite3.

for a in data:
    print(a)

conn.close()
