from server import Server
# Получаем из config.py наш api-token
from config import vk_api_token

while True:
    try:
        server1 = Server(vk_api_token, 189842227, "server1")
        print(1)
        server1.start()
    except:
        pass
'''
server1 = Server(vk_api_token, 189842227, "server1")
print(1)
server1.start()
'''
