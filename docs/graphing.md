# About MyDollarBot's /display Feature's Graph module
This feature enables the user to see their expense in a graphical format to enable better UX.

Currently, the /display command will provide the expenses as a message to the users via the bot. To better the UX, we decided to add the option to show the expenses in a Bar Graph.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/shonilbhide/dollar_bot/blob/Rubrics/code/graphing.py)

# Code Description
## Functions

- viewBudget(data): This function creates a pie chart to visualize different budget categories. It takes a dictionary of budget data as input and generates a graph that represents the budget distribution across various categories. To provide a visual representation of how the budget is allocated in different spending categories.

- addlabels(x, y): This function is used to add labels to the bar graph. It takes two lists, 'x' (category names) and 'y' (expenditure values), and adds the corresponding values inside the bars of a bar graph. To make the bar graph more informative by labeling each bar with its expenditure value.

- visualize(total_text, monthly_budget): This is the main function that generates a bar graph to compare actual expenditure with the budget for different categories. It takes two inputs: 'total_text,' which contains information about actual expenses, and 'monthly_budget,' which is a dictionary specifying the budget for each category. To create a visual comparison between the user's actual expenditures and their budgeted amounts for different spending categories.

# How to run this feature?
After you've added sufficient input data, use the /display command and you can see the output in a pictorial representation. 
