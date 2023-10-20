# About MyDollarBot's code.py file
code.py is the main file from where calls to the corresponding .py files for all features are sent. It contains a number of endpoints which redirect to function calls in the corresponding files. 

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/shonilbhide/dollar_bot/blob/Rubrics/code/code.py)


# Code Description
## Functions

- run(message, bot): This function serves as the entry point for the budget feature. It displays a menu in the chatbot, prompting the user to select an operation related to their budget. The available options are determined by the helper.getBudgetOptions() function. Once the user makes a selection, the control is passed to the post_operation_selection(message, bot) function for further processing.

- post_operation_selection(message, bot): This function processes the user's selection of a budget operation. It checks if the selected operation is valid and, if not, informs the user that the operation is invalid. If the user is new and doesn't have a budget record, it initializes one. Depending on the selected operation (e.g., add, update, view, delete), it calls the respective sub-module functions to perform the desired operation and then stores the updated budget data using helper.write_json(user_list).

- budget_update.run(message, bot): This function is called when the user selects the "add" or "update" operation. It handles the process of adding or updating budget expenses. The exact details of these operations are likely implemented in the budget_update module.

- budget_view.run(message, bot): This function is called when the user selects the "view" operation. It is responsible for displaying the user's budget information, such as expenses and balances. The specific implementation of the viewing process is likely found in the budget_view module.

- budget_delete.run(message, bot): This function is called when the user selects the "delete" operation. It is responsible for managing the process of deleting specific budget expenses. The details of how the deletion process works are likely defined in the budget_delete module.

# How to run this feature?
This file contains information on the main code.py file from where all features are run. Instructions to run this are the same as instructions to run the project and can be found in README.md.
