# About DollarSplitBot's /add_user Feature
This feature is a part of a Telegram bot's functionality that allows users to register new people or names in a chat. The primary purpose of this code is to handle the registration of people's names within a specific chat and manage the list of registered users.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/shonilbhide/dollar_bot/blob/main/code/add_user.py)

# Code Description
## Functions

1. `register_people(message, bot, user_list)`:
   - This function initiates the registration process when a user sends a message to the bot.
   - It checks if the user's chat ID is not in the `user_list`, a data structure that stores user information.
   - If the chat ID is not in `user_list`, it creates a new user record using `helper.createNewUserRecord(message)` and adds it to the `user_list`.
   - It sets up a keyboard interface for user input and prompts the user to enter the name of the person they want to register.
   - After the user provides a name, it registers the name and sets up the next step handler to handle further options.

2. `add_person(message, bot, registered_users, user_list)`:
   - This function is called after the user provides the name they want to register.
   - It checks if the provided name is unique for the chat. If the name is already registered, it informs the user. Otherwise, it adds the name to the list of registered users.
   - It provides feedback to the user about the successful registration of the name and offers further options using a keyboard interface.
   - Depending on the user's choice, it can either prompt the user to register another person or finish the registration process.

3. `handle_registration_choice(message, bot, registered_users, user_list)`:
   - This function handles the user's choice after registering a person.
   - It checks the user's choice and acts accordingly. If the user wants to register another person, it prompts for a name again. If the user chooses to finish registration, it stores the registered users and their related data in the `user_list`. This data includes who owes money to whom and how much.
   - After storing the data, it displays the list of registered users or informs the user that no users are registered yet.


# How to run this feature?
This code is part of a Telegram bot's functionality that allows users to register people within a chat, stores information about registered users and their financial transactions, and provides a user-friendly interface for interacting with the bot during the registration process.
