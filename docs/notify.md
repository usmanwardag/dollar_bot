# About DollarSplitBot's code.py file
notify.py is is for a program that helps users manage their budgets and sends notifications when they exceed their budget for a specific category. 

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/shonilbhide/dollar_bot/blob/main/code/notify.py)

# Code Description
## Functions
- notify(chat_id, cat, amount): This function sends a notification on Telegram when the user exceeds their budget for a specific category. It takes three arguments:
chat_id: The user's Telegram chat ID, which helps the program send the notification to the correct user.
cat: The category for which the budget is exceeded (e.g., "Groceries" or "Transportation").
amount: The amount by which the budget is exceeded.
This function reads some configuration data from a file (specifically, an "api_token"), which is required to send the Telegram notification. Then, it formats a message to inform the user that they've exceeded their budget for a particular category and sends it to the user on Telegram.

# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /budget into the telegram bot.
                                                                                                                 
                                                                                                                 
                                                                                                                 
