import helper
import logging
from telebot import types
import matplotlib.pyplot as plt
import time
import numpy as np

def viewOverallBudget(chat_id, bot):
    if not helper.isCategoryBudgetAvailable(chat_id):
        bot.send_message(chat_id, "No category budget available", reply_markup=types.ReplyKeyboardRemove())
        return
    category_budget = {}
    for cat in helper.spend_categories:
        if helper.isCategoryBudgetByCategoryAvailable(chat_id, cat):
            category_budget[cat] = helper.getCategoryBudgetByCategory(chat_id, cat)
    
    _, ax = plt.subplots()
    ax.pie(category_budget.values(), labels=category_budget.keys(), autopct='%1.1f%%')
    ax.set_title("Budget split")
    random_time = time.time()
    img_name = str(random_time)+".png"
    plt.savefig(img_name)
    bot.send_photo(chat_id, photo=open(img_name, 'rb'), reply_markup=types.ReplyKeyboardRemove())

def viewSpendWise(chat_id, bot):
    category_spend = {}
    for cat in helper.spend_categories:
        spend = helper.calculate_total_spendings_for_cateogory_chat_id(chat_id,cat)
        if spend != 0:
            category_spend[cat] = spend

    if category_spend.keys() == None:
        bot.send_message(chat_id, "No category spend available", reply_markup=types.ReplyKeyboardRemove())
        return
    
    _, ax = plt.subplots()
    ax.pie(category_spend.values(), labels=category_spend.keys(), autopct='%1.1f%%')
    ax.set_title("Category-wise spend")
    random_time = time.time()
    img_name = str(random_time)+".png"
    plt.savefig(img_name)
    bot.send_photo(chat_id, photo=open(img_name, 'rb'), reply_markup=types.ReplyKeyboardRemove())

def viewRemaining(chat_id, bot):
    if not helper.isCategoryBudgetAvailable(chat_id):
        bot.send_message(chat_id, "No category budget available", reply_markup=types.ReplyKeyboardRemove())
        return

    category_spend_percent = {}
    for cat in helper.spend_categories:
        if helper.isCategoryBudgetByCategoryAvailable(chat_id, cat):
            percent = helper.calculateRemainingCateogryBudgetPercent(chat_id, cat)
            category_spend_percent[cat] = percent
    
    labels = tuple(category_spend_percent.keys())
    print(labels)
    type(labels)

    remaining_val_list = [100 - x for x in list(category_spend_percent.values())]

    weight_counts = {
        "Used": list(category_spend_percent.values()),
        "Remaining": remaining_val_list,
    }
    print(weight_counts)

    width = 0.5

    _, ax = plt.subplots()
    # simply impossible to submit anything other than an np ndarray here
    # matplotlib simply fails to recognize shape of any other "array-like"
    #object
    bottom = np.zeros(len(list(category_spend_percent.values())))

    for boolean, weight_count in weight_counts.items():
        print(boolean, weight_count)
        ax.bar(labels, weight_count, width, label=boolean, bottom=bottom)
        bottom += weight_count

    ax.set_title("Category-wise budget consumed")
    plt.xlabel("Categories")
    plt.ylabel("Percentage")
    ax.legend(loc="upper right")

    random_time = time.time()
    img_name = str(random_time)+".png"
    plt.savefig(img_name)
    bot.send_photo(chat_id, photo=open(img_name, 'rb'), reply_markup=types.ReplyKeyboardRemove())

def viewHistory(chat_id, bot):
    if not helper.getUserHistory(chat_id):
        bot.send_message(chat_id, "No history available", reply_markup=types.ReplyKeyboardRemove())
        return
    
    cat_spend_dict = helper.getUserHistoryDateExpense(chat_id)

    plt.plot(cat_spend_dict.keys(), cat_spend_dict.values(), marker='o')
    plt.title("Time-series of expenses")
    plt.xlabel("Time")
    plt.ylabel("Expense")
    random_time = time.time()
    img_name = str(random_time)+".png"
    plt.savefig(img_name)
    bot.send_photo(chat_id, photo=open(img_name, 'rb'), reply_markup=types.ReplyKeyboardRemove())