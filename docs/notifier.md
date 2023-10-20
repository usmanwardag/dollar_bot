# About DollarSplitBot's notifier.py file
notifier.py is used to send notifications to a Telegram chat. This can be helpful for various purposes, like receiving updates or alerts from a program or service.
# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/shonilbhide/dollar_bot/blob/main/code/notifier.py)

# Code Description
## Functions
- _get_chat_id method: This is a private method within the TelegramNotifier class. It attempts to fetch the chat ID by making an API request to Telegram. The chat ID is essential to send messages to a specific chat or group. If it fails to fetch the chat ID, it sets the chat ID to None and prints an error message.

- send method: This method is used to send a message to the chat or group associated with the TelegramNotifier object. It takes a msg (message) as an argument, which is the text to be sent.
Before sending the message, it checks if the chat ID is available. If not, it attempts to retrieve it. It constructs a payload containing the chat ID and the message and sends it to the Telegram API. If the message is sent successfully, it prints a success message. If there's an error, it prints an error message.

# How to run this feature?
This file contains information on the main code.py file from where all features are run. Instructions to run this are the same as instructions to run the project and can be found in README.md.
