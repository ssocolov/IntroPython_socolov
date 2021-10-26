# Словари, методы словарей
# Модули
# Функции

# my_dict = {"name": "John", "age": 23}  # изменяемый, итерируемый тип данных. Порядок ключей не гарантируется!
# print(my_dict, type(my_dict))
# print(my_dict["name"])
# print(my_dict.get("name"))

# person = {"name": "John", "age": 23}
# person_datails = {"sex": "Female", "address": "Dnipro", "name": "Jane"}
# new_person = dict()  # создание ноовго словаря
# new_person.update(person)
# new_person.update(person_datails)

# new_person = {**person, **person_datails}   # соединение двух словарей
# print(new_person)

# person["sex"] = "Male"      # добавление данных в словарь вариант 1
# person.update(person_datails)
# print(person)
# person["sex"] = "Male"
# # person.update({"sex": "Male"})   # добавление данных в словарь вариант 2
# print(person)

# my_tuple = (("name", "John"), ("age", 23))
# my_list = [("name", "John"), ["age", 23]]
# person = dict(my_list)
# print(person)

# address = {"city": "Dnipro", "street": "Polya", "ZIP": 49000}
# skills = {"hard": ["python", "html", "DB", "C++"], "soft": []}
# person = {"name": "John", "age": 23, "skills": skills}
# person_datails = {"sex": "Male", "address": address}
# new_person = {**person_datails, **person}
# new_person["skills"]["hard"].append("JS")
# print(new_person)
# print(new_person["address"]["city"])


#
# my_dict = {1:11, (1,2, 3): "test", "1": "TEST"}
# print(11 in my_dict)   # in "смотрит" только в ключи
#
# print(my_dict.keys())   # dict_keys - почти список ключей
# keys = list(my_dict.keys())   # приведение к типу список
# values = my_dict.values()   # dict_values - "почти" список значений
# items = my_dict.items()
# print(items)


# my_dict = {"val_1": 12, "val_2": 24, "val_3": 6, "val_4": 58}
# res_values = []
# res_keys = []
# for value in my_dict.values():
#     if value > 10:
#         res_values.append(value)
#         res_keys.append(key)
# print(res_values)
# print(res_keys)


# print(values)
# for value in values:
#     print(value)

# my_temp_dict = {11: 1, 12: 2, 13: 3}
# if len(my_temp_dict.values()) == len(set(my_temp_dict.values())):

# print(my_temp_dict)
# temp_revers_dict = {value: key for key, value in my_temp_dict.items()}
# print(temp_revers_dict)
#

# my_str = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqa"
# res =[]
# for symb in my_str:
#     if my_str.count(symb) == 1:
#         res.append(symb)
# print(res)

# использование модулей, пакетов, библиотек
# import random   # импорт всего модуля
# # from random import randint        # импорт конкретной функции
# from string import ascii_lowercase as alphabet

# value = random.randint(1, 10)
# print(value)
#
# my_list = ["True", "False", "Unknown"]
# my_choice = random.choice(my_list)
# print(my_choice)
#
# random.shuffle(my_list)   # shuffle перемешивает текущею последовательность
# print(my_list)
#
# alphabet_list = list(alphabet)
# print(alphabet, type(alphabet))


# функции
# import random
# # #
# # #
# def create_random_int_number_list(len_list=5):
#     numbers = [random.randint(1, 10) for _ in range(len_list)]
#     return numbers
# # #
#
# def print_dict(some_dict):  # создание своей функции print # всё что используем-ПЕРЕДАЁМ В ФУНКЦИЮ!!!
#     for key, value in person.items():
#         print(f"{key}: {value}")
#
#
# my_dict = {"val_1": 12, "val_2": 24, "val_3": 6, "val_4": 58}
# person = {"name": "John", "age": 23, "sex": "Male", }
# #
# print(person)
# print(dict(person))
# print(dict(some_dict=my_dict))
# len_list = random.randint(10, 20)
# result = create_random_int_number_list()
# print(result)
