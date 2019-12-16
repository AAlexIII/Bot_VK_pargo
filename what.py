def ans_to_ziro(ans):
    for i in [1]:
        if ans == "РОК":
            q = [0, 0, 0, 1]
            return q
        if ans == "ПОП":
            q = [0, 0, 1, 0]
            return q

        if ans == "Русский РЭП":
            q = [0, 1, 0, 0]
            return q
        if ans == "Классическую":
            q = [1, 0, 0, 0]
            return q

        if ans == "Рак, Скорпион, Рыбы":
            q = [0, 0, 0, 1]
            return q

        if ans == "Близнецы, Весы, Водолей":
            q = [0, 0, 1, 0]
            return q

        if ans == "Овен, Лев, Стрелец":
            q = [0, 1, 0, 0]
            return q

        if ans == "Телец, Дева, Козерог":
            q = [1, 0, 0, 0]
            return q

        if ans == "ФЭиФ":
            q = [1, 0, 0]
            return q

        if ans == "ФИПМ":
            q = [0, 1, 0]
            return q

        if (ans == "ФY") or (ans == "Другой хороший факультет"):
            q = [0, 0, 1]
            return q

        if ans == "Скорее всего":
            q = [1]
            return q

        if ans == "Вряд ли":
            q = [0]
            return q

        if ans == "ЯСНО":
            q = [0, 0, 0, 1]
            return q

        if ans == "Затянутое серое небо":
            q = [0, 0, 1, 0]
            return q

        if ans == "Солнце иногда пробивалось":
            q = [0, 1, 0, 0]
            return q

        if ans == "Менялась кардинально в течении дня":
            q = [1, 0, 0, 0]
            return q

        if ans == "Осадков Нет":
            q = [0, 0, 0, 1]
            return q

        if ans == "Дождь и Снег":
            q = [0, 0, 1, 0]
            return q

        if ans == "Дождь":
            q = [0, 1, 0, 0]
            return q

        if ans == "СНЕГ!!!":
            q = [1, 0, 0, 0]
            return q

        if ans == "1":
            q = [0, 0, 0, 1]
            return q

        if ans == "2":
            q = [0, 0, 1, 0]
            return q

        if ans == "3":
            q = [0, 1, 0, 0]
            return q

        if ans == "4":
            q = [1, 0, 0, 0]
            return q
