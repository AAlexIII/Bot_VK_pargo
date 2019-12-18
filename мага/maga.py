#!/usr/bin/env python
# -*- coding: utf-8 -*-
from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
import time
from datetime import datetime
import data
import random


def get(vk_session, id_group, vk, text):
    try:
        key_num = 0
        attachment = ''
        # print ('До всего ' + str(time.ctime(time.time())))
        max_num = vk.wall.get(owner_id=id_group, count=0)['count']  # Количество записей
        print("всего ", max_num)
        print('"' + text + '"')
        key_num = vk.wall.search(owner_id=id_group, query=text, count=0)['count']
        # print("Смотрим время после получения количества всех картинок" + str(time.ctime(time.time())))
        num = random.randint(1, key_num)
        # print("Время до получения пикчи" + str(time.ctime(time.time())))
        key = vk.wall.search(owner_id=str(id_group), query=text, count=1, offset=num)['items']
        buf = []
        for element in key:
            buf.append('wall' + str(id_group) + '_' + str(element['id']))
        attachment = ','.join(buf)
        # print("Время после получения пикчи" + str(time.ctime(time.time())))
        return attachment
    except:
        return str('Введи шо нидь другое')


login, password = "89817762764", "мойботномер1"
vk_session = vk_api.VkApi(login, password, app_id=2685278)
vk_session.auth(token_only=True)
mode = 0
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
lis = []
# главный цикл
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.from_user and not (event.from_me):
            print("Что то странное", session_api)
            print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print("Текст сообщения: " + str(event.text))
            print(event.user_id)
            response = event.text.lower()
            name = event.user_id

            if response == "начать" or response == "st" or response == "всё":
                vk_session.method('messages.send', {'user_id': event.user_id,
                                                    'message': 'Напиши "Хочу фильм", если хочешь подборку фильмов \nЕсли хочешь вернуться к переписке, то просто напиши "всё"',
                                                    'random_id': 0})
            elif name in lis:
                if response == "всё":
                    lis.remove(name)
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'ай эм гуд', 'random_id': 0})
                elif (get(vk_session, -69139588, session_api, event.text) == '1'):
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'Введи шо нидь другое', 'random_id': 0})
                else:
                    post = get(vk_session, -69139588, session_api, event.text)
                    print("ccылка: ", post)
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'Держи! Если хочешь закончить, напиши всё',
                                       'random_id': 0, "attachment": post})




            elif response == "привет":
                vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Здаров', 'random_id': 0})
            elif response == "как дела?":
                vk_session.method('messages.send',
                                  {'user_id': event.user_id, 'message': 'Думаю что посмотреть', 'random_id': 0})
            elif response == "да":
                vk_session.method('messages.send', {'user_id': event.user_id,
                                                    'message': 'Напиши "Хочу фильм", если хочешь подборку фильмов \nЕсли хочешь вернуться к переписке, то просто напиши "всё"',
                                                    'random_id': 0})
            elif response == "хочу фильм":
                vk_session.method('messages.send',
                                  {'user_id': event.user_id, 'message': 'Введите ключевое слово', 'random_id': 0})
                # name_film = event.text
                lis.append(name)
                # post = get(vk_session, -69139588, session_api)
                # print("ccылка: ", post)
                # vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Держи, фильм!', 'random_id': 0, "attachment":post})
            else:
                vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Вы написали ' + '"' + str(
                    event.text) + '"' + '\nИ конечно же я не знаю что это такое', 'random_id': 0})

    # time.sleep(1)
