# About MyDollarBot's /helper class
The helper file contains a set of functions that are commonly used for repeated tasks in the various features of MyDollarBot. Since these come up often, we have put them all up here in a separate file for reusability.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/shonilbhide/dollar_bot/blob/main/code/helper.py)

# Code Description
## Functions

- spend_categories: This is a list of predefined spending categories, such as "Food," "Groceries," "Utilities," etc. These categories are used to categorize expenses.

- choices: A list containing three options: "Date," "Category," and "Cost." These options might be used to select how the user wants to view or filter their expense data.

- spend_display_option: This list contains two options: "Day" and "Month." These options could be used to specify whether the user wants to view expenses on a daily or monthly basis.

- spend_estimate_option: Another list with two options: "Next day" and "Next month." These might be used to estimate future expenses based on past spending data.

- update_options: A dictionary with two key-value pairs, "continue" and "exit." These options could be used to continue or exit a particular process within the program.

- budget_options: A dictionary with options related to budget management, such as "add," "update," "view," and "delete."

- budget_types: A dictionary that defines different types of budgets, such as "Overall Budget" and "Category-Wise Budget."

- data_format: A dictionary that seems to be an initial data structure for storing user data, expenses, and budgets. It has placeholders for various data, including user information, expenses, and budget details.

- commands: A dictionary that provides descriptions of various commands or actions that the user can perform within the program. These descriptions include commands like "add," "display," "edit," etc.

Functions: The code defines several functions, including read_json, write_json, validate_entered_amount, and others. These functions likely handle reading and writing data, validating user input, and managing user records and budgets

# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /add into the telegram bot.

This file is not a feature and cannot be run per se. Its functions are used all over by the other files as it provides helper functions for various functionalities and features.
