import requests
from response_creator import send_message
from flask import Flask, request, json
import vk


app = Flask(__name__)


token = 'a6ce7f02770d6f1c1ccbfc042bd349f9b208338ad1a2314612f5790e51e2f4e085fb6baf45f8f43857f4d'
confirmation_token = '6071d7c2'

@app.route('/', methods=['POST'])
def processing():
    #Распаковываем json из пришедшего POST-запроса
    data = json.loads(request.data)
    #Вконтакте в своих запросах всегда отправляет поле типа
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        session = vk.Session()
        api = vk.API(session, v=5.50)
        user_id = data['object']['user_id']
        user_message = data['object']['body']
        send_message(user_id, user_message)  # отсылает ответ
        # Сообщение о том, что обработка прошла успешно
        return 'ok'

'''
#получаем с LongPoll сервера key, server и ts
token = 'a6ce7f02770d6f1c1ccbfc042bd349f9b208338ad1a2314612f5790e51e2f4e085fb6baf45f8f43857f4d'
data = requests.get('https://api.vk.com/method//messages.getLongPollServer', params={'v': '5.80','access_token': token}).json()['response']


#вечно посылает запросы к LongPoll
while True:
    response = requests.get('https://{server}?act=a_check&key={key}&ts={ts}&wait=25&mode=2&version=2'.format(server=data['server'], key=data['key'], ts=data['ts'])).json()#получаем обновление с LongPoll-a
    updates = response['updates']
    if updates != [] and updates[0][0] == 4:#является ли событие пришедшим сообщением и было бы оно вообще
        user_message = updates[0][5]
        user_id = updates[0][3]
        send_message(user_id, user_message)#отсылает ответ


    data['ts'] = response['ts']#обновление ts-a
'''