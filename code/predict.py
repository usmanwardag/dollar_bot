# average expenses by max no. of days between expenes, extrapolate to one month
# minimum 2 expenses in category to predict category wise
# minimum 2 expenses overall to predict overall budget
# factor in savings after extrapolation

import time
import helper
import logging
from telebot import types

# === Documentation of predict.py ===


def run(message, bot):
    """
    run(message, bot): This is the main function used to implement the predict feature.
    It takes 2 arguments for processing - message which is the message from the user, and
    bot which is the telegram bot object from the main code.py function.
    """
    helper.read_json()
    chat_id = message.chat.id
    history = helper.getUserHistory(chat_id)
    if history is None or len(history) < 2:
        bot.send_message(
            chat_id, "Sorry, you do not have sufficient spending records to predict a future budget"
        )
    else:
        bot.register_next_step_handler(message, predict_total, bot)


def predict_total(message, bot):
    """
    estimate_total(message, bot): It takes 2 arguments for processing - message which is the message
    from the user, and bot which is the telegram bot object from the run(message, bot): function in the
    same file. This function loads the user's data using the helper file's getUserHistory(chat_id) method.
    After this, depending on the option user has chosen on the UI, it calls the calculate_estimate(queryResult,
    days_to_estimate): to process the queried data to return to the user after which it finally passes the data to
    the UI for the user to view.
    """
    try:
        chat_id = message.chat.id

        history = helper.getUserHistory(chat_id)

        bot.send_message(chat_id, "Hold on! Calculating...")
        # show the bot "typing" (max. 5 secs)
        bot.send_chat_action(chat_id, "typing")
        time.sleep(0.5)
        budget = helper.getOverallBudget(chat_id)

    except Exception as e:
        logging.exception(str(e))
        bot.reply_to(message, str(e))


def predict_category_spending(history):
    """
    predict_category_spending(history): Takes 1 arguments for processing - history
    which is the record of all expenses from a category. It parses the history
    and turns it into a form suitable for display on the UI by the user.
    """
    #todo

def predict_overall_spending(history):
    """
    predict_overall_spending(history): Takes 1 arguments for processing - history
    which is the record of all expenses of the user. It parses the history
    and turns it into a form suitable for display on the UI by the user.
    """
    #todo
