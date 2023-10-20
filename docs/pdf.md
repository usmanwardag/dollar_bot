# About DollarSplitBot's /pdf Feature
The provided code appears to be part of a Python script designed to create PDF documents based on user input in a chat application, possibly a Telegram bot.

The user can choose a category and add the amount for the budget to be stored in the expense tracker.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/shonilbhide/dollar_bot/blob/main/code/pdf.py)

# Code Description
## Functions

- run(message, bot): This is the main function for implementing the PDF save feature. It reads some data, displays a menu asking the user what kind of PDF they want to generate, and registers a handler for the user's response.

- pdfGeneration(message, bot, user_list, user_history): This function generates PDF documents based on user preferences. Depending on the user's choice, it can generate two types of PDF documents: one showing total expenses categorized, and the other showing who owes whom how much. It uses the matplotlib, tabulate, and fpdf libraries to create these PDFs.

# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /pdf into the telegram bot.
