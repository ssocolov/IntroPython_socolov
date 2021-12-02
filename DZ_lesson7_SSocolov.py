#
# Задание. balance_default.json - файл с данными о некоторых математиках прошлого.
import os
import json
import re
from operator import itemgetter

os.chdir("DZ_files")


# 1. Необходимо написать функцию,
# которая считает эти данные из файла и возвращала содержимое файла в той же структкру, что и в файле. Параметр
# функции - имя файла.

def read_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


print(read_json("balance_default.json"))


# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.

def sort_by_surname(data):
    with open(data, "r", encoding='utf-8') as file:
        sort_name = sorted(json.load(file), key=itemgetter('name'))
        return sort_name


print(sort_by_surname("balance_default.json"))

# 3. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.

dict_list = read_json("balance_default.json")


def key_sorted_by_data(obj_dict):
    years = re.findall(r'[0-9]+', obj_dict["years"])
    return int(years[-1]) if "BC" in obj_dict["years"] else -int(years[-1])


new_dict_list = sorted(dict_list, key=key_sorted_by_data)

print(new_dict_list)


# 4. Написать функцию сортировки по количеству слов в поле "text".


def sort_by_len_text(person_dict):
    return len(person_dict["text"].split())


data_math_sort_by_len_text = sorted(read_json("balance_default.json"), key=lambda person_dict: len(person_dict["text"].split()))
print(data_math_sort_by_len_text)