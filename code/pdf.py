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
        print('User-history--> ',user_history)
        
        #Issue 3 - added the if condition - start
        if user_history != None:
        #Issue 3 - added the if condition - end
            message = "Alright. I just created a pdf of your expense history!"
            bot.send_message(chat_id, message)
            fig = plt.figure()
            ax = fig.add_subplot(1, 1, 1)
            top = 0.8
            if len(user_history) == 0:
                plt.text(
                    0.1,
                    top,
                    "No record found!",
                    horizontalalignment="left",
                    verticalalignment="center",
                    transform=ax.transAxes,
                    fontsize=20,
                )
            for rec in user_history:
                date, category, amount = rec.split(",")
                date, time = date.split(" ")
                print(date, category, amount)
                rec_str = f"{amount}$ {category} expense on {date} at {time}"
                plt.text(
                    0,
                    top,
                    rec_str,
                    horizontalalignment="left",
                    verticalalignment="center",
                    transform=ax.transAxes,
                    fontsize=14,
                    bbox=dict(facecolor="red", alpha=0.3),
                )
                top -= 0.15
            plt.axis("off")
            plt.savefig("expense_history.pdf")
            plt.close()
            bot.send_document(chat_id, open("expense_history.pdf", "rb"))
        
        #Issue 3 - added the else condition - start
        else:
            message = "Looks like you have not entered any data yet. Please enter some data and then try creating a pdf."
            bot.send_message(chat_id, message)

            display_text = ""
            commands = helper.getCommands()
            for (
            c
            ) in (
                commands
            ):  # generate help text out of the commands dictionary defined at the top
                display_text += "/" + c + ": "
                display_text += commands[c] + "\n"
            bot.send_message(chat_id, "Please select a menu option from below:")
            bot.send_message(chat_id, display_text)
        #Issue 3 - added the else condition - end

    except Exception as e:
        logging.exception(str(e))
        bot.reply_to(message, "Oops!" + str(e))
