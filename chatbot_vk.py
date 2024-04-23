import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime
import time
import random

session = vk_api.VkApi(token = '')
session_api = session.get_api()
longpoll = VkLongPoll(session)

hello_list = ('И тебе привет','Привет', 'Здравствуй')
stiker_id_list = (77717, 51637, 75865, 75868)
music_mess_list = ('музык', 'песн')
music_list = ('277796815_456241204', '277796815_456241201', '277796815_456241199', '277796815_456241195', '277796815_456241194')
film_list = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия',
         'Город грехов', 'Мементо', 'Отступники', 'Деревня']
cats_list = ('210589082_457248005', '210589082_457248003', '210589082_457248002', '210589082_457247952', '210589082_457247921')
while True:
  for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
      print('Сообдение пришло в {}'.format(event.datetime))
      print('Текст сообщения {}'.format(event.text))
      # Задержка при отправке
      response = event.text.lower()
      if event.from_user and not event.from_me:
        time.sleep(random.uniform(0.5, 2.0))
        if response.find('привет') >= 0 or response.find('здравствуй') >= 0:
          session.method('messages.send', {'user_id' : event.user_id, 'message': random.choice(hello_list),
            'random_id': 0} )
          # Стикеры
        elif response.find('как дела') >= 0:
          session.method('messages.send', {'user_id' : event.user_id, 'message': '', 'random_id': 0,
            'sticker_id': random.choice(stiker_id_list)} )
        elif response.find('фильм') >= 0:
          session.method('messages.send', {'user_id': event.user_id, 'message': random.choice(film_list),
            'random_id': 0})
        elif response.find('кот') >= 0:

          session.method('messages.send', {'user_id': event.user_id, 'message':'',
            'random_id': 0,'attachment': f'photo-{random.choice(cats_list)}'})
          # Медиа файлы
        else:
          for el in music_mess_list :
            if response.find(el)  >= 0:
              session.method('messages.send',
                {'user_id': event.user_id, 'message': '', 'random_id': 0, 'attachment': f'audio{random.choice(music_list)}'})


