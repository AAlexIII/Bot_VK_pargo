import sqlite3
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE good(ID int, muslo text, zod text,fak text, parn text, done text)")
cursor.execute("""INSERT INTO good
                VALUES (000, 'Скорее всего', 'ЯСНО',
                                'Осадков Нет', '1111','343r')""")
conn.commit()
conn.close()
