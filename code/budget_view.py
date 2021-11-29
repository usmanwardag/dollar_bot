import graphing
import helper
import logging
import os


def run(message, bot):
    try:
        print("here")
        chat_id = message.chat.id
        if helper.isOverallBudgetAvailable(chat_id):
            display_overall_budget(message, bot)
        elif helper.isCategoryBudgetAvailable(chat_id):
            display_category_budget(message, bot)
        else:
            raise Exception('Budget does not exist. Use ' + helper.getBudgetOptions()
                            ['update'] + ' option to add/update the budget')
    except Exception as e:
        helper.throw_exception(e, message, bot, logging)


def display_overall_budget(message, bot):
    chat_id = message.chat.id
    data = helper.getOverallBudget(chat_id)
    bot.send_message(chat_id, 'Overall Budget: $' + data)


def display_category_budget(message, bot):
    chat_id = message.chat.id
    data = helper.getCategoryBudget(chat_id)
    graphing.viewBudget(data)
    bot.send_photo(chat_id, photo=open('budget.png', 'rb'))
    os.remove('budget.png')
