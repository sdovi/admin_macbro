import telebot

import re
from config import TOKEN
from time import sleep
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
import requests

token = 'http://127.0.0.1:8000/api/get'
bot = telebot.TeleBot(TOKEN)

user_info = {
    "title": None,
    "name": None,
    "phone": None
}
text = {
    'welcome': "Привет, Выберите язык,\n"
               "Салом, тилни танланг"
}

btn = {
    "btn_uz": KeyboardButton(text="Uz"),
    "btn_ru": KeyboardButton(text="Русс"),
}

inline_btn = dict({})  # инлайн кнопки
actions = dict({})  # ответы бота


@bot.message_handler(commands=['start'])
def start(message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(btn['btn_uz'], btn['btn_ru'])
    bot.send_message(message.chat.id, text['welcome'], reply_markup=kb)


@bot.message_handler(content_types=['text'])
def main_func(message):
    if message.text == "Uz" or message.text == "Русс":
        language_down(message)


def language_down(message):  # выбор языка
    global text01, btn1, actions1, inline_btn1
    if message.text == "Uz":
        from text_uz import text01, btn1, actions1, inline_btn1
        user_info["title"] = message.chat.id
    elif message.text == "Русс":
        from text_ru import text01, btn1, actions1, inline_btn1
        user_info["title"] = message.chat.id

    text.update(text01)
    btn.update(btn1)
    actions.update(actions1)
    inline_btn.update(inline_btn1)
    kb = ReplyKeyboardMarkup(resize_keyboard=True)  # отправка запросов
    kb.add(btn['btn1'])
    user_choice = bot.send_message(message.chat.id, text['actions'], reply_markup=kb)
    bot.register_next_step_handler(user_choice, regist)


def regist(message):
    if message.text == text["text1"]:
        user_choise = bot.send_message(message.chat.id, text["text2"], reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(user_choise, regist_name)


def regist_name(message):
    user_info["name"] = message.text
    kna = ReplyKeyboardMarkup(resize_keyboard=True)  # принимает имя
    kna.add(btn['btn3'])
    bot.send_message(message.chat.id, text["text3"], reply_markup=ReplyKeyboardRemove())
    user_choise = bot.send_message(message.chat.id, text["text4"], reply_markup=kna)
    bot.register_next_step_handler(user_choise, regist_phone)


def regist_phone(message):
    if message.content_type == 'contact':
        user_info['phone'] = int(message.contact.phone_number)  # принимает номер
        bot.send_message(message.chat.id, text["text5"], reply_markup=ReplyKeyboardRemove())
        kb = InlineKeyboardMarkup(row_width=1)
        for x, i in inline_btn.items():
            kb.add(i)

        requests.post(token, json=user_info)

        sleep(1)
        bot.send_message(message.chat.id, text["text6"])
        bot.send_message(message.chat.id, text["caruz"], reply_markup=kb)
    elif len(message.text) == 12 and re.match(r'^(998)[\d]{9}$', message.text):
        user_info['phone'] = message.text  # принимает номер
        bot.send_message(message.chat.id, text["text5"], reply_markup=ReplyKeyboardRemove())
        kb = InlineKeyboardMarkup(row_width=1)
        for x, i in inline_btn.items():
            kb.add(i)
        sleep(1)
        bot.send_message(message.chat.id, text["text6"])
        bot.send_message(message.chat.id, text["caruz"], reply_markup=kb)
    else:
        bot.send_message(message.chat.id, text["text7"])


bot.polling()
