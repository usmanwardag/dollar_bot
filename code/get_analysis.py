import helper
import logging
import types
import matplotlib.pyplot as plt
import time

def viewOverallBudget(chat_id, bot):
    if not helper.isCategoryBudgetAvailable():
        bot.send_message(chat_id, "No category budget available", reply_markup=types.ReplyKeyboardRemove())
    category_budget = {}
    for cat in helper.spend_categories:
        category_budget[cat] = helper.getCategoryBudgetByCategory(chat_id, cat)
    
    fig, ax = plt.subplots()
    ax.pie(category_budget.values, labels=category_budget.keys, autopct='%1.1f%%')
    random_time = time.time()
    img_name = str(random_time)+".png"
    plt.savefig(img_name)
    bot.send_photo(chat_id, img_name, reply_markup=types.ReplyKeyboardRemove())
