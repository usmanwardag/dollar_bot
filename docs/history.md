# About MyDollarBot's /history Feature
This feature enables the user to view all of their stored records i.e it gives a historical view of all the expenses stored in MyDollarBot.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/shonilbhide/dollar_bot/blob/main/code/history.py)

# Code Description
## Functions

- run(message, bot): This is the primary function that handles the display of historical spending data for a user.
How it works: It takes two inputs, message (a message from the user) and bot (a communication tool for the bot). The function first tries to read the user's historical data, and if it finds any data, it formats it into a tabular view. Then it sends this data back to the user. If no data is found, it informs the user that there are no records. To provide the user with their spending history.

- helper.read_json(): This function reads data from a JSON file. To retrieve the user's historical data.

- helper.getUserHistory(chat_id): This function retrieves a specific user's spending history. To obtain the user's historical spending records based on their chat ID.

- bot.send_message(chat_id, tabular_data, parse_mode="Markdown"): This sends the formatted spending data back to the user in a message, allowing the user to view their historical data in a neat table format. To present the historical data to the user in a visually appealing way.

- Exception Handling: The code is prepared to handle exceptions. If any errors occur during the process, it logs the error and informs the user about the issue. To ensure that the user receives feedback in case something goes wrong, and to keep a record of errors for debugging.

# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /add into the telegram bot.

