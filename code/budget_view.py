import helper
import logging

def run(message, bot):
    try:
        chat_id = message.chat.id
        if helper.isOverallBudgetAvailable(chat_id):
            display_overall_budget(message, bot)
        elif helper.isCategoryBudgetAvailable(chat_id):
            display_category_budget(message, bot)
        else:
            raise Exception(
                "Budget does not exist. Use " + helper.getBudgetOptions()["update"] + " option to add/update the budget"
            )
    except Exception as e:
        helper.throw_exception(e, message, bot, logging)

def display_overall_budget(message, bot):
    chat_id = message.chat.id
    data = helper.getOverallBudget(chat_id)
    if data is not None:
        data = str(data)  # Convert the float to a string
    bot.send_message(chat_id, "Overall Budget: $" + str(data))


def display_category_budget(message, bot):
    chat_id = message.chat.id
    data = helper.getCategoryBudget(chat_id)
    if data is not None:
        formatted_data = "\n".join([f"{category}: ${budget}" for category, budget in data.items()])
        bot.send_message(chat_id, "Category-Wise Budgets:\n" + formatted_data)
