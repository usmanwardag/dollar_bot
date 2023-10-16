import helper
import logging
from matplotlib import pyplot as plt

#Issue 15 - Added tabulate and fpdf libraries
from tabulate import tabulate
from fpdf import FPDF

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

            #issue 15 - modified the format of pdf document - start
            table_data = [entry.split(',') for entry in user_history]

            # Create a PDF document
            pdf = FPDF()
            pdf.add_page()

            # Set font
            pdf.set_font("helvetica", size=12)

            # Define the table columns
            columns = ["Date & Time", "Category", "Amount"]

            # Create a table and set its properties
            pdf.set_fill_color(135, 206, 235)  # Light blue

            pdf.set_font(family="helvetica",style="B")
            pdf.cell(0, 10, "Expense Report", ln=1, align="C", fill=True)
            pdf.set_fill_color(255, 255, 255)  # White
            pdf.ln()
            pdf.ln()
            # Add table headers
            pdf.set_font("helvetica", size=12, style="B")
            for col in columns:
                pdf.cell(64, 10, col, border=1, align="C", fill=True)
            pdf.ln()

            # Add table data
            pdf.set_font("helvetica", size=10)
            for row in table_data:
                for item in row:
                    pdf.cell(64, 10, item, border=1, align="C", fill=True)
                pdf.ln()

            # Save the PDF
            pdf.output("expense_report.pdf")
            bot.send_document(chat_id, open("expense_report.pdf", "rb"))
            print("PDF generated successfully.")
            #issue 15 - modified the format of pdf document - start
            
        
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
        bot.send_message(message, "Oops!" + str(e))
