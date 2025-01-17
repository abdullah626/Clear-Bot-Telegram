# -*- coding: utf-8 -*-

import re
import json
import logging


admin_user = ["kaosyancisi"]
token = "5400477700:AAHd52D-OuYmT9kZGK0HBeyaYcBYkbbEfO8"


def get_bad_words():
    with open('bad_words.json', 'r', encoding='utf-8') as f:
        r = json.load(f)
    return r


texts = {
    'start': 'Merhaba, ben istenmeyen içeriği kaldıran bir sohbet botuyum. Yasaklanmış kelimeleri, fotoğrafları, coğrafi konumu, kişileri, belgeleri ve diğer çöpleri silebilirim. İstenmeyen posta koruması ayarlamak da mümkündür. \n\n',
    'help_text': 'Kötü içerikli gönderileri silebilmem için lütfen "Yönetici Yap" bölümünde "Mesajları Silme"  izni verin \n Bütün bunlardan sonra düzgün çalışacağım!!',
    'no_perm': 'Değerli yöneticiler, {0}Yayınları silme iznim yok! \n Lütfen düzeltin!',
    'add_chat': 'Sohbete ekle',
    'add_antispam': 'Spam koruması',
    'add_antispam_tutor': 'Sohbetinizde spam korumasını etkinleştirmek için şunları yapmanız gerekir: \n \n 1) Sohbet ayarlarına gidin \n \n 2) Grubu yönetin \n \n 3) İzinler \n \n 4) Seç öğe - Yavaş mod (burada mesaj göndermek için bir zaman sınırı belirleyebilirsiniz) \n \n Bitti! Sohbetiniz artık korumalı ve güvende.',
    'add_antispam_list': ['spam koruması' , 'spam' , 'koruma' , 'dan koruma' , 'spam koruması'],
    'add_chat_list': ['sohbete ekle' , 'ekle' , 'sohbet'],
    'add_chat_tutor': 'Beni bir sohbete eklemek için aşağıdaki düğmeyi tıklayın ve bir sohbet seçin! \n \n <i>Not: Bir sohbet yöneticisi değilseniz, bir bot ekleyemeyebilirsiniz!</i>',
    'help': 'Yardım',
    'help_list': ['yardım' , 'yardım' , 'destek' ],
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
