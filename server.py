import vk_api.vk_api
import random
from numpy import array
import json
import sqlite3
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType

import MY_FIRST_II as M


class Server:

    def __init__(self, api_token, group_id, server_name: str = "Empty"):
        # Даем серверу имя
        self.server_name = server_name

        # Для Long Poll
        self.vk = vk_api.VkApi(token=api_token)

        # Для использоания Long Poll API
        self.long_poll = VkBotLongPoll(self.vk, group_id, wait=20)

        # Для вызова методов vk_api
        self.vk_api = self.vk.get_api()

    def send_msg(self, idp, send_id=51101228):
        """
        Отправка сообщения через метод messages.send
        :param send_id: vk id пользователя, который получит сообщение
        :param message: содержимое отправляемого письма
        :return: None
        """
        m = 'https://vk.com/id' + str(idp)
        self.vk_api.messages.send(peer_id=send_id,
                                  message=m, random_id=random.randint(1, 999999))


def start(self):
    with open('data.txt') as f:
        data = f.read()
    data = array(json.loads(data))
    X, Y = data[:, 0:24], data[:, 24]
    u = UU(X.shape[1])
    u.add(20)
    u.add(20)
    u.add(7)
    u.train(X, Y)

    mus_ans = ["РОК", 'ПОП', "Русский РЭП", "Классическую"]
    par_ans = ['1', '2', '3', '4']
    znak_ans = ["Рак, Скорпион, Рыбы", "Овен, Лев, Стрелец", "Близнецы, Весы, Водолей", "Телец, Дева, Козерог"]
    fipm_ans = ["ФЭиФ", "ФИПМ", "ФУ", "Другой хороший факультет"]
    priv = ['ку', 'хай', 'прив', 'привет', 'hi', 'здравствуй']
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    for event in self.long_poll.listen():  # Слушаем сервер
        if event.type == VkBotEventType.MESSAGE_NEW:

            username = self.get_user_name(event.object.from_id)
            peer = event.object.peer_id
            txt = str(event.object.text)
            uu_name = ''
            ker_name = ""
            fix = 'Настроить'
            fill = 'Ввести данные'
            me = 'Узнать данные'
            I_want_help = 'Помочь'
            kolvo_par = 'Кол-во пар'
            musik = 'Предпочитаемую музыку'
            fipm = 'Факультет'
            znak = 'Знак'

            cursor.execute("""SELECT muslo, zod, fak, parn FROM good WHERE ID = :l""", {'l': peer})
            d = cursor.fetchone()
            ready = True
            for i in d:
                if i == '':
                    ready = False
                    break
            cursor.execute("""SELECT ID FROM good""")
            ids = cursor.fetchone()
            if peer not in ids:
                cursor.execute("""INSERT INTO good
                                VALUES (:l , '', '','', '','No')""", {'l': peer})
                conn.commit()

            if txt in priv:
                self.sms(peer, f"{username}, Здравствуй!", k=give_klav(situation=1))

            elif txt == 'Начать' or txt == 'Готово':
                self.sms(peer, 'Доступные функции можно найти на стене', k=give_klav(situation=1))

            elif txt == fill:
                self.sms(peer, 'Что вы хотите заполнить?', k=give_klav(situation=11))

            elif txt == fix:
                self.sms(peer, 'Пора что-то менять, что хочешь изменить?')
            elif txt == znak:
                self.sms(peer, 'Выберите свой знак зодиака', k=give_klav(situation=2))
            elif txt == musik:
                self.sms(peer, 'Выберите предпочитаемую музыку', k=give_klav(situation=4))
            elif txt == fipm:
                self.sms(peer, 'Выбери свой факультет', k=give_klav(situation=5))
            elif txt == kolvo_par:
                self.sms(peer, 'Сколько сегодня пар', k=give_klav(situation=3))

            elif txt in mus_ans:
                cursor.execute("UPDATE good SET muslo = :a WHERE ID = :l", {'l': peer, 'a': txt})
                conn.commit()
                self.sms(peer, 'ОК', k=give_klav(situation=11))
            elif txt in par_ans:
                cursor.execute("UPDATE good SET parn = :a WHERE ID = :l", {'l': peer, 'a': txt})
                conn.commit()
                self.sms(peer, 'ОК', k=give_klav(situation=11))
            elif txt in znak_ans:
                cursor.execute("UPDATE good SET zod = :a WHERE ID = :l", {'l': peer, 'a': txt})
                conn.commit()
                self.sms(peer, 'ОК', k=give_klav(situation=11))
            elif txt in fipm_ans:
                cursor.execute("UPDATE good SET fak = :a WHERE ID = :l", {'l': peer, 'a': txt})
                conn.commit()
                self.sms(peer, 'ОК', k=give_klav(situation=11))

            elif txt == I_want_help:
                self.sms(peer, 'Пройдите опрос https://forms.gle/op1eaYcdUWzoE3Sz9')

            elif txt == me:
                cursor.execute("""SELECT muslo, zod, fak, parn FROM good WHERE ID = :l""", {'l': peer})
                d = cursor.fetchone()
                self.sms(peer, f'Музыка {d[0]}\nЗнак {d[1]}\nФкультет {d[2]}\nКол-во пар {d[3]}')

            # else:
            #   if event.object.id > 0:
            #        self.sms(peer, 'Я только учусь, данная команда мне не понятна. Чему мне стоит научиться?')

            # muslo = я есть
            # zod = погода
            # fak = осадки
            if txt == uu_name:
                if ready:
                    what = []
                    cursor.execute("""SELECT muslo, zod, fak, parn FROM good WHERE ID = :l""", {'l': peer})
                    d = cursor.fetchone()
                    cursor.execute("""SELECT muslo, zod, fak FROM good WHERE ID = 000""")
                    dd = cursor.fetchone()
                    for i in d[:3]:
                        q = ans_to_ziro(i)
                        for j in q:
                            what.append(j)
                    for i in dd:
                        q = ans_to_ziro(i)
                        for j in q:
                            what.append(j)
                    q = ans_to_ziro(d[3])
                    for j in q:
                        what.append(j)
                    self.sms(peer, u.say(what))
                else:
                    self.sms(peer, 'Ещё не все данные заполнены')
            elif txt == ker_name:
                if ready:
                    print()
                    # self.sms(peer, u.say(what))

                else:
                    self.sms(peer, 'Ещё не все данные заполнены')
            # self.sms(peer, f"{username},R получил ваше сообщение!")


def sms(self, peer_id, message, k=give_klav(situation=1)):
    # str(json.dumps(({"buttons": [], "one_time": True})))
    self.vk_api.messages.send(peer_id=peer_id, message=message, random_id=random.randint(1, 999999), keyboard=k)


def get_user_name(self, user_id):
    """ Получаем имя пользователя"""
    return self.vk_api.users.get(user_id=user_id)[0]['first_name']
