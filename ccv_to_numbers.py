import csv
import json

FILENAME = "datas.csv"

data = []
with open(FILENAME, encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        a = []
        b = []
        if row[0] == "РОК":
            q = [0, 0, 0, 1]
            for i in q:
                a.append(i)
                b.append(i)
        if row[0] == "ПОП":
            q = [0, 0, 1, 0]
            for i in q:
                a.append(i)
                b.append(i)
        if row[0] == "Русский РЭП":
            q = [0, 1, 0, 0]
            for i in q:
                a.append(i)
                b.append(i)
        if row[0] == "Классическую":
            q = [1, 0, 0, 0]
            for i in q:
                a.append(i)
                b.append(i)
        if row[1] == "Рак, Скорпион, Рыбы":
            q = [0, 0, 0, 1]
            for i in q:
                a.append(i)
                b.append(i)
        if row[1] == "Близнецы, Весы, Водолей":
            q = [0, 0, 1, 0]
            for i in q:
                a.append(i)
                b.append(i)
        if row[1] == "Овен, Лев, Стрелец":
            q = [0, 1, 0, 0]
            for i in q:
                a.append(i)
                b.append(i)
        if row[1] == "Телец, Дева, Козерог":
            q = [1, 0, 0, 0]
            for i in q:
                a.append(i)
                b.append(i)
        if row[2] == "ФЭиФ":
            q = [1, 0, 0]
            for i in q:
                a.append(i)
                b.append(i)
        if row[2] == "ФИПМ":
            q = [0, 1, 0]
            for i in q:
                a.append(i)
                b.append(i)
        if (row[2] != "ФИПМ") and (row[2] != "ФЭиФ"):
            q = [0, 0, 1]
            for i in q:
                a.append(i)
                b.append(i)
        if row[3] == "Скорее всего":
            a.append(1)
        if row[3] == "Вряд ли":
            a.append(0)
        if row[4] == "ЯСНО":
            q = [0, 0, 0, 1]
            for i in q:
                a.append(i)

        if row[4] == "Затянутое серое небо":
            q = [0, 0, 1, 0]
            for i in q:
                a.append(i)

        if row[4] == "Солнце иногда пробивалось":
            q = [0, 1, 0, 0]
            for i in q:
                a.append(i)

        if row[4] == "Менялась кардинально в течении дня":
            q = [1, 0, 0, 0]
            for i in q:
                a.append(i)

        if row[5] == "Нет":
            q = [0, 0, 0, 1]
            for i in q:
                a.append(i)

        if row[5] == "Дождь и Снег":
            q = [0, 0, 1, 0]
            for i in q:
                a.append(i)

        if row[5] == "Дождь":
            q = [0, 1, 0, 0]
            for i in q:
                a.append(i)

        if row[5] == "СНЕГ!!!":
            q = [1, 0, 0, 0]
            for i in q:
                a.append(i)
        if row[6] == "1":
            q = [0, 0, 0, 1]
            for i in q:
                a.append(i)

        if row[6] == "2":
            q = [0, 0, 1, 0]
            for i in q:
                a.append(i)

        if row[6] == "3":
            q = [0, 1, 0, 0]
            for i in q:
                a.append(i)

        if row[6] == "4":
            q = [1, 0, 0, 0]
            for i in q:
                a.append(i)

        if row[7] == "Нет":
            b.append(0)
        if row[7] == "Да":
            b.append(1)

        if row[8] == "ЯСНО":
            q = [0, 0, 0, 1]
            for i in q:
                b.append(i)
        if row[8] == "Затянутое серое небо":
            q = [0, 0, 1, 0]
            for i in q:
                b.append(i)
        if row[8] == "Солнце иногда пробивалось":
            q = [0, 1, 0, 0]
            for i in q:
                b.append(i)
        if row[8] == "Менялась кардинально в течении дня":
            q = [1, 0, 0, 0]
            for i in q:
                b.append(i)
        if row[9] == "Нет":
            q = [0, 0, 0, 1]
            for i in q:
                b.append(i)
        if row[9] == "Дождь и Снег":
            q = [0, 0, 1, 0]
            for i in q:
                b.append(i)
        if row[9] == "Дождь":
            q = [0, 1, 0, 0]
            for i in q:
                b.append(i)
        if row[9] == "СНЕГ!!!":
            q = [1, 0, 0, 0]
            for i in q:
                b.append(i)
        if row[10] == "1":
            q = [0, 0, 0, 1]
            for i in q:
                b.append(i)

        if row[10] == "2":
            q = [0, 0, 1, 0]
            for i in q:
                b.append(i)

        if row[10] == "3":
            q = [0, 1, 0, 0]
            for i in q:
                b.append(i)

        if row[10] == "4":
            q = [1, 0, 0, 0]
            for i in q:
                b.append(i)
        a.append(0)
        b.append(1)
        data.append(a)
        data.append(b)
        if len(a) != 25:
            print(row, a, len(a))
with open('data.txt', 'w') as f:
    f.write(json.dumps(data))
