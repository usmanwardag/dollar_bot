# About DollarSlpitBot's /add Feature
This part of a Telegram bot application helps users track their expenses and split costs with others.
Currently we have the following expense categories set by default:

- Food
- Groceries
- Utilities
- Transport
- Shopping
- Miscellaneous

The user can choose a category and add the amount they have spent to be stored in the expense tracker.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/shonilbhide/dollar_bot/blob/main/code/add.py)

# Code Description
## Functions

1. run(message, bot):
This is the main function of the "add" feature. It prompts the user to select an expense category and then directs them to the `post_category_selection` function to enter the expense amount.
   - Arguments: `message` (user's message) and `bot` (Telegram bot object).
2. `select_user(message, bot, owed_by, user_list, paid_by)`:
This function is used to select users who shared the expense. It allows users to add multiple participants for sharing an expense.
   - Arguments: `message` (user's message), `bot` (Telegram bot object), `owed_by` (a list of users who owe), `user_list` (list of users), and `paid_by` (the user who paid initially).

3. `add_shared_user(message, bot, owed_by, user_list, paid_by)`:
This function lets the user choose additional participants for sharing the expense and adds them to the list.
   - Arguments: `message` (user's message), `bot` (Telegram bot object), `owed_by` (a list of users who owe), `user_list` (list of users), and `paid_by` (the user who paid initially).

4. `user_choice(message, bot, owed_by, user_list, paid_by)`:
It handles the user's choice of adding more participants or proceeding to enter the expense category.
   - Arguments: `message` (user's message), `bot` (Telegram bot object), `owed_by` (a list of users who owe), `user_list` (list of users), and `paid_by` (the user who paid initially).

5. `post_append_spend(message, bot, owed_by, user_list, paid_by)`:
This function prompts the user to select an expense category for the shared expense.
   - Arguments: `message` (user's message), `bot` (Telegram bot object), `owed_by` (a list of users who owe), `user_list` (list of users), and `paid_by` (the user who paid initially).

6. `post_category_selection(message, bot, owed_by, paid_by, user_list)`:
This function asks the user to enter the amount spent on the chosen expense category and then directs to the `post_amount_input` function.
   - Arguments: `message` (user's message), `bot` (Telegram bot object), `owed_by` (a list of users who owe), `paid_by` (the user who paid initially), and `user_list` (list of users).

7. `post_amount_input(message, bot, selected_category, owed_by, paid_by, user_list)`:
It validates the amount entered by the user, then calls the `add_user_record` function to store the expense data.
   - Arguments: `message` (user's message), `bot` (Telegram bot object), `selected_category` (the chosen expense category), `owed_by` (a list of users who owe), `paid_by` (the user who paid initially), and `user_list` (list of users).

8. `add_user_record(user_list, message, chat_id, record_to_be_added, amount_value, owed_by, paid_by)`:
This function stores the expense record in the user's data, updates who owes whom, and keeps track of the shared expense.
   - Arguments: `user_list` (list of users and their expenses), `message` (user's message), `chat_id` (user's chat ID), `record_to_be_added` (expense record), `amount_value` (amount spent), `owed_by` (a list of users who owe), and `paid_by` (the user who paid initially).

This code segment is part of a larger bot application, and it manages the addition of expenses and splitting costs among users. It helps users keep track of their spending and shared expenses with friends or groups.

# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /add into the telegram bot.

Below you can see an example in text format:

Rutuja Rashinkar, [19-10-2023 08:27 PM]
/add

My_MyDollarBot_bot, [19-10-2023 08:27 PM]
Select who paid for the Expense

Rutuja Rashinkar, [19-10-2023 08:27 PM]
Rutuja Rashinkar

My_MyDollarBot_bot, [19-10-2023 08:27 PM]
Select who shares the Expense

Rutuja Rashinkar, [19-10-2023 08:27 PM]
B

My_MyDollarBot_bot, [19-10-2023 08:27 PM]
Do you want to add more user to share the expense? Y/N

Rutuja Rashinkar, [19-10-2023 08:28 PM]
Y

My_MyDollarBot_bot, [19-10-2023 08:28 PM]
Select who shares the Expense

Rutuja Rashinkar, [19-10-2023 08:28 PM]
C

My_MyDollarBot_bot, [19-10-2023 08:28 PM]
Do you want to add more user to share the expense? Y/N

Rutuja Rashinkar, [19-10-2023 08:28 PM]
N

My_MyDollarBot_bot, [19-10-2023 08:28 PM]
Select a category

My_MyDollarBot_bot, [19-10-2023 08:28 PM]
Select Category

Rutuja Rashinkar, [19-10-2023 08:28 PM]
Groceries

My_MyDollarBot_bot, [19-10-2023 08:28 PM]
How much did you spend on Groceries? 
(Enter numeric values only)

Rutuja Rashinkar, [19-10-2023 08:28 PM]
45