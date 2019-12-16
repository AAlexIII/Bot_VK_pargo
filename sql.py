import sqlite3
'''
записать нового пользователя
изменить штуки
столбик заполнения
прочитать данные
'''
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE good(ID int, muslo text, zod text,fak text, parn text, done text)")
cursor.execute("""INSERT INTO good
                VALUES (000, 'Скорее всего', 'ЯСНО',
                                'Осадков Нет', '1111','343r')""")
urr = '001'
cursor.execute("DELETE FROM good")
# Вставляем данные в таблицу
cursor.execute("""INSERT INTO good
                VALUES (45445, 'Andy Hunter', '7/24/2012',
                                'Xplore Records', 'MP3','343r')""")
conn.commit()
cursor.execute("""SELECT ID FROM good""")
print(cursor.fetchone())
cursor.execute("UPDATE good SET muslo = :l WHERE ID = 45445", {'l': urr})
conn.commit()
cursor.execute("""SELECT ID, muslo FROM good WHERE ID = :l""", {'l': 45445})
print(cursor.fetchone())

conn.close()