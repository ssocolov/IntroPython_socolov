import requests
from bs4 import BeautifulSoup
import json


# парсим курс USD
def Currency_exchange_rate_dollar():
    url = 'https://minfin.com.ua/currency/nbu/'
    source = requests.get(url)
    main_text = source.text
    soup = BeautifulSoup(main_text)
    table = soup.find('table', {'class': 'table-auto'})
    tr = table.find('td', {'class': 'responsive-hide'})
    tr_1 = tr.text
    tr_2 = tr_1[1:5]
    return float(tr_2)


print("Выберите операцию", "RATE", "AVAILABLE", "BUY", "SELL", "BUY_ALL", "SELL_ALL", "RESTART")


# по запросу "RATE" выводим на экран текущий курс
def input_rate():
    global curr
    oper = input()
    if oper == 'RATE':
        curr = Currency_exchange_rate_dollar()
    return curr


# print(input_rate())


# запрос на покупку USD "BUY" + конвертация в UAH
def input_buy():

    oper1 = input()
    if oper1 == 'BUY':
        USD_input = int(input("Введите сумму USD для покупки: "))
        buy_usd = Currency_exchange_rate_dollar() * USD_input
    return buy_usd


# покупаем USD конвертация
# def exchange_USD_to_UAH():
#     USD_input = int(input("Введите сумму USD для покупки: "))
#     UAH_to_by_USD = Currency_exchange_rate_dollar() * USD_input
#     return UAH_to_by_USD


print(input_buy())


def input_sell():

    oper2 = input()
    if oper2 == 'SELL':
        USD_input = int(input("Введите сумму USD для продажи: "))
        sell_usd = Currency_exchange_rate_dollar() * USD_input
    return sell_usd


print(input_sell())


# продаем USD конвертация
# def exchange_UAH_to_USD():
#     USD_input = int(input("Введите сумму USD для продажи: "))
#     USD_to_SELL = Currency_exchange_rate_dollar() * USD_input
#     return USD_to_SELL


# print(exchange_UAH_to_USD())


# Чтение файла JSON содержащего данные по балансам USD и UAH
def read_balance_UAH_json(file):  # читаем из файла баланс гривен
    with open(file, 'r') as file:
        data = json.load(file)
        return data['Balance']['UAH']


print(read_balance_UAH_json("balance_default.json"))


def read_balance_USD_json(file):  # читаем из файла баланс долларов
    with open(file, 'r') as file:
        data = json.load(file)
        return data['Balance']['USD']


# print(read_balance_USD_json('balance_default.json'))


# Остаток UAH на счету после покупки
def UAH_balance_after_buy():
    UAH_new_balance = read_balance_UAH_json("balance_default.json") - exchange_USD_to_UAH()
    return UAH_new_balance


# print(UAH_balance_after_buy())


# записать новый баланс в файл
def write_balance_UAH_json():
    with open('balance_temp.json', 'rt') as file:
        settings = json.load(file)
        settings["UAH"] = UAH_balance_after_buy
        with open('balance_temp.json', 'wt') as file:
            json.dump(settings, file)
        return settings

# def write_balance_USD_json(balance):
#     with open('balance_default.json', 'rt') as file:
#         settings = json.load(file)
#         settings["USD"] = new_USD
#         with open('balance_default.json', 'wt') as file:
#             json.dump(settings, file)
#             return settings


# print(write_balance_UAH_json(UAH_balance_after_buy))
