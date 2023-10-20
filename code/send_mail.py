import helper
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from fpdf import FPDF

user_emails = {}

# === Documentation of add.py ===
def run(message, bot):
    helper.read_json()
    chat_id = message.chat.id
    message1 = bot.send_message(chat_id, "Please enter the email address")
    bot.register_next_step_handler(message1, add_emails, bot)

def add_emails(message, bot):
    """
    add_emails(message, bot):
    Takes 2 arguments - message (a message received from the user) and bot (the chatbot instance).
    This function extracts the email from the user's message and associates it with the user's chat ID in the user_emails dictionary.
    It can also perform email validation. If the email is invalid, it sends a message to the user to enter a valid email.
    Finally, the user is notified that their email has been recorded and is asked if they want to send an email to the provided address.
    """
    chat_id = message.chat.id
    email = message.text
    # Assuming you want to store the email address in the user_emails dictionary
    user_emails[chat_id] = email

    # You can also validate the email address if needed
    if not is_valid_email(email):
        bot.send_message(chat_id, "Invalid email address. Please enter a valid email.")
        return

    # Notify the user that their email address has been recorded
    choice = bot.send_message(chat_id, f"Thank you for providing your email. Do you want to send email to {email}? Y/N")
    bot.register_next_step_handler(choice, send_email, bot)

# Example of a basic email validation function (you can expand this)
def is_valid_email(email):
    """
    is_valid_email(email):
    Takes one argument - email (the email address to be validated).
    This function checks if the provided email address is in a valid format using a regular expression pattern.
    If the email is in a valid format, it returns True; otherwise, it returns False.
    """
    import re
    email_pattern = r'^\S+@\S+\.\S+$'
    return re.match(email_pattern, email) is not None
    
def send_email(choice, bot):
    """
    send_email(choice, bot):
    Takes two arguments - choice (user's choice of sending an email) and bot (the chatbot instance).
    If the user's choice is 'Y' or 'y', this function sets up a Gmail SMTP connection, composes and sends emails to all users stored in the user_emails dictionary.
    It uses a Gmail account for sending emails, and the email content is based on data obtained from the 'helper.read_json()' function.
    After sending the emails, it closes the SMTP connection.
    """
    if str(choice.text) == "Y" or str(choice.text) == "y":
        # Set up the Gmail API
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587  # Port for TLS
        smtp_username = 'csc510group32@gmail.com'
        smtp_password = 'hqrx opxo lviu mubb'  

        # Create an SMTP connection
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)


        # Compose and send emails to all users
        for chat_id, email in user_emails.items():
            # Create a MIME message with a subject
            subject = "Calculated Owings"
            message_body = format_text_data(helper.read_json())
            message = MIMEMultipart()
            message['From'] = smtp_username
            message['To'] = email
            message['Subject'] = subject
            message.attach(MIMEText(message_body, 'plain'))

            # Send the email
            server.sendmail(smtp_username, email, message.as_string()) 

        # Close the SMTP connection
        server.quit()



def format_text_data(user_list):
    """
    format_text_data(user_list):
    Takes one argument - user_list (a dictionary containing details about owed and owing amounts among users).
    This function formats the provided user_list data into a text representation with detailed information on who owes and is owed money.
    The formatted text data is enclosed in triple backticks for use in Markdown or code block formatting.
    The resulting text data is returned as a string.
    """
    text_data = "```\n"

    for user, details in user_list.items():
        for user_name in details["users"]:
            gets_back_amount = round(details['owed'][user_name], 2)
            text_data += f"{user_name} gets back {gets_back_amount} dollars.\n"

            gives_to_list = list(details["owing"][user_name].keys())
            gives_amount_list = list(details["owing"][user_name].values())

            if not gives_to_list:
                text_data += f"{user_name} gives to no one.\n"
            else:
                for i in range(len(gives_to_list)):
                    gives_to_entry = gives_to_list[i]
                    gives_amount_entry = round(gives_amount_list[i], 2)
                    text_data += f"{user_name} gives {gives_amount_entry} dollars to {gives_to_entry}.\n"

    text_data += "```"
    return text_data












