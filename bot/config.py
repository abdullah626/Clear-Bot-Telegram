# -*- coding: utf-8 -*-

import re
import json
import logging


admin_user = ["por0vos1k"]
token = "1426362013:AAEHULtj5Spt4CzJA3XTmh_J2NzrkbyyQ4o"


def get_bad_words():
    with open('bad_words.json', 'r', encoding='utf-8') as f:
        r = json.load(f)
    return r


texts = {
    'start': 'Здравствуйте, я - бот, убирающий нежелательный контент в чате. Могу удалять запрещенные слова, фото, геолокацию, контакты, документы и прочий мусор. Также имеется возможность поставить защиту от спама. \n\n',
    'help_text': 'Для того, чтобы я смог удалять сообщения с плохим содержанием, выдайте мне права на "Удаление сообщений" при "Сделать администратором"\nПосле всех проделанный действий я буду работать корректно!',
    'no_perm': 'Дорогие админы, {0}у меня нет прав на удаление сообщений!\nИсправьте пожалуйста!',
    'add_chat': 'Добавить в чат',
    'add_antispam': 'Защита от спама',
    'add_antispam_tutor': 'Для того, чтобы подключить защиту от спама в вашем чате - вам необходимо:\n\n1) Зайти в настройки чата\n\n2) Управление группой\n\n3) Разрешения\n\n4) Выбрать пункт - Медленный режим (там вы можете указать ограничение на отправку сообщений по времени)\n\nГотово! Теперь ваш чат защищен и находится в безопасности.',
    'add_antispam_list': ['защита от спама', 'спам', 'защита', 'защита от', 'защита спам'],
    'add_chat_list': ['добавить в чат', 'добавить', 'чат'],
    'add_chat_tutor': 'Чтобы добавить меня в чат, нажмите на кнопку ниже и выберите чат!\n\n<i>Примечание: если вы не администратор чата, возможно не сможете добавить бота!</i>',
    'help': 'Помощь',
    'help_list': ['помощь', 'подмога', 'поддержка'],
    'bad_words': get_bad_words()
}


_log_format = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).(%(lineno)d) - %(message)s"
_log_level = logging.DEBUG
_log_level_file = logging.DEBUG
_log_dir = 'logs'
_log_prefix = 'name'


all_content_types = ['text', 'audio', 'document', 'photo', 'video']
regexp = str.maketrans("", "", "!@#$%^&*_+|+\:;[]{}()<>?,.=\"\\")


emoji_pattern = re.compile(
    "["
    u"\U0001F600-\U0001F64F"
    u"\U0001F300-\U0001F5FF"
    u"\U0001F680-\U0001F6FF"
    u"\U0001F1E0-\U0001F1FF"
    "]+",

    flags=re.UNICODE
)

"""
needs_to_delete = [
    ['Y', 'У'],
    ['а', 'а'],
    ['х', 'x'],
    ['c', 'с'],
    ['o', 'о'],
    ['4', 'ч']
]

# OR

needs_to_delete = (
    # ('EN', 'RU')
    ('E','Е'),
    ('T','Т'),
    ('Y','У'),
    ('U','И'),
    ('O','О'),
    ('P','Р'),
    ('A','А'),
    ('H','Н'),
    ('K','К'),
    ('X','Х'),
    ('C','С'),
    ('B','В'),
    ('n','П'),
    ('M','М'),
    ('3','З'),
    ('0','О')
)

needs_to_delete = (
    'а' => ['а', 'a', '@'],
    'б' => ['б', '6', 'b'],
    'в' => ['в', 'b', 'v'],
    'г' => ['г', 'r', 'g'],
    'д' => ['д', 'd', 'g'],
    'е' => ['е', 'e'],
    'ё' => ['ё', 'е', 'e'],
    'ж' => ['ж', 'zh', '*'],
    'з' => ['з', '3', 'z'],
    'и' => ['и', 'u', 'i'],
    'й' => ['й', 'u', 'y', 'i'],
    'к' => ['к', 'k', 'i{', '|{'],
    'л' => ['л', 'l', 'ji'],
    'м' => ['м', 'm'],
    'н' => ['н', 'h', 'n'],
    'о' => ['о', 'o', '0'],
    'п' => ['п', 'n', 'p'],
    'р' => ['р', 'r', 'p'],
    'с' => ['с', 'c', 's'],
    'т' => ['т', 'm', 't'],
    'у' => ['у', 'y', 'u'],
    'ф' => ['ф', 'f'],
    'х' => ['х', 'x', 'h', 'к', 'k', '}{'],
    'ц' => ['ц', 'c', 'u,'],
    'ч' => ['ч', 'ch'],
    'ш' => ['ш', 'sh'],
    'щ' => ['щ', 'sch'],
    'ь' => ['ь', 'b'],
    'ы' => ['ы', 'bi'],
    'ъ' => ['ъ'],
    'э' => ['э', 'е', 'e'],
    'ю' => ['ю', 'io'],
    'я' => ['я', 'ya'],
)

"""
