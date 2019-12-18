import json


def give_klav(situation, uu_name='Гена', ker_name='Оля', I_want_help='Помочь', Who_I='Узнать данные', fill='Ввести данные',
              kolvo_par='Кол-во пар', musik='Предпочитаемую музыку', fipm='Факультет', znak='Знак'):
    if situation == 0:
        allready = {
            "one_time": False,
            "buttons": [
                [{
                    "action": {
                        "type": "text",
                        "payload": "",
                        "label":'Погода'
                    },
                    "color": "positive"
                }],[
                    {
                        "action": {
                            "type": "text",
                            "payload": "",
                            "label": 'Я'
                        },
                        "color": "negative"
                    }],
                [{
                    "action": {
                        "type": "text",
                        "payload": "",
                        "label": 'Осадки'
                    },
                    "color": "primary"
                }],
                [{
                    "action": {
                        "type": "text",
                        "payload": "",
                        "label": Who_I
                    },
                    "color": "primary"
                }], [{
                    "action": {
                        "type": "text",
                        "payload": "",
                        "label": 'Готово'
                    },
                    "color": "secondary"
                }]
            ]}
        allready = json.dumps(allready, ensure_ascii=False).encode('utf-8')
        return str(allready.decode('utf-8'))

    if situation == 10:
        allready = {
            "one_time": False,
            "buttons": [
                [{
                    "action": {
                        "type": "text",
                        "payload": "",
                        "label":"ЯСНО"
                    },
                    "color": "positive"
                }],[
                    {
                        "action": {
                            "type": "text",
                            "payload": "",
                            "label": "Затянутое серое небо"
                        },
                        "color": "negative"
                    }],
                [{
                    "action": {
                        "type": "text",
                        "payload": "",
                        "label": "Солнце иногда пробивалось"
                    },
                    "color": "primary"
                }],
                [{
                    "action": {
                        "type": "text",
                        "payload": "",
                        "label": "Менялась кардинально в течении дня"
                    },
                    "color": "primary"
                }], [{
                    "action": {
                        "type": "text",
                        "payload": "",
                        "label": 'го'
                    },
                    "color": "secondary"
                }]
            ]}
        allready = json.dumps(allready, ensure_ascii=False).encode('utf-8')
        return str(allready.decode('utf-8'))
    if situation == 20:
        allready = {
            "one_time": False,
            "buttons": [
                [{
                    "action": {
                        "type": "text",
                        "payload": "",
                        "label":"Осадков Нет"
                    },
                    "color": "positive"
                }],[
                    {
                        "action": {
                            "type": "text",
                            "payload": "",
                            "label": "Дождь и Снег"
                        },
                        "color": "negative"
                    }],
                [{
                    "action": {
                        "type": "text",
                        "payload": "",
                        "label": 'Дождь'
                    },
                    "color": "primary"
                }],
                [{
                    "action": {
                        "type": "text",
                        "payload": "",
                        "label": "СНЕГ!!!"
                    },
                    "color": "primary"
                }], [{
                    "action": {
                        "type": "text",
                        "payload": "",
                        "label": 'го'
                    },
                    "color": "secondary"
                }]
            ]}
        allready = json.dumps(allready, ensure_ascii=False).encode('utf-8')
        return str(allready.decode('utf-8'))
    if situation == 30:
        allready = {
            "one_time": False,
            "buttons": [
                [{
                    "action": {
                        "type": "text",
                        "payload": "",
                        "label":'Скорее всего'
                    },
                    "color": "positive"
                }],[
                    {
                        "action": {
                            "type": "text",
                            "payload": "",
                            "label": 'Вряд ли'
                        },
                        "color": "negative"
                    }],
                [{
                    "action": {
                        "type": "text",
                        "payload": "",
                        "label": 'Готово'
                    },
                    "color": "primary"
                }],
                [{
                    "action": {
                        "type": "text",
                        "payload": "",
                        "label": Who_I
                    },
                    "color": "primary"
                }], [{
                    "action": {
                        "type": "text",
                        "payload": "",
                        "label": 'го'
                    },
                    "color": "secondary"
                }]
            ]}
        allready = json.dumps(allready, ensure_ascii=False).encode('utf-8')
        return str(allready.decode('utf-8'))
    if situation == 1:
        allready = {
            "one_time": False,
            "buttons": [
                [{
                    "action": {
                        "type": "text",
                        "payload": "",
                        "label": uu_name
                    },
                    "color": "positive"
                },
                    {
                        "action": {
                            "type": "text",
                            "payload": "",
                            "label": ker_name
                        },
                        "color": "negative"
                    }],
                [{
                    "action": {
                        "type": "text",
                        "payload": "",
                        "label": fill
                    },
                    "color": "primary"
                }],
                [{
                    "action": {
                        "type": "text",
                        "payload": "",
                        "label": Who_I
                    },
                    "color": "primary"
                }], [{
                    "action": {
                        "type": "text",
                        "payload": "",
                        "label": I_want_help
                    },
                    "color": "secondary"
                }]
            ]}
        allready = json.dumps(allready, ensure_ascii=False).encode('utf-8')
        return str(allready.decode('utf-8'))
    if situation == 11:
        What_fill = {
            "one_time": False,
            "buttons": [
                [{
                    "action": {
                        "type": "text",
                        "payload": "",
                        "label": znak
                    },
                    "color": "primary"
                }], [
                    {
                        "action": {
                            "type": "text",
                            "payload": "",
                            "label": fipm
                        },
                        "color": "primary"
                    }], [
                    {
                        "action": {
                            "type": "text",
                            "payload": "",
                            "label": kolvo_par
                        },
                        "color": "primary"
                    }], [
                    {
                        "action": {
                            "type": "text",
                            "payload": "",
                            "label": musik
                        },
                        "color": "primary"
                    }], [
                    {
                        "action": {
                            "type": "text",
                            "payload": "",
                            "label": 'Готово'
                        },
                        "color": "secondary"
                    }]]}
        What_fill = json.dumps(What_fill, ensure_ascii=False).encode('utf-8')
        return str(What_fill.decode('utf-8'))

    if situation == 2:
        What_fill = {
            "one_time": False,
            "buttons": [
                [{
                    "action": {
                        "type": "text",
                        "payload": "",
                        "label": "Телец, Дева, Козерог"
                    },
                    "color": "positive"
                }], [
                    {
                        "action": {
                            "type": "text",
                            "payload": "",
                            "label": "Овен, Лев, Стрелец"
                        },
                        "color": "negative"
                    }], [
                    {
                        "action": {
                            "type": "text",
                            "payload": "",
                            "label": "Рак, Скорпион, Рыбы"
                        },
                        "color": "primary"
                    }], [
                    {
                        "action": {
                            "type": "text",
                            "payload": "",
                            "label": "Близнецы, Весы, Водолей"
                        },
                        "color": "secondary"
                    }]]}
        What_fill = json.dumps(What_fill, ensure_ascii=False).encode('utf-8')
        return str(What_fill.decode('utf-8'))
    if situation == 3:
        What_fill = {
            "one_time": False,
            "buttons": [
                [{
                    "action": {
                        "type": "text",
                        "payload": "",
                        "label": "1"
                    },
                    "color": "primary"
                }], [
                    {
                        "action": {
                            "type": "text",
                            "payload": "",
                            "label": "2"
                        },
                        "color": "primary"
                    }], [
                    {
                        "action": {
                            "type": "text",
                            "payload": "",
                            "label": "3"
                        },
                        "color": "primary"
                    }], [
                    {
                        "action": {
                            "type": "text",
                            "payload": "",
                            "label": "4"
                        },
                        "color": "primary"
                    }]]}
        What_fill = json.dumps(What_fill, ensure_ascii=False).encode('utf-8')
        return str(What_fill.decode('utf-8'))

    if situation == 4:
        What_fill = {
            "one_time": False,
            "buttons": [
                [{
                    "action": {
                        "type": "text",
                        "payload": "",
                        "label": "РОК"
                    },
                    "color": "primary"
                }], [
                    {
                        "action": {
                            "type": "text",
                            "payload": "",
                            "label": "ПОП"
                        },
                        "color": "primary"
                    }], [
                    {
                        "action": {
                            "type": "text",
                            "payload": "",
                            "label": "Классическую"
                        },
                        "color": "primary"
                    }], [
                    {
                        "action": {
                            "type": "text",
                            "payload": "",
                            "label": "Русский РЭП"
                        },
                        "color": "primary"
                    }]]}
        What_fill = json.dumps(What_fill, ensure_ascii=False).encode('utf-8')
        return str(What_fill.decode('utf-8'))
    if situation == 5:
        What_fill = {
            "one_time": False,
            "buttons": [
                [{
                    "action": {
                        "type": "text",
                        "payload": "",
                        "label": "ФЭиФ"
                    },
                    "color": "primary"
                }], [
                    {
                        "action": {
                            "type": "text",
                            "payload": "",
                            "label": "ФИПМ"
                        },
                        "color": "primary"
                    }], [
                    {
                        "action": {
                            "type": "text",
                            "payload": "",
                            "label": "ФУ"
                        },
                        "color": "primary"
                    }], [
                    {
                        "action": {
                            "type": "text",
                            "payload": "",
                            "label": "Другой хороший факультет"
                        },
                        "color": "primary"
                    }]]}
        What_fill = json.dumps(What_fill, ensure_ascii=False).encode('utf-8')
        return str(What_fill.decode('utf-8'))


'''
allready = {
    "one_time": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "",
                "label": uu_name
            },
            "color": "positive"
        },
            {
                "action": {
                    "type": "text",
                    "payload": "",
                    "label": ker_name
                },
                "color": "secondary"
            }]]}


who = json.dumps(who, ensure_ascii=False).encode('utf-8')
who = str(who.decode('utf-8'))
No_klav = {"buttons": [], "one_time": True}
ken = json.dumps(ken, ensure_ascii=False).encode('utf-8')
ken = str(ken.decode('utf-8'))
'''
