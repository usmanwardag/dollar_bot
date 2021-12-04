from jproperties import Properties
from notifier import TelegramNotifier

configs = Properties()


def notify():
    import os
    token = str(configs.get('api_token').data)
    notifier = TelegramNotifier(token, parse_mode="HTML")
    notifier.send("<b>Test bold text</b> and normal text")
