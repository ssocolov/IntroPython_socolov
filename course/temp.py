import requests
from bs4 import BeautifulSoup
import json


# #################################Курс грн к доллару###############################################
#
def Currency_exchange_rate_dollar():
    url = 'https://minfin.com.ua/currency/nbu/'
    source = requests.get(url)
    main_text = source.text
    soup = BeautifulSoup(main_text)
    table = soup.find('table', {'class': 'table-auto'})
    tr = table.find('td', {'class': 'responsive-hide'})
    tr_1 = tr.text
    tr_2 = tr_1[1:5]
    tr_3 = float(tr_2)
    # tr_3 = ''
    # for i in tr_2:
    #     if i == '.':
    #         i = ','
    #     tr_3 += i
    Curse = 'Курс доллара' + str(tr_3)
    print(tr_3)
# Currency_exchange_rate_dollar()
#
# ############################################Сюда присвоим переменную с количествои грн которая будет менятся##############################
# def uah_1():
#     uah = 10000
#     return uah
# # ############################конвертация грн в доллаh################################
# def exchange_UAH_to_USD():
#     UAH_1 = int(uah_1())
#     USD_1 = int(Currency_exchange_rate_dollar())
#     count = UAH_1 / USD_1
#     amount = str(count)
#     result = amount[:5]
#     print(result)
#
# exchange_UAH_to_USD()

def read_balance_json(file):
    with open(file, "r") as file:
        data = json.load(file)
        return data


print(read_balance_json("balance.json"))


# def write_json(filename, data, indent=None):
#     with open('balance.json', 'w') as f:
#         json.dump(data, f, ensure_ascii=False)


# with open('balance.json') as f:
#     data = json.load(f)
#     data['UAH'] =
# with open('balance.json', 'w') as f:
#     json.dump(data, ensure_ascii=False, indent=4)
#
# import json
# with open('balance.json') as f:
#     data = json.load(f)
# data['UAH'] = 'bye'
# with open('balance.json', 'w') as f:
#     json.dump(data, ensure_ascii=False, indent=4)



# def read_balance(text):
#     my_file = open("balance.txt", "r")
#
#     my_file.close()
#     return my_string
#
#
# print("Баланс кошелька>:")
# print(read_balance("balance.txt"))
#
#
# def write_balance(text):
#     my_file = open("balance.txt", "w")
#     my_file.write("UAH = 100 \nUSD = 650 ")
#     my_file.close()
#     return
#
#
# print(write_balance(""))

# def withdraw():  # asks for withdrawal amount, withdraws amount from balance, returns the balance amount
#     while True:
#         withdraw = int(input("Сколько вы хотите продать UAH"))
#         if withdraw > balance:
#             print("У вас нет на счету такой суммы")
#         else:
#             new_balance = balance - withdraw
#             print("Сумма оставшаяся на вашем счету: UAH" + str(new_balance))
#             return (new_balance)
#
# def deposit():
#     deposit = int(input("Сколько вы хотите внести на баланс: "))
#     new_balance = balance + deposit
#     print("Сумма оставшаяся на вашем счету: UAH" + str(new_balance))
#     return (new_balance)
#
# # This is the only place you HAVE to change for it to work
# balance = withdraw()
# balance = deposit()
