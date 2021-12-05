import helper
import logging
from matplotlib import pyplot as plt

# === Documentation of pdf.py ===

def run(message, bot):
    """
    run(message, bot): This is the main function used to implement the pdf save feature. 
    """
    try:
        helper.read_json()
        chat_id = message.chat.id
        user_history = helper.getUserHistory(chat_id)
        spend_total_str = ""
        #if user_history is None:
        #    raise Exception("Sorry! No spending records found!")
        spend_total_str = "Here is your spending history : \nDATE, CATEGORY, AMOUNT\n----------------------\n"
        if len(user_history) == 0:
            spend_total_str = "Sorry! No spending records found!"
        else:
            for rec in user_history:
                spend_total_str += str(rec) + "\n"
        #bot.send_message(chat_id, spend_total_str)
        message = 'Alright. I just created a pdf of your expense history!'
        bot.send_message(chat_id, message)
        plt.figure()
        plt.savefig('expense_history.pdf')
        bot.send_document(chat_id, open('expense_history.pdf', 'rb'))
    except Exception as e:
        logging.exception(str(e))
        bot.reply_to(message, "Oops!" + str(e))
