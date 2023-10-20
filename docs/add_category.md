# About DollarSplitBot's /add_category Feature
This feature allows users to tell the chatbot what kind of expenses they want to track. If they choose a category that already exists, they are informed. If they choose a new category, it is added to their list of expense categories, and the chatbot starts tracking their spending for that category. This helps users keep a record of their expenses in different categories, like food, transportation, or shopping.

Currently we have the following expense categories set by default:

- Food
- Groceries
- Utilities
- Transport
- Shopping
- Miscellaneous


# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/shonilbhide/dollar_bot/blob/main/code/add_category.py)

# Code Description
## Functions

1. run(message, bot):
This function is the entry point for the "add" feature. When a user interacts with the bot, it pops up a menu asking the user to select an expense category. The function takes two arguments:
     - `message`: This is a message from the user, containing their selection.
     - `bot`: A reference to the Telegram bot object.

2. post_append_spend(message, bot):
This function is called after the user selects an expense category. It takes two arguments:
     - `message`: The message from the user containing the selected category.
     - `bot`: A reference to the Telegram bot object.

The function then processes the user's choice. If the selected category already exists, it informs the user. If it doesn't exist, it adds the category to the list of expense categories and stores it in the user's expense tracker.

# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /add_category into the telegram bot.

Sho, [13-10-2023 15:04]
/add_category

testbot_SSAR, [13-10-2023 15:13]
Please enter your category

Sho, [13-10-2023 15:13]
vehicle

testbot_SSAR, [13-10-2023 15:13]
The following category has been added: vehicle