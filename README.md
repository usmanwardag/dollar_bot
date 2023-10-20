# 💰 DollarSplitBot 💰

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#why-should-you-use-dollarsplitbot">Why should you use DollarSplitBot?</a></li>
    <li><a href="#check-out-the-video">Check out the video!</a></li>
    <li><a href="#what-is-new-in-this-version">What is new in this version?</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#testing">Testing</a></li>
    <li><a href="#code-coverage">Code Coverage</a></li>
    <li><a href="#automated-analysis-tools">Automated Analysis Tools</a></li>
    <li><a href="#License">License</a></li>
    <li><a href="#code-documentation">Code Documentation</a></li>
    <li><a href="#version-numbers">Version Specifications</a></li>
    <li><a href="#how-to-contribute">How to Contribute</a></li>
    <li><a href="#depriciated-libraries">Depriciated Libraries</a></li>
    <li><a href="#future-roadmap">Future RoadMap</a></li>
    <li><a href="#projects-users">Number of projects and Users associated with the project</a></li>
    <li><a href="#contributors">Contributors</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
    <li><a href="#contact-us">Contact Us</a></li>
  </ol>
</details>

<hr>
<p align="center">
<a><img  height=350 width=350 
  src="https://s1.mzstatic.com/us/r30/Purple1/v4/de/ab/45/deab454d-8881-b37d-9513-b0e26424cc57/pr_source.png?downloadKey=1425248837_8a393efcc4a821cbf9639d5570f8e966" alt="Dollar BoT"></a>
</p>
<hr>

