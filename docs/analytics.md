# About DollarBot's /analytics Feature
This feature allows users to view graphical insights about their budgeting and expenses.

There are four types of graphs that can be viewed.
1. 

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/sak007/MyDollarBot-BOTGo/blob/main/code/budget.py)

# Code Description
## Functions

1. run(message, bot):
This is the main function used to implement the budget feature. It pop ups a menu on the bot asking the user to choose to add, remove or display a budget, after which control is given to post_operation_selection(message, bot) for further proccessing. It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the main code.py function.

2. post_operation_selection(message, bot):
It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the run(message, bot): function in the budget.py file. Depending on the action chosen by the user, it passes on control to the corresponding functions which are all located in different files.   


# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /budget into the telegram bot.
