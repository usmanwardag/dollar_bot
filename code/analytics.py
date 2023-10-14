import helper
import logging
from telebot import types
import get_analysis

def run(message, bot):
    """
    run(message, bot): This is the main function used to implement the budget feature.
    It pop ups a menu on the bot asking the user to choose to view analytics
    after which control is given to post_operation_selection(message, bot) for further proccessing.
    It takes 2 arguments for processing - message which is the message from the user, and bot which is the
    telegram bot object from the main code.py function.
    """
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    options = helper.getAnalyticsOptions()
    markup.row_width = 2
    for c in options.values():
        markup.add(c)
    msg = bot.reply_to(message, "Select the type of analysis (grouped by category):", reply_markup=markup)
    bot.register_next_step_handler(msg, post_operation_selection, bot)

def post_operation_selection(message, bot):
    """
    post_operation_selection(message, bot): It takes 2 arguments for processing - message which
    is the message from the user, and bot which is the telegram bot object from the
    run(message, bot): function in the analytics.py file. Depending on the action chosen by the user,
    it passes on control to the corresponding functions which are all located in different files.
    """
    try:
        chat_id = message.chat.id
        op = message.text
        options = helper.getAnalyticsOptions()
        if op not in options.values():
            bot.send_message(
                chat_id, "Invalid", reply_markup=types.ReplyKeyboardRemove()
            )
            raise Exception('Sorry I don\'t recognise this operation "{}"!'.format(op))
        if op == options["overall"]:
            get_analysis.viewOverallBudget(chat_id, bot)
        elif op == options["spend"]:
            get_analysis.viewSpendWise(chat_id, bot)
        elif op == options["remaining"]:
            get_analysis.viewRemaining(chat_id, bot)
    except Exception as e:
        helper.throw_exception(e, message, bot, logging)