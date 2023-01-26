import sqlite3
conn = sqlite3.connect("sqlite.db")
conn.execute('''

        update student set st_name='ayush', st_email="ayush@gamil.com" where st_id = 11

        ''')
conn.commit()
conn.close()