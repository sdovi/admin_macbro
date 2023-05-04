import telebot
from config import TOKEN
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton
import requests

bot = telebot.TeleBot(TOKEN)
token_ipad = 'http://127.0.0.1:8000/ipadipad'
btn = {
    'btn1': KeyboardButton(text="Айпад📲"),
    'btn4': KeyboardButton(text="Айфон📲"),
    'btn2': KeyboardButton(text="Изменение данных"),
    'btn3': KeyboardButton(text="Добавление данных"),
    'btn5': KeyboardButton(text="Просмотр данных"),

}
ipads = {
    'ID': 0,
    'title': None,
    'price': 0,
}
ipad = {
    'ID': 0,
}
ipad_title = {
    'title': None,
}

ipad_price = {
    'price': 0,
}
btn_inline = {
    "btn_inl_1": KeyboardButton(text='Изменить название айпада', ),
    "btn_inl_2": KeyboardButton(text='Изменить цену айпада', ),
}


@bot.message_handler(commands=['start'])
def start(message):
    a = ReplyKeyboardMarkup(resize_keyboard=True)
    a.add(btn['btn2'], btn['btn3'], btn['btn5'])
    next = bot.send_message(message.chat.id, 'Приветствую, выберите пункт', reply_markup=a)
    bot.register_next_step_handler(next, path)


@bot.message_handler(content_types=['text'])
def path(message):
    if message.text == 'Изменение данных':
        next = bot.send_message(message.chat.id, 'Напишите ID Которое хотите поменять',
                                reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(next, pathid)
    if message.text == 'Добавление данных':
        a = ReplyKeyboardMarkup(resize_keyboard=True)
        a.add(btn['btn1'], btn['btn4'])
        next = bot.send_message(message.chat.id, 'Выберите что хотите добавить', reply_markup=a)
        bot.register_next_step_handler(next, sect_info_ipad_id)

    if message.text == 'Просмотр данных':
        info = requests.get(token_ipad).json()
        kb = InlineKeyboardMarkup()
        for i in info:
            a = InlineKeyboardButton(text=f'{i["title"]}',  callback_data=i['ID'])
            kb.add(a)


        bot.send_message(message.chat.id, 'Какой именно?', reply_markup=kb)


def sect_info_ipad_id(message):
    if message.text == 'Айпад📲':
        next = bot.send_message(message.chat.id, 'Придумайте айди для айпада', reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(next, sect_info_ipad_title)


def sect_info_ipad_title(message):
    ipads['ID'] = message.text
    bot.send_message(message.chat.id, 'Отлично')
    next = bot.send_message(message.chat.id, 'Теперь придумайте название для айпада', )
    bot.register_next_step_handler(next, sect_info_ipad_price)


def sect_info_ipad_price(message):
    ipads['title'] = message.text
    bot.send_message(message.chat.id, 'Отлично')
    next = bot.send_message(message.chat.id, 'Теперь придумайте Цену для айпада', )
    bot.register_next_step_handler(next, sect_info_ipad_end)


def sect_info_ipad_end(message):
    ipads['price'] = message.text
    requests.post(token_ipad, json=ipads)
    bot.send_message(message.chat.id, 'Готово👍', )


def pathid(message):
    ipad['ID'] = message.text
    bot.send_message(message.chat.id, 'Отлично')
    a = ReplyKeyboardMarkup(resize_keyboard=True)
    a.add(btn_inline['btn_inl_1'], btn_inline['btn_inl_2'], )
    next = bot.send_message(message.chat.id, 'Выберите что хотите изменить', reply_markup=a)
    bot.register_next_step_handler(next, info)


def info(message):
    if message.text == 'Изменить название айпада':
        next = bot.send_message(message.chat.id, 'Введите название айпада', reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(next, info_ipad)

    if message.text == 'Изменить цену айпада':
        next = bot.send_message(message.chat.id, 'Введите цену айпада', reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(next, info_price)


def info_ipad(message):
    ipad_title['title'] = message.text
    requests.patch(f'http://127.0.0.1:8000/ipadipad/{ipad["ID"]}/', json=ipad_title)
    a = ReplyKeyboardMarkup(resize_keyboard=True)
    a.add(btn['btn1'])
    next = bot.send_message(message.chat.id, 'Успешно изменен\n'
                                             'Выберите что хотите изменить', reply_markup=a)
    bot.register_next_step_handler(next, path)


def info_price(message):
    ipad_price['price'] = message.text
    requests.patch(f'http://127.0.0.1:8000/ipadipad/{ipad["ID"]}/', json=ipad_price)
    a = ReplyKeyboardMarkup(resize_keyboard=True)
    a.add(btn['btn1'])
    next = bot.send_message(message.chat.id, 'Успешно изменен\n'
                                             'Выберите что хотите изменить', reply_markup=a)
    bot.register_next_step_handler(next, path)



@bot.callback_query_handler(func=lambda call: True)
def call(call):
    req = call.data.split('_')[0]
    dss = requests.get(f'http://127.0.0.1:8000/ipadipad').json()
    print(dss)




bot.polling()
