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
        message = 'Alright. I just created a pdf of your expense history!'
        bot.send_message(chat_id, message)
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        top = 0.8
        if len(user_history) == 0:
            plt.text(0.1, top, 'No record found!', horizontalalignment='left',
                     verticalalignment='center', transform=ax.transAxes, fontsize=20)
        for rec in user_history:
            date, category, amount = rec.split(',')
            date, time = date.split(' ')
            print(date, category, amount)
            rec_str = f'{amount}$ {category} expense on {date} at {time}'
            plt.text(0, top, rec_str, horizontalalignment='left',
                     verticalalignment='center', transform=ax.transAxes, fontsize=14,
                     bbox=dict(facecolor='red', alpha=0.3))
            top -= 0.15
        plt.axis('off')
        plt.savefig('expense_history.pdf')
        plt.close()
        bot.send_document(chat_id, open('expense_history.pdf', 'rb'))
    except Exception as e:
        logging.exception(str(e))
        bot.reply_to(message, "Oops!" + str(e))
