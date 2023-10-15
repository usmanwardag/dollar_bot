import helper
import logging
from telebot import types

# Initialize a dictionary to store registered users
registered_users = {}
user_list=helper.read_json()
def register_people(message, bot):
    chat_id = message.chat.id
    if "users" in user_list[str(chat_id)].keys():
        registered_users={chat_id : user_list[str(chat_id)]["users"]}
    else:
        registered_users = {}
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 2
    msg = bot.send_message(chat_id, "Enter the name of the person you want to register:")
    bot.register_next_step_handler(msg, add_person, bot,registered_users)

def add_person(message, bot,registered_users):
    chat_id = message.chat.id
    name = message.text

    # Check if the name is unique for this chat_id
    if chat_id in registered_users and name in registered_users[chat_id]:
        bot.send_message(chat_id, f"{name} is already registered.")
    else:
        if chat_id not in registered_users.keys():
            registered_users[chat_id] = []

        registered_users[chat_id].append(name)

        bot.send_message(chat_id, f"{name} has been registered successfully!")

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.row_width = 2
        markup.add("Register Another Person", "Finish Registration")
        msg = bot.send_message(chat_id, "What would you like to do next?", reply_markup=markup)

        bot.register_next_step_handler(msg, handle_registration_choice, bot,registered_users)

def handle_registration_choice(message, bot,registered_users):
    chat_id = message.chat.id
    choice = message.text

    if choice == "Register Another Person":
        msg = bot.send_message(chat_id, "Enter the name of the person you want to register:")
        bot.register_next_step_handler(msg, add_person, bot,registered_users)
    elif choice == "Finish Registration":
        # Display the names of registered users
        if chat_id in registered_users:
            users = registered_users[chat_id]
            user_list[str(chat_id)]["users"]=users
            helper.write_json(user_list)
            if users:
                bot.send_message(chat_id, "Registered Users:\n" + '\n'.join(registered_users[chat_id]))
            else:
                bot.send_message(chat_id, "No users registered yet.")
    else:
        bot.send_message(chat_id, "Invalid choice. Please select a valid option.")
