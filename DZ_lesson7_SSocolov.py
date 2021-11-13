# https://py.checkio.org/
# сделать первый уровень
#
# Задание. data.json - файл с данными о некоторых математиках прошлого.
#
# 1. Необходимо написать функцию,
# которая считает эти данные из файла и возвращала содержимое файла в той же структкру, что и в файле. Параметр
# функции - имя файла.
import os
import json
from operator import itemgetter

os.chdir("DZ_files")


def read_json(data):
    with open(data, "r", encoding='utf-8') as file:
        result = json.load(file)
    return result


print(read_json("data.json"))


# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.

def sort_by_surname(data):
    with open(data, "r", encoding='utf-8') as file:
        sort_name = sorted(json.load(file), key=itemgetter('name'))
        return sort_name


print(sort_by_surname("data.json"))

# 3. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.

##### ЗАДАНИЕ НЕ ЗАКОНЧЕНО ВОЗНИКЛИ ТРУДНОСТИ

def death_date(data):
    with open(data, "r", encoding='utf-8') as file:
        for record in json.load(file):   # НЕ МОГУ ПОНЯТЬ, ПО КАКОЙ ПРИЧИНЕ ОН ВЫЧИТЫВАЕТ ИЗ СПИСКА ТОЛЬКО ПЕРВЫЙ СЛОВАРЬ
            dates = (''.join(record["years"].split())).split("–")
            death = int(dates[1].replace(".", "").replace("c", "").replace("BC", ""))
            death = death * -1 if dates[1].find("BC") != -1 else death
            # record["death"] = death
            return death


print(death_date("data.json"))


# 4. Написать функцию сортировки по количеству слов в поле "text".
#
# Отсортировать данные из файла с помощью данных функций.