[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://github.com/shonilbhide/dollar_bot)

![MIT license](https://img.shields.io/badge/License-MIT-green.svg)
[![Platform](https://img.shields.io/badge/Platform-Telegram-blue)](https://desktop.telegram.org/)
![GitHub](https://img.shields.io/badge/Language-Python-blue.svg)
[![GitHub contributors](https://img.shields.io/github/contributors/shonilbhide/dollar_bot)](https://github.com/shonilbhide/dollar_bot/graphs/contributors)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10015948.svg)](https://zenodo.org/records/10015948)
[![CircleCI](https://dl.circleci.com/status-badge/img/circleci/KRJsvuprWQqWTJMZXoedkH/S11gsHj3tEGpX8YLaeYmJ5/tree/main.svg?style=svg&circle-token=03704a79749569bc04a53ce05296fb34003e4713)](https://dl.circleci.com/status-badge/redirect/circleci/KRJsvuprWQqWTJMZXoedkH/S11gsHj3tEGpX8YLaeYmJ5/tree/main)
[![codecov](https://codecov.io/gh/usmanwardag/dollar_bot/branch/main/graph/badge.svg?token=PYAWX95R67)](https://codecov.io/gh/usmanwardag/dollar_bot)

[![GitHub issues](https://img.shields.io/github/issues/shonilbhide/dollar_bot)](https://github.com/shonilbhide/dollar_bot/issues)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/shonilbhide/dollar_bot)](https://github.com/shonilbhide/dollar_bot/issues?q=is%3Aissue+is%3Aclosed)

<hr>

## Why should you use DollarSplitBot?

"Discover a whole new level of financial clarity and fairness – where you'll never have to wonder 'Who owes me, and who do I owe?' again. Say goodbye to financial puzzles, and embrace our extended expense management system to reclaim your peace of mind!"

Introducing DollarSplitBot, your trusty companion on Telegram, here to turn the mundane task of tracking your daily expenses into a breeze. This ingenious bot simplifies the process of keeping tabs on your spending, even when you're offline. But that's not all; it's also your go-to solution for managing group expenses and ensuring everyone's financial equilibrium.

With just a few swift commands, DollarSplitBot empowers you to:

1. **Welcome New Faces:** Add your friends to share expenses with ease.
2. **Log Your Transactions:** Document and store your expenditures effortlessly.
3. **Equitable Divisions:** Showcase your spending history, unraveling who owes what to whom.
4. **Money Matters:** Keep tabs on your daily and monthly expenditure totals.
5. **Your Financial Story:** Access your spending history at any time.
6. **A Clean Slate:** Erase all records when it's time to start anew.
7. **Tailored Details:** Edit any spending particulars to your liking.
8. **Paper Trail:** Generate sleek PDF expenditure reports for a comprehensive overview.
9. **Friendly Nudges:** Send friendly reminders via email to ensure financial settlements.

DollarSplitBot: Where simplicity meets financial harmony at your fingertips.

## Check out the video!

To demonstrate our application's functionality and showcase its working examples, we have produced a YouTube video for the DollarSplitBot project. In this video, we showcase that the system operates as intended. You can view the video by clicking on the following link:  [YouTube Link](https://youtu.be/aCjcT1CHAzU)

## What is new in this version?

Checkout the [this documentation](docs/Update_Version.pdf)
## Installation

The below instructions can be followed in order to set-up this bot at your end in a span of few minutes! Let's get started:

1. Clone this repository to your local system.

2. Start a terminal session in the directory where the project has been cloned. Run the following command to install the required dependencies:
```
  pip install -r requirements.txt

```
3. Download and install the Telegram desktop application for your system from the following site:
 ```
 https://desktop.telegram.org/
 ```
## How to run?

1. In Telegram, search for "BotFather". Click on "Start", and enter the following command:
```
  /newbot
```
2. Follow the instructions on screen and choose a name for your bot (e.g., `dollarbot`). After this, select a username for your bot that ends with "bot". The username has to be unique. 

3. BotFather will now confirm the creation of your bot and provide a TOKEN to access the HTTP API - copy and save this token for future use.

4. In the repo directory (where you cloned it), run these commands to (i) grant execution access to a bash script, and (ii) execute that bash script to run the Telegram Bot:
```
   chmod a+x run.sh
   ./run.sh
```
   
(OR)
```
   chmod a+x run.sh
   bash run.sh
```
```Note```: It will ask you to paste the API token you received from Telegram in step 4.
A successful run will generate a message on your terminal that says "TeleBot: Started polling." 

5. In the Telegram app, search for your newly created bot by entering the username and open the same. Now, on Telegram, enter the "/start" or "menu" command, and you are all set to track your expenses!

### Run Automatically at Startup

To run the script automatically at startup / reboot, simply add the `.run_forever.sh` script to your `.bashrc` file, which executes whenever you reboot your system.

## Configuring Email Credentials for SMTP: Sending Emails from Your Account

**SMTP (Simple Mail Transfer Protocol)** is a standard protocol for sending emails. It is widely used for sending email messages from one server to another. In the code, we are using SMTP to send emails via a Gmail account. Here's how the SMTP configuration and usage work:

1. **SMTP Server**: The `smtp_server` variable is set to 'smtp.gmail.com,' which is the SMTP server for Gmail. This server is responsible for sending your email messages.

2. **SMTP Port**: The `smtp_port` variable is set to 587. This is the port for TLS (Transport Layer Security) encryption. Gmail uses this port for secure email communication.

3. **SMTP Username**: The smtp_username variable should be set to your own Gmail email address from which you want to send the emails. Make sure to replace `your-email@gmail.com` with your actual Gmail email address in the code. This ensures that the emails will be sent from your specific Gmail account.

4. **SMTP Password**: The `smtp_password` variable is set, you need to generate an "App Password". An App Password is a 16-character code that allows you to access your Gmail account without revealing your real password. To generate an App Password, follow these steps:

   - Go to your Google Account settings (https://myaccount.google.com/).
   - In the "Security" section, under "Signing in to Google", select "App Passwords".
   - Select "Mail" and "Other (Custom name)" from the dropdown menus.
   - Click "Generate".
   -  Google will provide you with a 16-character App Password. Use this as your `smtp_password` in your code.

By customizing these settings, you can send emails from any email account using SMTP. Just ensure you are adhering to the security guidelines provided by your email provider.

## Testing

We use pytest to perform testing on all unit tests together. The command needs to be run from the home directory of the project. The command is:
```
python run -m pytest test/
```

## Code Coverage

Code coverage is part of the build. Every time new code is pushed to the repository, the build is run, and along with it, code coverage is computed. This can be viewed by selecting the build, and then choosing the codecov pop-up on hover.

Locally, we use the coverage package in python for code coverage. The commands to check code coverage in python are as follows:

```
coverage run -m pytest test/
coverage report
```

## Use Cases

Common use cases for DollarSplitBot summarized in three points:

1. **Personal Expense Tracking:**
   - Easily log and monitor your individual daily and monthly expenses, including groceries, dining out, transportation, and entertainment.
   - Access your spending history and totals at any time, providing valuable insights into your financial habits.

2. **Group Expense Management:**
   - Efficiently manage group expenses with friends or family members. Add participants to track shared costs and responsibilities.
   - DollarSplitBot calculates equitable divisions, simplifying the process of determining who owes what to whom in group expenses.

3. **Expense Reporting and Communication:**
   - Generate detailed PDF expenditure reports for a comprehensive overview of your financial activity.
   - Utilize the bot's email reminders to facilitate financial settlements and maintain harmony in shared expenses, ensuring everyone is accountable.

Certainly, you can watch this video [YouTube Link](https://youtu.be/JT06PTMHz7Y) for a step-by-step guide on how to use DollarSplitBot. 

## Automated Analysis Tools

This project uses various automated analysis tools like 
- pylint and flask8 for code formating
- pytest for tesing
- coverage.py for code coverage
- Travis CI for automated testing
  
## License

This project is licensed under the terms of the MIT license. Please check [License](https://github.com/shonilbhide/dollar_bot/blob/main/LICENSE) for more details.


## Code Documentation

Checkout the [docs](https://github.com/shonilbhide/dollar_bot/tree/main/docs)

## Version Specifications
The current release of the project has the following versions:
- python- Python 3.9.1
- pip- pip 23.2.1


## How to Contribute

We would be happy to receive contributions! If you'd like to, please go through our [CONTRIBUTING.md](https://github.com/shonilbhide/dollar_bot/blob/main/CONTRIBUTING.md)

For any feedback, issues, or bug reports, please create an issue [here](https://github.com/shonilbhide/dollar_bot/issues/new).

## Depriciated Libraries
- "The parameter "none_stop" is deprecated. Use "non_stop" instead."
## Future RoadMap

- More content can be added for the way notifications can be displayed on the user front. This can be done to make the UI more interactive.
- Recurring expenses feature can be added for faster addition of expenses instead of following the whole process of everytime.
- This application can be integrated with a group chat to track expenses of a group.
- A better model can be implemented to forecast the budgets and expenses for future.
- Make our bot support multiple languages, and not just english so that it might be helpful in the other regions of the world.
-  Integrate the bot with financial services, like bank APIs, for real-time expense tracking and account balance updates.
- Implement a reminder system to notify users of recurring expenses, upcoming bills, or when they need to settle debts.


## Number of projects and Users associated with the project
Here is the list of projects and the users associated with the project:
- Project 1[Project1] (https://github.com/shonilbhide/dollar_bot) and users: Shonil_Bhide, Rutuja_Rashinkar, Sakshi_Basapure Akshada_Malpure
- Project 2 [Project2] (https://github.com/usmanwardag/dollar_bot) and users: Usman_Khan, Aakriti_Aakriti, Suneha_Bose, Muskan_Gupta, Kriti_Khullar
- Project 3 [Project3] (https://github.com/sak007/MyDollarBot-BOTGo) and users: Athithya, Subramanian, Ashok, Zunaid, Rithik, Dev, Prakruthi, Radhika, Rohan, Sunidhi
- Project 4 [Project4] (https://github.com/deekay2310/MyDollarBot) and users:Dev, Prakruthi, Radhika, Rohan, Sunidhi 


## Contributors
<table>
  <tr>
    <td align="center"><a href="https://github.com/shonilbhide"><img src="https://avatars.githubusercontent.com/u/51792152?s=96&v=4" width="75px;" alt=""/><br /><sub><b>Shonil bhide</b></sub></a></td>
    <td align="center"><a href="https://github.com/sakshibasapure"><img src="https://avatars.githubusercontent.com/u/40641044?v=4" width="75px;" alt=""/><br /><sub><b>Sakshi Basapure</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/rutuja-39"><img src="https://avatars.githubusercontent.com/u/59025269?v=4" width="75px;" alt=""/><br /><sub><b>Rutuja Rashinkar</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/agmalpur"><img src="https://avatars.githubusercontent.com/u/144184451?v=4" width="75px;" alt=""/><br /><sub><b>Akshada Malpure</b></sub></a><br /></td>
  </tr>
</table>

## Acknowledgements

- We would like to express our gratitude 🙏🏻 and a big thank you 😇 to Prof. Dr. Timothy Menzie for giving us the opportunity to get into the shoes of software building and learning new skills and development process throught the project building.
- A big thank you 😊 to the Teaching Assistants for their support.
- Thank you to the previous team 😊 for a thorough ReadMe and deatiled documentation.[MyDollarBot](https://github.com/sak007/MyDollarBot-BOTGo)
- Thank you to the ⭐️[Telegram bot](https://github.com/python-telegram-bot/python-telegram-bot)

## Contact Us
In case of any queries, kindly contact us on: <b>csc510group32@gmail.com</b>
