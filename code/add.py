import helper
import logging
from telebot import types
from datetime import datetime

option = {}

# === Documentation of add.py ===

def run(message, bot):
    """
    run(message, bot): This is the main function used to implement the add feature.
    It pop ups a menu on the bot asking the user to choose their expense category,
    after which control is given to post_category_selection(message, bot) for further proccessing.
    It takes 2 arguments for processing - message which is the message from the user,
    and bot which is the telegram bot object from the main code.py function.
    """
    helper.read_json()
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 2
    chat_id = message.chat.id
    expense_history = helper.getUserHistory(chat_id)
    if expense_history:
        recur_msg = bot.send_message(chat_id,"You have previously recorded expenses. Do you want to repeat one of these expenses?(Y/N)")
        bot.register_next_step_handler(recur_msg, record_expense, bot, expense_history)
    else:
        for c in helper.getSpendCategories():
            markup.add(c)
        markup.add("Add new category")
        msg = bot.reply_to(message, "Select Category", reply_markup=markup)
        bot.register_next_step_handler(msg, post_category_selection, bot)

def post_append_spend(message, bot):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 2
    selected_category = message.text
    chat_id = message.chat.id
    allocated_categories = helper.getCategoryBudget(chat_id)
    if selected_category not in allocated_categories.keys():
        helper.updateBudgetCategory(chat_id,selected_category)
    helper.spend_categories.insert(0,selected_category)
    for c in helper.getSpendCategories():
        markup.add(c)
    msg = bot.reply_to(message, "Select Category", reply_markup=markup)
    bot.register_next_step_handler(msg, post_category_selection, bot)

def post_category_selection(message, bot):
    """
    post_category_selection(message, bot): It takes 2 arguments for processing -
    message which is the message from the user, and bot which is the telegram bot object
    from the run(message, bot): function in the add.py file. It requests the user to enter the amount
    they have spent on the expense category chosen and then passes control to
    post_amount_input(message, bot): for further processing.
    """
    try:
        chat_id = message.chat.id
        selected_category = message.text
        if selected_category == "Add new category":
            message1 = bot.send_message(chat_id, "Please enter your category")
            bot.register_next_step_handler(message1, post_append_spend, bot)
        else:
            if selected_category not in helper.getSpendCategories():
                bot.send_message(
                    chat_id, "Invalid", reply_markup=types.ReplyKeyboardRemove()
                )
                raise Exception(
                    'Sorry, I don\'t recognise this category "{}"!'.format(selected_category)
                )
            option[chat_id] = selected_category
            message = bot.send_message(
                chat_id, "How much did you spend on {}? \n(Numeric values only)".format(str(option[chat_id])),)
            bot.register_next_step_handler(message, post_amount_input, bot, selected_category)
    except Exception as e:
        logging.exception(str(e))
        bot.reply_to(message, "Oh no! " + str(e))
        display_text = ""
        commands = helper.getCommands()
        for c in commands:  
            # generate help text out of the commands dictionary defined at the top
            display_text += "/" + c + ": "
            display_text += commands[c] + "\n"
        bot.send_message(chat_id, "Please select a menu option from below:")
        bot.send_message(chat_id, display_text)

def record_expense(message, bot, previous_expenses):
    print("In function to record expense")
    selection = message.text
    print(selection)
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 2
    if selection == "Y" or selection == "y":
        for record in previous_expenses:
            markup.add(record)
        msg = bot.reply_to(message, "Select the expense you want to repeat", reply_markup=markup)
        bot.register_next_step_handler(msg, post_expense_selection, bot)
    else:
        for c in helper.getSpendCategories():
            markup.add(c)
        markup.add("Add new category")
        msg = bot.reply_to(message, "Select Category", reply_markup=markup)
        bot.register_next_step_handler(msg, post_category_selection, bot)

def post_expense_selection(message,bot):
    chat_id = message.chat.id
    expense_record = message.text
    expense_data = expense_record.split(",")
    amount = expense_data[2]
    category = expense_data[1]
    print(amount)
    amount_value = helper.validate_entered_amount(amount)  # validate
    try:
        if amount_value == 0:  # cannot be $0 spending
            raise Exception("Spent amount has to be a non-zero number.")
        date_of_entry = datetime.today().strftime(helper.getDateFormat())
        date_str, category_str, amount_str = (
            str(date_of_entry),
            str(category),
            str(amount_value),
        )
        helper.write_json(
            add_user_record(
                chat_id, "{},{},{}".format(date_str, category_str, amount_str)
            )
        )
        bot.send_message(
            chat_id,
            "The following expenditure has been recorded: You have spent ${} for {} on {}".format(
                amount_str, category_str, date_str
            ),
        )
        helper.display_remaining_budget(message, bot, category)
    except Exception as e:
        logging.exception(str(e))
        bot.reply_to(message, "Oh no. " + str(e))

def post_amount_input(message, bot, selected_category):
    """
    post_amount_input(message, bot): It takes 2 arguments for processing -
    message which is the message from the user, and bot which is the telegram bot
    object from the post_category_selection(message, bot): function in the add.py file.
    It takes the amount entered by the user, validates it with helper.validate() and then
    calls add_user_record to store it.
    """
    try:
        print("---------------------------------------------------")
        chat_id = message.chat.id
        print(chat_id)
        amount_entered = message.text
        print("0000000000000000000000000000000000000000000000000")
        print(amount_entered)
        print(selected_category)
        amount_value = helper.validate_entered_amount(amount_entered)  # validate
        if amount_value == 0:  # cannot be $0 spending
            raise Exception("Spent amount has to be a non-zero number.")

        date_of_entry = datetime.today().strftime(
            helper.getDateFormat())
        date_str, category_str, amount_str = (
            str(date_of_entry),
            str(option[chat_id]),
            str(amount_value),
        )
        helper.write_json(
            add_user_record(
                chat_id, "{},{},{}".format(date_str, category_str, amount_str)
            )
        )
        bot.send_message(
            chat_id,
            "The following expenditure has been recorded: You have spent ${} for {} on {}".format(
                amount_str, category_str, date_str
            ),
        )
        helper.display_remaining_budget(message, bot, selected_category)
    except Exception as e:
        logging.exception(str(e))
        bot.reply_to(message, "Oh no. " + str(e))

def add_user_record(chat_id, record_to_be_added):
    """
    add_user_record(chat_id, record_to_be_added): Takes 2 arguments -
    chat_id or the chat_id of the user's chat, and record_to_be_added which
    is the expense record to be added to the store. It then stores this expense record in the store.
    """
    user_list = helper.read_json()
    print("!" * 5)
    print("before")
    print(user_list)
    print("!" * 5)
    if str(chat_id) not in user_list:
        user_list[str(chat_id)] = helper.createNewUserRecord()

    user_list[str(chat_id)]["data"].append(record_to_be_added)
    print("!" * 5)
    print("after")
    print(user_list)
    print("!" * 5)
    return user_list
