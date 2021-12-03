#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import telebot
import time
import helper
import edit
import history
import display
import estimate
import delete
import add
import budget
from datetime import datetime
from jproperties import Properties

configs = Properties()

with open('user.properties', 'rb') as read_prop:
    configs.load(read_prop)

api_token = str(configs.get('api_token').data)

bot = telebot.TeleBot(api_token)

telebot.logger.setLevel(logging.INFO)

option = {}

# === Documentation of code.py ===

# Define listener for requests by user
def listener(user_requests):
    """
    listener(user_requests): Takes 1 argument user_requests and logs all user 
    interaction with the bot including all bot commands run and any other issue logs.
    """
    for req in user_requests:
        if(req.content_type == 'text'):
            print("{} name:{} chat_id:{} \nmessage: {}\n".format(
                str(datetime.now()), str(req.chat.first_name), str(req.chat.id), str(req.text)))


bot.set_update_listener(listener)


# defines how the /start and /help commands have to be handled/processed
@bot.message_handler(commands=['start', 'menu'])
def start_and_menu_command(m):
    """
    start_and_menu_command(m): Prints out the the main menu displaying the features that the 
    bot offers and the corresponding commands to be run from the Telegram UI to use these features. 
    Commands used to run this: commands=['start', 'menu']
    """
    helper.read_json()
    global user_list
    chat_id = m.chat.id

    # print('receieved start or menu command.')
    #text_into = "Welcome to the Dollar Bot!"

    text_intro = "Welcome to the Dollar Bot! \n" + \
                 "DollarBot can track all your expenses with simple and easy to use commands :) \n\n" + \
                 "Type /faq or /help to get stated."
                 
    #commands = helper.getCommands()
    #for c in commands:  # generate help text out of the commands dictionary defined at the top
    #    text_intro += "/" + c + ": "
    #    text_intro += commands[c] + "\n\n"
    bot.send_message(chat_id, text_intro)
    return True


# defines how the /new command has to be handled/processed
@bot.message_handler(commands=['add'])
def command_add(message):
    """
    command_add(message) Takes 1 argument message which contains the message from 
    the user along with the chat ID of the user chat. It then calls add.py to run to execute 
    the add functionality. Commands used to run this: commands=['add']
    """
    add.run(message, bot)


# function to fetch expenditure history of the user
@bot.message_handler(commands=['history'])
def command_history(message):
    """
    command_history(message): Takes 1 argument message which contains the message from 
    the user along with the chat ID of the user chat. It then calls history.py to run to execute 
    the add functionality. Commands used to run this: commands=['history']
    """
    history.run(message, bot)


# function to edit date, category or cost of a transaction
@bot.message_handler(commands=['edit'])
def command_edit(message):
    """
    command_edit(message): Takes 1 argument message which contains the message from 
    the user along with the chat ID of the user chat. It then calls edit.py to run to execute 
    the add functionality. Commands used to run this: commands=['edit']
    """
    edit.run(message, bot)


# function to display total expenditure
@bot.message_handler(commands=['display'])
def command_display(message):
    """
    command_display(message): Takes 1 argument message which contains the message from the user 
    along with the chat ID of the user chat. It then calls display.py to run to execute the add functionality. 
    Commands used to run this: commands=['display']
    """
    display.run(message, bot)


# function to estimate future expenditure
@bot.message_handler(commands=['estimate'])
def command_estimate(message):
    estimate.run(message, bot)


# handles "/delete" command
@bot.message_handler(commands=['delete'])
def command_delete(message):
    """
    command_delete(message): Takes 1 argument message which contains the message from the user 
    along with the chat ID of the user chat. It then calls delete.py to run to execute the add functionality.
    Commands used to run this: commands=['display']
    """
    delete.run(message, bot)


@bot.message_handler(commands=['budget'])
def command_budget(message):
    budget.run(message, bot)


# not used
def addUserHistory(chat_id, user_record):
    global user_list
    if(not(str(chat_id) in user_list)):
        user_list[str(chat_id)] = []
    user_list[str(chat_id)].append(user_record)
    return user_list


def main():
    """
    main() The entire bot's execution begins here. It ensure the bot variable begins 
    polling and actively listening for requests from telegram.
    """
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        logging.exception(str(e))
        time.sleep(3)
        print("Connection Timeout")


if __name__ == '__main__':
    main()
