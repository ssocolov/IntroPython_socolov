# регулярные выражения №№№№№№№№№№

import re
import os

os.chdir("DZ_files")


# функция читает весь файл
def read_from_logs(filename):
    with open(filename, 'r') as file:
        data = file.read().split("\n")
    return data
print(read_from_logs("logs.txt"))

# функция выводит IP адреса из файла
def get_ip_numbers(logs):
    ips = []
    for line in logs:
        ip_mask = r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
        ip = re.findall(ip_mask, line)
        ips += ip
    return ips

# функция выводит даты из файла
def get_dates(logs):
    dates = []
    for line in logs:
        date_mask = r"\d{4}[-/]{1}\d{2}[-/]{1}\d{2}"
        date = re.findall(date_mask, line)
        dates += date
    return dates

logs = read_from_logs("logs.txt")

# ips = []
# for line in logs:
#     ip_mask = r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
#     ip = re.findall(ip_mask, line)
#     ips += ip
ips = get_ip_numbers(logs)
print(ips)
dates = get_dates(logs)
print(dates)

