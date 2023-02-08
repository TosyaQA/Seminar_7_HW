import datetime

def log_cash(mode, result):
    with open ("log.txt", 'a', encoding='utf-8') as file:
        file.write(f"{mode} = {result}. Время запроса: {str(datetime.datetime.now())} \n")