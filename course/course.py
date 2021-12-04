import requests
from bs4 import BeautifulSoup
import json


# получаем курс USD с сайта МинФина
def Currency_exchange_rate_dollar():
    url = 'https://minfin.com.ua/currency/nbu/'
    source = requests.get(url)
    main_text = source.text
    soup = BeautifulSoup(main_text)
    table = soup.find('table', {'class': 'table-auto'})
    tr = table.find('td', {'class': 'responsive-hide'})
    tr_1 = tr.text
    tr_2 = tr_1[1:6]
    return float(tr_2)

print("Выберите операцию", "RATE", "BUY", "SELL", "AVAILABLE", "BUY_ALL", "SELL_ALL", "RESTART")

# по запросу "RATE" выводим на экран текущий курс
def input_rate():
    global curr
    oper = input()
    if oper == 'RATE':
        curr = Currency_exchange_rate_dollar()
    return curr

print(input_rate())

# запрос на покупку USD "BUY" + конвертация в UAH
def input_buy():
    global buy_usd
    oper1 = input()
    if oper1 == 'BUY':
        USD_input = int(input("Введите сумму USD для покупки: "))
        buy_usd = Currency_exchange_rate_dollar() * USD_input
    return buy_usd

print(input_buy())

# запрос на продажу USD "SELL" + конвертация в UAH
def input_sell():
    oper2 = input()
    if oper2 == 'SELL':
        USD_input = int(input("Введите сумму USD для продажи: "))
        sell_usd = Currency_exchange_rate_dollar() * USD_input
    return sell_usd

print(input_sell())

# Чтение файла JSON содержащего данные по балансам USD и UAH
def read_balance_UAH_json(file):  # читаем из файла баланс гривен
    with open(file, 'r') as file:
        data = json.load(file)
        return data
#
read_balance_UAH_json("balance_default.json")

## считываем начальный баланс валют
def input_available():
    oper3 = input()
    if oper3 == 'AVAILABLE':
        return read_balance_UAH_json("balance_default.json")

print(input_available())

# Остаток UAH на счету после покупки USD нажать 'enter"
def UAH_balance_after_buy():
    UAH_new_balance = read_balance_UAH_json("balance_default.json") - input_buy()
    return UAH_new_balance

UAH_balance_after_buy()


# читаем файл с временным балансом UAH ("balance_temp.json")
def read_balance_UAH_json(file):  # читаем из файла баланс гривен
    with open(file, 'r') as file:
        data = json.load(file)
        return data ["Balance"] ["UAH"]
#
print(read_balance_UAH_json("balance_UAH_temp.json"))

# записать новый баланс в файл balance_UAH_temp.json
def write_balance_UAH_json():
    settings = read_balance_UAH_json("balance_default.json") - input_buy()
    with open('balance_UAH_temp.json', 'w', encoding='utf-8') as file:
        json.dump(settings, file, ensure_ascii=False, indent=4)
    return settings

write_balance_UAH_json()



