# -*- coding: utf-8 -*-
import telebot
import pickle
import os


bot = telebot.TeleBot('1570485407:AAETRt2q3eUW2pSZKYswseD2Fdv1UY571WE')
keyboard0 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard0.row('Вопрос 2', 'Вопрос 3', 'Вопрос 4', '->')
keyboard01 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard01.row('Вопрос 5', 'Вопрос 6', 'Вопрос 7', '-->')
keyboard02 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard02.row('Вопрос 8', 'Вопрос 9', 'Вопрос 10', '--->')
keyboard03 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard03.row('Проверить результаты', 'Сбросить результаты')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Начать тест')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row('Вопрос 1 :9', 'Вопрос 1 :15', 'Вопрос 1 :12')
keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard3.row('Вопрос 2 :19', 'Вопрос 2 :10', 'Вопрос 2 :14')
keyboard4 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard4.row('Вопрос 3 :37', 'Вопрос 3 :13', 'Вопрос 3 :11')
keyboard5 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard5.row('Вопрос 4 :93', 'Вопрос 4 :19', 'Вопрос 4 :40')
keyboard6 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard6.row('Вопрос 5 :9', 'Вопрос 5 :3', 'Вопрос 5 :1')
keyboard7 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard7.row('Вопрос 6 :14', 'Вопрос 6 :15', 'Вопрос 6 :8')
keyboard8 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard8.row('Вопрос 7 :110', 'Вопрос 7 :156', 'Вопрос 7 :122')
keyboard9 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard9.row('Вопрос 8 :9', 'Вопрос 8 :33', 'Вопрос 8 :12')
keyboard10 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard10.row('Вопрос 9 :90', 'Вопрос 9 :130', 'Вопрос 9 :120')
keyboard11 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard11.row('Вопрос 10 :6', 'Вопрос 10 :13', 'Вопрос 10 :12')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Вас приветствует IqTestBot', reply_markup=keyboard1)
    
