# About MyDollarBot's /add_category Feature
#TO-DO
This feature enables the user to add a new category.
Currently we have the following expense categories set by default:

- Food
- Groceries
- Utilities
- Transport
- Shopping
- Miscellaneous


# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/sak007/MyDollarBot-BOTGo/blob/main/code/add_category.py)

# Code Description
## Functions

1. run(message, bot):
This is the main function used to implement the add_category feature. It asks the user to add a new category, after which control is given to post_append_spend(message, bot) for further proccessing. It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the main code.py function.

2. post_append_spend(message, bot):
 It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the run(message, bot): function in the add_category.py file. It requests the user to enter the a new category. It also handles the case of keeping the category names unique.


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