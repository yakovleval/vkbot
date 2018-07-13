import requests
from response_creator import send_message



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