@bot.message_handler(content_types=['text'])
def send_text(message):
    
    if message.text == '->':
        bot.send_message(message.chat.id, 'Ок', reply_markup=keyboard01)
    if message.text == '-->':
        bot.send_message(message.chat.id, 'Ок', reply_markup=keyboard02)
    if message.text == '--->':
        bot.send_message(message.chat.id, 'Ок', reply_markup=keyboard03)
    #Вопрос 1
    if message.text == 'Начать тест':
        bot.send_message(message.chat.id, 'Сумма двух чисел равна 15, а их разность 3. Найдите большее число.', reply_markup=keyboard2)
    elif message.text == "Вопрос 1 :9":
        with open(str(message.chat.id), 'wb') as bd:
            temp11212 = 1
            pickle.dump(temp11212, bd)
        bot.send_message(message.chat.id, 'Ответ верен!', reply_markup=keyboard0)
    elif message.text == "Вопрос 1 :15":        
        bot.send_message(message.chat.id, 'Ответ неверный', reply_markup=keyboard0)
    elif message.text == 'Вопрос 1 :12':        
        bot.send_message(message.chat.id, 'Ответ неверный', reply_markup=keyboard0)
    #Вопрос 2
    if message.text == 'Вопрос 2':
        bot.send_message(message.chat.id, 'Одно из чисел в два раза больше другого. Найдите меньшее из чисел, если их сумма равна 30', reply_markup=keyboard3)
    elif message.text == "Вопрос 2 :10":
        with open(str(message.chat.id), 'rb') as bd:
            data_new = pickle.load(bd)
            data_new = data_new + 1
        with open(str(message.chat.id), 'wb') as bd:
            pickle.dump(data_new, bd)
        bot.send_message(message.chat.id, 'Ответ верен!', reply_markup=keyboard0)
    elif message.text == "Вопрос 2 :19":
        bot.send_message(message.chat.id, 'Ответ неверный', reply_markup=keyboard0)
    elif message.text == 'Вопрос 2 :14':
        bot.send_message(message.chat.id, 'Ответ неверный', reply_markup=keyboard0)
    #Вопрос 3
    if message.text == 'Вопрос 3':
        bot.send_message(message.chat.id, 'Дочь младше папы на 26 лет, а вместе им 48 лет. Определите возраст папы', reply_markup=keyboard4)
    elif message.text == "Вопрос 3 :37" :
        with open(str(message.chat.id), 'rb') as bd:
            data_new = pickle.load(bd)
            data_new = data_new + 1
        with open(str(message.chat.id), 'wb') as bd:
            pickle.dump(data_new, bd)
        bot.send_message(message.chat.id, 'Ответ верен!', reply_markup=keyboard0)
    elif message.text == "Вопрос 3 :13":
        bot.send_message(message.chat.id, 'Ответ неверный', reply_markup=keyboard0)
    elif message.text == 'Вопрос 3 :11':
        bot.send_message(message.chat.id, 'Ответ неверный', reply_markup=keyboard0)
    #Вопрос 4
    if message.text == 'Вопрос 4':
        bot.send_message(message.chat.id, 'Определите расстояние пройденное лодкой за 2 часа по течению реки, если скорость реки 2 км/ч, собственная скорость лодки 18км/ч.', reply_markup=keyboard5)
    elif message.text == "Вопрос 4 :40":
        with open(str(message.chat.id), 'rb') as bd:
            data_new = pickle.load(bd)
            data_new = data_new + 1
        with open(str(message.chat.id), 'wb') as bd:
            pickle.dump(data_new, bd)
        bot.send_message(message.chat.id, 'Ответ верен!', reply_markup=keyboard0)
    elif message.text == "Вопрос 4 :19":
        bot.send_message(message.chat.id, 'Ответ неверный', reply_markup=keyboard0)
    elif message.text == 'Вопрос 4 :93':
        bot.send_message(message.chat.id, 'Ответ неверный', reply_markup=keyboard0)
    #Вопрос 5
    if message.text == 'Вопрос 5':
        bot.send_message(message.chat.id, 'Скорость лодки по течению 23 км/ч, против течени 17 км/ч. Определите скорость течения.', reply_markup=keyboard6)
    elif message.text == "Вопрос 5 :3":
        with open(str(message.chat.id), 'rb') as bd:
            data_new = pickle.load(bd)
            data_new = data_new + 1
        with open(str(message.chat.id), 'wb') as bd:
            pickle.dump(data_new, bd)
        bot.send_message(message.chat.id, 'Ответ верен!', reply_markup=keyboard0)
    elif message.text == "Вопрос 5 :9":
        bot.send_message(message.chat.id, 'Ответ неверный', reply_markup=keyboard0)
    elif message.text == 'Вопрос 5 :1':
        bot.send_message(message.chat.id, 'Ответ принят', reply_markup=keyboard0)

    #Вопрос 6
    if message.text == 'Вопрос 6':
        bot.send_message(message.chat.id, 'Одна труба заполняет бассей за 12 минут, а вторая за 24 минут. За сколько минут наполнится бассейн, если будут работать обе трубы одновременно?', reply_markup=keyboard7)
    elif message.text == "Вопрос 6 :8":
        with open(str(message.chat.id), 'rb') as bd:
            data_new = pickle.load(bd)
            data_new = data_new + 1
        with open(str(message.chat.id), 'wb') as bd:
            pickle.dump(data_new, bd)
        bot.send_message(message.chat.id, 'Ответ верен!', reply_markup=keyboard0)
    elif message.text == "Вопрос 6 :14":
        bot.send_message(message.chat.id, 'Ответ неверный', reply_markup=keyboard0)
    elif message.text == "Вопрос 6 :15":
        bot.send_message(message.chat.id, 'Ответ неверный', reply_markup=keyboard0)
    #Вопрос 7
    if message.text == 'Вопрос 7':
        bot.send_message(message.chat.id, 'Мотоциклист и велосипедист выехали одновременно навстречу друг другу со скоростью 40 и 15 км/ч соответственно. Через два часа они встретились. Определите какое было расстояние между ними перврначально.', reply_markup=keyboard8)
    elif message.text == "Вопрос 7 :110":
        with open(str(message.chat.id), 'rb') as bd:
            data_new = pickle.load(bd)
            data_new = data_new + 1
        with open(str(message.chat.id), 'wb') as bd:
            pickle.dump(data_new, bd)
        bot.send_message(message.chat.id, 'Ответ верен!', reply_markup=keyboard0)
    elif message.text == "Вопрос 7 :156":
        bot.send_message(message.chat.id, 'Ответ неверный', reply_markup=keyboard0)
    elif message.text == 'Вопрос 7 :122':
        bot.send_message(message.chat.id, 'Ответ неверный', reply_markup=keyboard0)
    #Вопрос 8
    if message.text == 'Вопрос 8':
        bot.send_message(message.chat.id, 'Два пешехода вышли одновременно в одном направлении со скоростью 5 и 6 км/ч. Определите расстояние между ними через 3 часа движения.', reply_markup=keyboard9)
    elif message.text == "Вопрос 8 :33":
        with open(str(message.chat.id), 'rb') as bd:
            data_new = pickle.load(bd)
            data_new = data_new + 1
        with open(str(message.chat.id), 'wb') as bd:
            pickle.dump(data_new, bd)
        bot.send_message(message.chat.id, 'Ответ верен!', reply_markup=keyboard0)
    elif message.text == "Вопрос 8 :9":
        bot.send_message(message.chat.id, 'Ответ неверный', reply_markup=keyboard0)
    elif message.text == 'Вопрос 8 :12':
                bot.send_message(message.chat.id, 'Ответ неверный', reply_markup=keyboard0)
    #Вопрос 9
    if message.text == 'Вопрос 9':
        bot.send_message(message.chat.id, 'Найдите площадь прямоугольника, если его длина 12 м, а ширина на 2 м меньше.', reply_markup=keyboard10) 
    elif message.text == "Вопрос 9 :120":
        with open(str(message.chat.id), 'rb') as bd:
            data_new = pickle.load(bd)
            data_new = data_new + 1
        with open(str(message.chat.id), 'wb') as bd:
            pickle.dump(data_new, bd)
        bot.send_message(message.chat.id, 'Ответ верен!', reply_markup=keyboard0)   
    elif message.text == "Вопрос 1 :130":
        bot.send_message(message.chat.id, 'Ответ неверный', reply_markup=keyboard0)
    elif message.text == 'Вопрос 9 :90':
        bot.send_message(message.chat.id, 'Ответ неверный', reply_markup=keyboard0)
    #Вопрос 10
    if message.text == 'Вопрос 10':
        bot.send_message(message.chat.id, 'Найдите сторону квадрата, у которого площадь равна площади прямоугольника со сторонами 4 и 9 см', reply_markup=keyboard11)
    elif message.text == "Вопрос 10 :6":
        with open(str(message.chat.id), 'rb') as bd:
            data_new = pickle.load(bd)
            data_new = data_new + 1
        with open(str(message.chat.id), 'wb') as bd:
            pickle.dump(data_new, bd)
        bot.send_message(message.chat.id, 'Ответ верен!', reply_markup=keyboard0)  
    elif message.text == "Вопрос 10 :13":    
        bot.send_message(message.chat.id, 'Ответ неверный', reply_markup=keyboard0)
    elif message.text == 'Вопрос 10 :12':
        bot.send_message(message.chat.id, 'Ответ неверный', reply_markup=keyboard0)

    elif  message.text == 'Проверить результаты':
        try :
            with open(str(message.chat.id), 'rb') as bd:
                data_new = pickle.load(bd)

            q = str(data_new) + '/10'
            ot.send_message(message.chat.id, q, reply_markup=keyboard0)
        except FileNotFoundError:
            bot.send_message(message.chat.id, '0/10', reply_markup=keyboard1)
    elif message.text == 'Сбросить результаты':
        os.remove(str(message.chat.id))
        bot.send_message(message.chat.id, 'Результаты сброшены', reply_markup=keyboard1)
bot.polling()