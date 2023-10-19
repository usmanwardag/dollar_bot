'''
This is the main file used to implement the DELETE BUDGET feature.
'''

import logging
import helper
from telebot import types

def run(message, bot):
    chat_id = message.chat.id
    user_list = helper.read_json()

    if str(chat_id) not in user_list:
        bot.send_message(chat_id, "You don't have budget data to delete.")
    else:
        if "budget" in user_list[str(chat_id)]:
            # The 'budget' dictionary exists; you can proceed with deleting it
            user_list[str(chat_id)]["budget"] = {"overall": None, "category": {}}
        else:
            bot.send_message(chat_id, "No budget data to delete.")
                
        helper.write_json(user_list)
        bot.send_message(chat_id, "Budget data deleted successfully.")

    helper.write_json(user_list)
