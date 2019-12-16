import vk_api.vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

import random
from numpy import array
import json
import sqlite3

from klava import give_klav
from MY_FIRST_II import UU
from what import ans_to_ziro

from keras.models import Sequential, load_model
from sklearn.model_selection import train_test_split


class Server:

    def __init__(self, api_token, group_id, server_name="Empty"):

        # Даем серверу имя
        self.server_name = server_name

        # Для Long Poll
        self.vk = vk_api.VkApi(token=api_token)

        # Для использоания Long Poll API
        self.long_poll = VkBotLongPoll(self.vk, group_id, wait=20)

        # Для вызова методов vk_api
        self.vk_api = self.vk.get_api()
        # vk = vk_api.VkApi(token=token)

        # Работа с сообщениями
        # longpoll = VkLongPoll(vk)

    def send_msg(self, send_id=51101228):
        """
        Отправка сообщения через метод messages.send
        :param send_id: vk id пользователя, который получит сообщение
        :param message: содержимое отправляемого письма
        :return: None
        """
        m = 'https://vk.com/id'
        self.vk_api.messages.send(peer_id=send_id,
                                  message=m, random_id=random.randint(1, 999999))

    def start(self):

        with open('data.txt') as f:
            data = f.read()
        data = array(json.loads(data))

        X, Y = data[:, 0:24], data[:, 24]
        u = UU(X.shape[1])
        u.add(12)
        u.add(19)
        u.add(9)
        u.train(X, Y, 100)

        model = load_model("weights.h5")

        self.send_msg()

        mus_ans = ["РОК", 'ПОП', "Русский РЭП", "Классическую"]
        par_ans = ['1', '2', '3', '4']
        znak_ans = ["Рак, Скорпион, Рыбы", "Овен, Лев, Стрелец", "Близнецы, Весы, Водолей", "Телец, Дева, Козерог"]
        fipm_ans = ["ФЭиФ", "ФИПМ", "ФУ", "Другой хороший факультет"]
        priv = ['ку', 'хай', 'прив', 'привет', 'hi', 'здравствуй']

        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()
        for event in self.long_poll.listen():
            print(6)  # Слушаем сервер
            if event.type == VkBotEventType.MESSAGE_NEW:
                print(7)

                username = self.get_user_name(event.object.from_id)
                peer = event.object.peer_id
                txt = str(event.object.text)
                uu_name = 'Гена'
                ker_name = "Оля"
                fix = 'Настроить'
                fill = 'Ввести данные'
                me = 'Узнать данные'
                I_want_help = 'Помочь'
                kolvo_par = 'Кол-во пар'
                musik = 'Предпочитаемую музыку'
                fipm = 'Факультет'
                znak = 'Знак'

                cursor.execute("""SELECT ID FROM good""")
                ids = cursor.fetchone()
                if peer not in ids:
                    cursor.execute("""INSERT INTO good
                                    VALUES (:l , '', '','', '','No')""", {'l': peer})
                    conn.commit()

                cursor.execute("""SELECT muslo, zod, fak, parn FROM good WHERE ID = :l""", {'l': peer})
                d = cursor.fetchone()
                ready = True
                for i in d:
                    if i == '':
                        ready = False
                        break

                if txt in priv:
                    self.sms(peer, f"{username}, Здравствуй!", k=give_klav(situation=1))

                if txt == 'Начать' or txt == 'Ку' or txt == 'ку':
                    self.sms(peer, f'''Привет, {username}, я бот предсказатель, в моей голове 2 личности
                                    Гена - ребёнок создателя, отлично справляется с тестовыми вариантами
                                    Оля - училась в Гарварде, по технологии глубокого обучения, её результат в тестах 88%
                                    Выбери одного и он\она ответит нужно ли идти на пары

                                    Чтобы получить результат тебе нужно заполнить свои данные.
                                    Ты всегда можешь посмотреть свои данные и изменить их''', k=give_klav(situation=1))
                elif txt == 'Готово':
                    self.sms(peer, f"{username}, а ты молодец!\n Не забудь проверить свои данные!",
                             k=give_klav(situation=1))

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
                    self.sms(peer, 'Сколько завтра пар?', k=give_klav(situation=3))

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
                    self.sms(peer,
                             'Пройдя опрос, вы поможете мне лучше прогнозировать ответы forms.gle/op1eaYcdUWzoE3Sz9')

                elif txt == me:
                    cursor.execute("""SELECT muslo, zod, fak, parn FROM good WHERE ID = :l""", {'l': peer})
                    d = cursor.fetchone()
                    self.sms(peer,
                             f'О тебе:\nПредпочитаемая Музыка {d[0]}\nЗнак зодиака {d[1]}\nТвой факультет {d[2]}\nПар завтра {d[3]}')
                    cursor.execute("""SELECT muslo, zod, fak FROM good WHERE ID = 000""")
                    d = cursor.fetchone()
                    self.sms(peer, f'О завтрешнем дне:\nВстреча с Александром {d[0]}\nПогода {d[1]}\nОсадки {d[2]}')

                # else:
                #   if event.object.id > 0:
                #        self.sms(peer, 'Я только учусь, данная команда мне не понятна. Чему мне стоит научиться?')

                # muslo = я есть
                # zod = погода
                # fak = осадки
                elif txt == uu_name:
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
                        self.sms(peer, f'На пары стоит с ходить с вероятностью {self.make_norm(u.say(what))}')
                    else:
                        self.sms(peer, 'Ещё не все данные заполнены')
                elif txt == ker_name:
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

                        self.sms(peer,
                                 f'На пары стоит с ходить с вероятностью {self.make_norm(model.predict(array([what])))}')

                    else:
                        self.sms(peer, 'Ещё не все данные заполнены')
                # self.sms(peer, f"{username},R получил ваше сообщение!")
        conn.close()

    def sms(self, peer_id, message, k=give_klav(situation=1)):
        # str(json.dumps(({"buttons": [], "one_time": True})))
        self.vk_api.messages.send(peer_id=peer_id, message=message, random_id=random.randint(1, 999999), keyboard=k)

    def make_norm(self, a):
        t = a[0][0]
        print(t)
        if t < 0.005:
            t = '100% точно стоит'
        elif t > 0.99:
            t = '0% \n Стоит сходить, но точно не на пары'
        else:
            t = str(int(round(t, 2) * 100)) + '%'
        return t

    def get_user_name(self, user_id):
        """ Получаем имя пользователя"""
        return self.vk_api.users.get(user_id=user_id)[0]['first_name']
