from telebot import types

class KButtons():
    def welcome_buttons():
        keyboard =  types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add('Оформить заказ','Калькулятор Цен')
        keyboard.add('Инструкция')
        keyboard.add('Поддержка')
        return keyboard