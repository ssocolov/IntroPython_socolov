#
# Задание. data.json - файл с данными о некоторых математиках прошлого.
import os
import re
import json
from operator import itemgetter

os.chdir("DZ_files")


# 1. Необходимо написать функцию,
# которая считает эти данные из файла и возвращала содержимое файла в той же структкру, что и в файле. Параметр
# функции - имя файла.

def read_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


# print(read_json("data.json"))


# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.

# def sort_by_surname(data):
#     with open(data, "r", encoding='utf-8') as file:
#         sort_name = sorted(json.load(file), key=itemgetter('name'))
#         return sort_name
#
#
# print(sort_by_surname("data.json"))


# 3. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.

##### ЗАДАНИЕ НЕ ЗАКОНЧЕНО ВОЗНИКЛИ ТРУДНОСТИ

# def death_date(data):
#     with open(data, "r", encoding='utf-8') as file:
#         for record in json.load(file):
#             new_list = []
#             dates = (''.join(record["years"].split())).split("–")
#             death = int(dates[1].replace(".", "").replace("c", "").replace("BC", ""))
#             death = death * -1 if dates[1].find("BC") != -1 else death
#             new_list.append(death)
#             # record["death"] = death
#         return new_list
#
#
# print(death_date("data.json"))


# def death_date(date):
#     with open(date, 'r', encoding='utf-8') as file:
#         data = json.load(file)
#     years = re.findall(r'[0-9]+', data["years"])
#     return int(years[-1]) if "BC" in date["years"] else -int(years[-1])
#
#
# new_dict_list = sorted(json.load(), key=death_date)
#
# print(new_dict_list)


dict_list = read_json("data.json")


def key_sorted_by_data(obj_dict):
    years = re.findall(r'[0-9]+', obj_dict["years"])
    return int(years[-1]) if "BC" in obj_dict["years"] else -int(years[-1])


new_dict_list = sorted(dict_list, key=key_sorted_by_data)

# print(new_dict_list)


# 4. Написать функцию сортировки по количеству слов в поле "text".


def sort_by_len_text(person_dict):
    return len(person_dict["text"].split())


data_math_sort_by_len_text = sorted(read_json("data.json"), key=lambda person_dict: len(person_dict["text"].split()))
# print(data_math_sort_by_len_text)
