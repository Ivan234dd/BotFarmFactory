TELEGRAM_ACCOUNTS = [
    dict(phone='+48735538445', proxy="http://mtddwniu:a1avaureymee@45.127.248.127:5128"),
    dict(phone='+99999999991', proxy="https://user:pass@host:port"),
    dict(phone='+55555555544'),
]

try:
    from accounts_local import *
except ImportError:
    pass
