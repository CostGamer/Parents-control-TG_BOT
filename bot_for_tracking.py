import psutil
import time
import telebot


def get_process_time(process_name):  # Function that tracking the APP ON
    for proc in psutil.process_iter(['name', 'create_time']):
        if proc.info['name'] == process_name:
            return time.time() - proc.info['create_time']
    return None


def close_process(process_name):  # Function that terminate definite APP
    for proc in psutil.process_iter():
        if proc.name() == process_name:
            proc.terminate()


# Your TG_BOT TOKEN
bot = telebot.TeleBot('TOKEN')


# Handling the start command
@bot.message_handler(commands=['start', 'restart'])
def start(message):
    chat_id = message.chat.id
    # First message
    bot.send_message(chat_id, "Hi, let's track or close some APPs")

    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2)
    btn1 = telebot.types.KeyboardButton('Track')
    btn2 = telebot.types.KeyboardButton('Close')
    keyboard.row(btn1, btn2)
    bot.send_message(
        chat_id, "Below you see the buttons⬇️\nWhat do you like to do?", reply_markup=keyboard)
    bot.register_next_step_handler(message, click)


def click(message):
    chat_id = message.chat.id
    if message.text == 'Track':
        list_of_aps_for_track(message)
    elif message.text == 'Close':
        list_of_aps_for_close(message)


def list_of_aps_for_track(message):
    chat_id = message.chat.id

    markup = telebot.types.InlineKeyboardMarkup()   # Keyboard for track buttons
    butt1 = telebot.types.InlineKeyboardButton(
        'Google', callback_data='Google')
    butt2 = telebot.types.InlineKeyboardButton(
        'Telegram', callback_data='Telegram')
    butt3 = telebot.types.InlineKeyboardButton(
        'Yandex', callback_data='Yandex')
    butt4 = telebot.types.InlineKeyboardButton(
        'WeChat', callback_data='WeChat')

    markup.add(butt1, butt2)
    markup.add(butt3, butt4)
    bot.send_message(chat_id, 'Choose the APP to Track', reply_markup=markup)


def list_of_aps_for_close(message):
    chat_id = message.chat.id

    markup = telebot.types.InlineKeyboardMarkup()   # Keyboard for close buttons
    butt1 = telebot.types.InlineKeyboardButton(
        'Close Google', callback_data='Close_Google')
    butt2 = telebot.types.InlineKeyboardButton(
        'Close Telegram', callback_data='Close_Telegram')
    butt3 = telebot.types.InlineKeyboardButton(
        'Close Yandex', callback_data='Close_Yandex')
    butt4 = telebot.types.InlineKeyboardButton(
        'Close WeChat', callback_data='Close_WeChat')

    markup.add(butt1, butt2)
    markup.add(butt3, butt4)
    bot.send_message(chat_id, 'Choose the APP to Track', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback(callback):
    chat_id = callback.message.chat.id
    if callback.data == 'Google':  # Track the Google APP
        process_name = "chrome.exe"     # The name of the process
        uptime = get_process_time(process_name)
        if uptime is not None:
            bot.send_message(chat_id, f'''The running time for Google is {
                int(uptime/60)} minutes and {
                int(uptime % 60)} seconds''')
        else:
            bot.send_message(chat_id, f'''The Google is not run''')
        bot.send_message(chat_id, f'''To check different APPs - click to the APPs button
For closing the APP you should restart the bot (command /restart)''')

    elif callback.data == 'Telegram':  # Track the Telegram APP
        process_name = "Telegram.exe"     # The name of the process
        uptime = get_process_time(process_name)
        if uptime is not None:
            bot.send_message(chat_id, f'''The running time for Telegram is {
                int(uptime/60)} minutes and {
                int(uptime % 60)} seconds''')
        else:
            bot.send_message(chat_id, f'''The Telegram is not run''')
        bot.send_message(chat_id, f'''To check different APPs - click to the APPs button
For closing the APP you should restart the bot (command /track_or_close)''')

    elif callback.data == 'Yandex':  # Track the Yandex APP
        process_name = "browser.exe"     # The name of the process
        uptime = get_process_time(process_name)
        if uptime is not None:
            bot.send_message(chat_id, f'''The running time for Yandex is {
                int(uptime/60)} minutes and {
                int(uptime % 60)} seconds''')
        else:
            bot.send_message(chat_id, f'''The Yandex is not run''')
        bot.send_message(chat_id, f'''To check different APPs - click to the APPs button
For closing the APP you should restart the bot (command /track_or_close)''')

    elif callback.data == 'WeChat':  # Track the WeChat APP
        process_name = "WeChat.exe"     # The name of the process
        uptime = get_process_time(process_name)
        if uptime is not None:
            bot.send_message(chat_id, f'''The running time for WeChat is {
                int(uptime/60)} minutes and {
                int(uptime % 60)} seconds''')
        else:
            bot.send_message(chat_id, f'''The WeChat is not run''')
        bot.send_message(chat_id, f'''To check different APPs - click to the APPs button
For closing the APP you should restart the bot (command /track_or_close)''')

    elif callback.data == 'Close_Google':   # Close the Google APP
        close_process('chrome.exe')
        bot.send_message(chat_id, f'''The Google was successfully closed''')

    elif callback.data == 'Close_Telegram':     # Close the Telegram APP
        close_process('Telegram.exe')
        bot.send_message(chat_id, f'''The Telegram was successfully closed''')

    elif callback.data == 'Close_Yandex':   # Close the Yandex APP
        close_process('browser.exe')
        bot.send_message(chat_id, f'''The Yandex was successfully closed''')

    elif callback.data == 'Close_WeChat':   # Close the WeChat APP
        close_process('WeChat.exe')
        bot.send_message(chat_id, f'''The WeChat was successfully closed''')


bot.polling()
