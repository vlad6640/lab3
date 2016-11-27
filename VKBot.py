import vk
import time
import datetime
import weather

print('VKBot')

session = vk.Session('dd2d90af4b8f3d9f22a049147035730ba278e7da933831e771858df85b7d5871db15447016faf002ed777')

api = vk.API(session)

while(True):
    try:
        messages = api.messages.get()
    except:
        continue
    for m in messages[1:]:
        if m['read_state'] == 0:
            uid = m['uid']
            user_name = api.users.get(user_ids=uid)[0]['first_name']
            try:
                chat_id = m['chat_id']
            except:
                chat_id = 0
            if chat_id > 0:
                uid = 0
            text = m['body']
            text = text.lower()
            text = text.replace(' ', '')
        date_time_string = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')

        if text == 'помощь':
            api.messages.send(uid=uid, chat_id=chat_id, message=date_time_string +
                                                      '\n>VKBot v0.1 \n>Разработал vlad6640')

        if text == 'привет':
            api.messages.send(uid=uid, chat_id=chat_id, message=date_time_string + '\n\nЗдравствуй, ' + user_name + '!!!')

        if text[0:7:1] == "погодав":
            api.messages.send(uid=uid, chat_id=chat_id, message=str(date_time_string + '\n\n' +
                                                                    weather.weather_now(text)))


        api.messages.markAsRead(message_ids=m['mid'])

time.sleep(3)
