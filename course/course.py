import requests
from bs4 import BeautifulSoup
import json


# url = 'https://minfin.com.ua/currency/nbu/'
# source = requests.get(url)
# main_text = source.text
# soup = BeautifulSoup(main_text)
# table = soup.find('table', {'class': 'table-auto'})
# tr = table.find('td', {'class': 'responsive-hide'})
# tr = tr.text
# tr = tr[1:5]
# USD = float(tr)
# print(type(USD), USD)

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
    # tr_3 = ''
    # for i in tr_2:
    #     if i == '.':
    #         i = ','
    #     tr_3 += i
    # Curse = 'Курс доллара' + str(tr_3)
    # return tr_2
    return float(tr_2)


#
#
# print(Currency_exchange_rate_dollar())


# Чтение файлв JSON содержащего данные по балансам USD и UAH


def read_balance_UAH_json(file):  # читаем из файла баланс гривен
    with open(file, 'r') as file:
        data = json.load(file)
        return data['Balance']['UAH']


def read_balance_USD_json(file):  # читаем из файла баланс долларов
    with open(file, 'r') as file:
        data = json.load(file)
        return data['Balance']['USD']


print(read_balance_UAH_json('balance.json'), read_balance_USD_json('balance.json'))   # можно использовать для кнопки RESET


######### написать операцию по покупке USD ###########################################################################################################






new_UAH = 500         # баланс гривен после операции с валютами
new_USD = 500               # баланс долларов после операций с валютами


def write_balance_UAH_json(balance):
    with open('balance.json', 'rt') as file:
        settings = json.load(file)
        settings["UAH"] = new_UAH
        with open('balance.json', 'wt') as file:
            json.dump(settings, file)
            return settings


def write_balance_USD_json(balance):
    with open('balance.json', 'rt') as file:
        settings = json.load(file)
        settings["USD"] = new_USD
        with open('balance.json', 'wt') as file:
            json.dump(settings, file)
            return settings


print(write_balance_UAH_json(new_UAH), write_balance_USD_json(new_USD))





# ############################################ Cюда присвоим переменную с количествои грн которая будет менятся
# ##############################
# def uah_1(): uah = 10000 return uah
#
#
# ############################ конвертация грн в долларах ################################
# def exchange_UAH_to_USD():
#     UAH_1 = int(uah_1())
#     USD_1 = int(Currency_exchange_rate_dollar())
#     count = UAH_1 / USD_1
#     # amount = count[:8]
#     print(type(count))


# exchange_UAH_to_USD()

#
# from tkinter import *
# from tkinter import messagebox
# from tkinter import ttk
# import math
# import sys
#
# root = Tk()
# root.title("UAH - USD")
# bttn_list = [
#     "BUY", "SELL", "KURS", "Баланс", "Exit"]
# r = 1
# c = 0
# for i in bttn_list:
#     rel = ""
#     cmd = lambda x=i: calc(x)
#     ttk.Button(root, text=i, command=cmd, width=7).grid(row=r, column=c)
#     c += 1
#     if c > 6:
#         c = 0
#         r += 1
# currency_entry = Entry(root, width=40)
# currency_entry.grid(row=0, column=0, columnspan=10)
#
#
# # логика калькулятора
# def calc(key):
#     global memory
#     if key == "=":
#         # исключение написания слов
#         str1 = "-+0123456789.*/)("
#         if currency_entry.get()[0] not in str1:
#             currency_entry.insert(END, "First symbol is not number!")
#             messagebox.showerror("Error!", "You did not enter the number!")
#         # исчисления
#         try:
#             result = eval(currency_entry.get())
#             currency_entry.insert(END, "=" + str(result))
#         except:
#             currency_entry.insert(END, "Error!")
#             messagebox.showerror("Error!", "Check the correctness of data")
#     # вывести курс USD
#     elif key == "KURS":
#         currency_entry.insert(END, "=" + str(Currency_exchange_rate_dollar() * (int(currency_entry.get()))))
#         pass
#     # выход из программы
#     elif key == "Exit":
#         root.after(1, root.destroy)
#         sys.exit
#     # elif key == "(":
#     #     calc_entry.insert(END, "(")
#     # elif key == ")":
#     #     calc_entry.insert(END, ")")
#     # else:
#     #     if "=" in calc_entry.get():
#     #         calc_entry.delete(0, END)
#     #     calc_entry.insert(END, key)
#
#
# root.mainloop()
