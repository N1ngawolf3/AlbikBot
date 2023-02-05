import telebot
from keyboard_buttons import KButtons
from messages import Messages
import openpyxl
from DB import add_client,add_fio

def main():
    bot = telebot.TeleBot('5914996329:AAEaeSAmyoCQXS73wTPIRIsGTKZMzjvk4cg')

    @bot.message_handler(commands=['admin'])
    def dodge_admin(message):
        pass
    #todo добавить сообщения для всех пользователей

    @bot.message_handler(commands=['start'])
    def reg_start(message):
        bot.send_message(message.from_user.id,Messages.welcome_message)
        bot.send_message(message.from_user.id,'Укажите свой номер телефона')
        bot.register_next_step_handler(message,reg_add_FIO)

    def reg_add_FIO(message):
        add_client(message.from_user.id, message.from_user.username, message.text)
        bot.send_message(message.from_user.id, 'Укажите свой ФИО(полностью)')
        bot.register_next_step_handler(message,reg_end)

    def reg_end(message):
        add_fio(message.from_user.id,message.text)
        bot.send_message(message.from_user.id,Messages.registration_end,
                         reply_markup=KButtons.welcome_buttons())

    @bot.message_handler(content_types=['text'])
    def text(message):
        if message.text == 'Инструкция': bot.send_message(message.from_user.id,Messages.instruction)
        if message.text == 'Поддержка' : bot.send_message(message.from_user.id,Messages.support)
        if message.text == 'Калькулятор Цен': bot.send_message(message.from_user.id,Messages.price) #todo сделать нормальный калькулятор
        if message.text == 'Оформить заказ': bot.send_message(message.from_user.id,Messages.order)



    bot.polling(none_stop=True,interval=0)


if __name__ == '__main__':
    main()