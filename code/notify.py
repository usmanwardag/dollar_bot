from jproperties import Properties
from notifier import TelegramNotifier

configs = Properties()

def notify(chat_id, cat, amount):
    print("inside notify")
    with open("user.properties", "rb") as read_prop:
        configs.load(read_prop)
    token = str(configs.get("api_token").data)
    print(token)
    notifier = TelegramNotifier(token, parse_mode="HTML", chat_id=chat_id)
    msg = "<b>Budget for " + cat + " exceeded by $" + amount + " !!!!</b>"
    notifier.send(msg)