#############Lesson5_1

# https://pythonru.com/osnovy/python-dict

# # Словари, методы словарей
# # модули
# # функции
#
# # ######################### словари
# my_dict = {"name": "John", "age": 23}  # изменяемый, итерируемый тип данных. Порядок ключей не гарантируется!
# print(my_dict, type(my_dict))
# print(my_dict["name"])
# print(my_dict.get(111))
#
# ########################### конструирование сложных словарей
# address = {"city": "Dnipro", "street": "Polya", "ZIP": 49000}
# skils = {"hard": ["python", "html", "DB", "C++"], "soft": []}
# person = {"name": "John", "age": 23, "skils": skils}
# person_datails = {"sex": "Male", "address": address}
#
# ######################### описание структуры данных с помощью словарей
#
# person = {"name": "John",
#           "age": 23,
#           "sex": "Male",
#           "address": {"city": "Dnipro",
#                       "street": "Polya",
#                       "ZIP": 49000
#                       },
#           "skils": {"hard": ["python", "html", "DB", "C++"],
#                     "soft": []
#                     }
#           }
#
# ######################################### конструирование словаря через метод update
# new_person = dict()
# new_person.update(person)
# new_person.update(person_datails)
#
# new_person = {**person_datails, **person}
# print(new_person["address"]["city"])
# new_person["skils"]["hard"].append("JS")
# print(new_person)
# person.update(person_datails)
# print(person)
# person["sex"] = "Male"
# print(person)
#
# ######################################## приведение к типу dict
# my_tuple = (("name", "John"), ("age", 23))
# my_list = [("name", "John"), ["age", 23]]
# person = dict(my_list)
# print(person)
#
#
# ########################################## циклы и dict
#
# my_dict = {1: 11, (1, 2, 3): "test", "1": "TEST"}
# print(11 in my_dict)  # in  "смотрит" только в ключи
#
# print(my_dict.keys())  # dict_keys - "почти" список ключей ))
# keys = list(my_dict.keys())
# values = my_dict.values()   #dict_values - "почти" список значений
# items = my_dict.items()
# print(items)
#
#
# my_dict = {"val_1": 12, "val_2": 24, "val_3": 6, "val_4": 58}
#
# for key in my_dict:  # "идет" ТОЛЬКО ПО КЛЮЧАМ
#     print(key, my_dict[key])
#
# res_values = []
# res_keys = []
# for key, value in my_dict.items():
#     if value > 10:
#         res_values.append(value)
#         res_keys.append(key)
#
# print(res_values)
# print(res_keys)

###### lesson5_2

#######################################################################################
import random
import string


def new_email(param):
    names = str(random.choice(name))
    rand_numb = str(random.randint(100, 999))
    rand_word = str(random.choice(string.ascii_lowercase))
    domains = str(random.choice(["com", "org", "net", "ua", "ru"]))
    param = names + '.' + rand_numb + '@' + rand_word + '.' + str(random.choice(domains))
    return param


name = ["John", "Pieter", "Sam", "Jim"]
# domains = ["com", "org", "net", "ua", "ru"]
# rand_numb = random.randint(100, 999)
# rand_word = random.choice(string.ascii_lowercase)
# for s in range(randint(5, 7)):

# e_mail = str(random.choice(names)) + '.' + str(rand_numb) + '@' + str(rand_word) + '.' + str(random.choice(domains))
# new_email(name)
print(new_email(name))
#############################################################################################
# def Mult2(number):
#     number = number * 2
#     print("Mult2.number = ", number)
#
# num = 25
# Mult2(num)
#
# print("num = ", num)

# import random
# import string
#
#
# def new_email():
#     return str(random.choice(names)) + '.' + str(random.randint(100, 999)) + '@' + str(random.choice(string.ascii_lowercase)) + '.' + str(random.choice(domains))
#     # return str(random.choice(names)) + '.' + str(random.randint(100, 999)) + '@' + str(random.choice(string.ascii_lowercase)) + '.' + str(random.choice(domains))
#
#
# names = ["John", "Pieter", "Sam", "Jim", "Max"]
# domains = ["com", "org", "net", "ua", "ru"]
# # rand_numb = random.randint(100, 999)
# # rand_word = random.choice(string.ascii_lowercase)
# # for s in range(randint(5, 7)):
#
# # e_mail = str(random.choice(names)) + '.' + str(rand_numb) + '@' + str(rand_word) + '.' + str(random.choice(domains))
#
# print(new_email())


#####################################################################################################################################################################################################

# def create_random_int_number_list(len_list=5):
#     numbers = [random.randint(1, 10) for _ in range(len_list)]
#     return numbers
#
#
# def print_dict(some_dict):  # ВСЕ ЧТО ИСПОЛЬЗУЕМ - ПЕРЕДАЕМ В ФУНКЦИЮ!!!
#     for key, value in some_dict.items():
#         print(f"{key}: {value}")
#
#
# my_dict = {"val_1": 12, "val_2": 24, "val_3": 6, "val_4": 58}
# person = {"name": "John", "age": 23, "sex": "Male", }
#
# # print(person)
# # print_dict(person)
# # print_dict(some_dict=my_dict)
# len_list = random.randint(10, 20)
# result = create_random_int_number_list()
# print(result)
#
# # использование модулей, пакетов, библиотек
# import random  # импорт всего модуля
# # from random import randint  # импорт конкретной функции
# from string import ascii_lowercase as alphabet

# value = random.randint(1, 10)
# print(value)
# my_list = ["True", "False", "Unknown"]
# my_choice = random.choice(my_list)
# print(my_choice)

# alphabet_list = list(alphabet)
# print(alphabet_list, type(alphabet_list))
#
# random.shuffle(alphabet_list)
# print(alphabet_list)


# my_temp_dict = {11: 1, 12: 2, 13: 3}
# print(my_temp_dict)
#
# if len(my_temp_dict.values()) == len(set(my_temp_dict.values())) :
#     temp_revers_dict = {value: key for key, value in my_temp_dict.items()}
#     print(temp_revers_dict)

# my_str = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqa"
# res = []
# for symb in set(my_str):
#     if my_str.count(symb) == 1:
#        res.append(symb)
# print(res)


#######################################################################################################################
#######################################################################################################################

# Строки, списки, циклы. Генераторы списков, множества
# Сложение строк
# s1 = "spam"
# s2 = "eggs"
# print(s1 + s2)
# spameggs

# дублирование строки
# print("spam" * 3)
# spamspamspam

# Длина строки (len)
# print(len("spam"))
# 4

# доступ по индексу
# S = 'spam'
# S[0]
# s
# S[2]
# a
# S[-2]
# a

# cрезы
# my_str = 'spameggs'
# new_str = my_str[1::3]
# print(new_str)
# pes

# Списки
# print(list("список"))
# #['с', 'п', 'и', 'с', 'о', 'к']


# 1. Дано целое число (int). Определить сколько нулей в этом числе.
# my_int = str(1020030)
# my_count = "0"
# count = (len([my_count for my_count in my_int if my_count == "0"]))
# print(count)

# my_int = str(1020030)
# symbol = "0"
# result = my_int.count(symbol)
# print(result)

# 2. Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля
#
# my_int = 155006
# count = 0
# while my_int % 10 == 0:
#     count += 1
#     my_int //= 10
# print(count)

#######################################################################################################################
# 3. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit)
#

# my_str = "43 больше 34 но меньше 56"
# my_list = []
# for numbers in my_str.split():
#     if numbers.isdigit():
#         my_list.append(int(numbers))
# result = sum(my_list)
# print(result)

#######################################################################################################################
# 4. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".
#
# my_str = "My long string"
# new_str = str(my_str[::-1])
# l_limit = "o"
# r_limit = "g"
# sub_str = new_str[(new_str.find(r_limit) + 1): new_str.rfind(l_limit)]
# result = sub_str[::-1]
# print(result)


#######################################################################################################################
# 5. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".
# #
# my_list = 'abs' 'wog' 'scenic' 'abro'
# my_list = ['abs', 'gm', 'arm', 'esp']
# new_list = []
# for symbol in my_list:
#     if symbol.startswith('a'):
#         new_list.append(symbol)
# print(new_list)


#######################################################################################################################
# 6. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.
#
# my_list = ['abibas', 'cargo', 'gm', 'dell', 'calc', 'esp']
# new_list = []
# for symbol in my_list:
#     if symbol.count('a'):
#         new_list.append(symbol)
# print(new_list)

#######################################################################################################################
# 7. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Например [1, 2, 3, "11", "22", 33]
# Создать новый список в который поместить только строки из my_list.
# my_list = [1, 2, 3, "11", "22", 33]
# new_list = []
# for symbol in my_list:
#     if type(symbol) == str:
#         new_list.append(symbol)
# print(new_list)

#######################################################################################################################
# 8. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке ТОЛЬКО ОДИН раз.
# my_str = "qwerty2qwerty"
# my_list = []
# for symbol in set(my_str):
#     if my_str.count(symbol) == 1:
#         my_list.append(symbol)
# print(my_list)

#######################################################################################################################
# 9. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
#
# my_str_1 = "abblikbc3"
# my_str_2 = "aahkbcc4"
# my_list = list(set(my_str_1).intersection(set(my_str_2)))
# print(my_list)


#######################################################################################################################
# 10. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой ТОЛЬКО ПО ОДНОМУ разу.
# Пример: для строк "aaaasdf1" и "asdfff2" ответ ["s", "d"], т.к. эти символы есть в каждой строке по одному разу
#
# my_str_1 = "aaaasdf1"             # "to be or not to be?"
# my_str_2 = "asdfff2"              # "back to future?"
# my_list = []
# for i in my_str_1 :
#     k = my_str_1.find(i) - my_str_1.rfind(i)
#     if k == 0:
#         if i in my_str_2 and my_str_2.find(i) - my_str_2.rfind(i) == 0 :
#             my_list.append(i)
# print(my_list)


########################################################################################################################
# 11. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2)

# my_str = "abcde"


# DZ_lesson_3 test
######## 1

# values = [1, 2, 3, 4, 5]
# print(type(values))
# <class 'list'>

######## 2

# values = (1, 2, 3, 4, 5)
# print(type(values))
# <class 'tuple'>

######## 3

# values = (1, 2, 3, 4, 5)
# values = list(values)
# print(type(values))
# <class 'list'>

######## 4

# values = [1, 2, 3, 4, 5]
# values = tuple(values)
# print(type(values))
# <class 'tuple'>

###### 5

# values = [1, 2, 3, 4, 5]
# result = []
# for value in values:
#     result.append(value)
# print(result)
# [1, 2, 3, 4, 5]

###### 6

# values = [1, 2, 3, 4, 5]
# result = []
# for value in values[::-1]:
#     result.append(value)
# print(result)
# [5, 4, 3, 2, 1]

###### 7

# values = [1, 2, 3, 4, 5]
# print(len(values))
# 5

###### 8

# values = [1, 2, 3, 4, 5]
# new_value = values + values[::-1]       # переворот второго списка
# print(new_value)
# [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]

###### 9

# values = [1, 2, 3, 4, 5]
# new_value = values
# new_value.append(6)     # добавляет указанное значение в ?конец? (начало) списка
# print(values)
# [1, 2, 3, 4, 5, 6]

####### 10

# values = [1, 2, 3, 4, 5]
# new_value = values.copy()       # скопировали список
# new_value.append(6)             # добавили к новому(скопированному) списку 6
# print(values)                   # на печать вывели оригинальный список value
# [1, 2, 3, 4, 5]

###### 11

# values = [0] * 6        # умножили список
# values[0] = 1           # заменили нулевой символ на 1
# print(values)
# [1, 0, 0, 0, 0, 0]

####### 12

# value = 0
# values = [value] * 6  # сделали value списком и умножили на 6
# value = 1             # в данном случае не учитывается, так как выводим values
# print(values)
# [0, 0, 0, 0, 0, 0]

####### 13

# my_list = [0]
# values = [my_list] * 3
# print(values)
# [[0], [0], [0]]

######## 14

# my_list = [0]
# values = [my_list] * 3      # сделали my_list списком со списком внутри, умножили список на 3
# my_list.append(1)           # добавили 1
# print(values)
# [[0, 1], [0, 1], [0, 1]]

###### 15

# my_list = [0]
# values = [my_list.copy()] * 3       # скопировали список, копию умножили на 3 получили values
# my_list.append(1)                   # к изначальному списку my_list добавили 1
# print(values)                       # печатаем values, то есть копию
# [[0], [0], [0]]

###### 16

# my_list = ["a", "b", "c", "d", "e", "f"]
# my_str = " ".join(my_list)      # объединили список в строку методом join с разделением через пробел
# print(my_str)
# a b c d e f

###### 17

# my_list = ["a", "b", "c", "d", "e", "f"]
# my_str = "_".join(my_list)      # # объединили список в строку методом join с разделением через нижнее подчеркивание
# print(my_str)
# a_b_c_d_e_f

###### 18

# my_list = ["a", "b", "c", "d", "e", "f"]
# my_str = "_".join(my_list[::-1])        # список объединили в строку с разделением через нижнее подчеркивание и перевернули в обратную сторону[::-1]
# print(my_str)
# f_e_d_c_b_a

####### 19

# my_list = ["a", "b", "c", "d", "e", "f"]
# my_str = "".join(my_list[::2])          # объединили список в строку без разделения и срезали все четные символы
# print(my_str)
# ace
##########################################################################################################################
# Домашнее задание 3
# Задания:
# 1) У вас есть список my_list с значениями типа int.
# Распечатать те значения, которые больше 100.
# Задание выполнить с помощью цикла for.

# my_list = [1, 3, 6, 45, 65, 77, 99, 100, 123, 134, 145, 144]
# for symbol in my_list:
#     if symbol > 100:
#         print(symbol)


# 2) У вас есть список my_list с значениями типа int, и пустой список my_results.
# Добавить в my_results те значения, которые больше 100.
# Распечатать список my_results.
# Задание выполнить с помощью цикла for.


#
# 3) У вас есть список my_list с значениями типа int.
# Если в my_list количество элементов меньше 2, то в конец добавить значение 0.
# Если количество элементов больше или равно 2, то добавить сумму последних двух элементов.
# Количество элементов в списке можно получить с помощью функции len(my_list)
#
#
# #####################################################
# Еще один пример - вложенные циклы (цикл в цикле).
# my_string_1 = "12"
# my_string_2 = "34"
# for symb_1 in my_string_1:
# 	for symb_2 in my_string_2:
# 		print(symb_1 + symb_2)
#
#
#
# Результат:
# "13"	# перебирается все элементы из my_string_2 для элемента "1" из my_string_1
# "14"
# "23"	# перебирается все элементы из my_string_2 для элемента "2" из my_string_1
# "24"
# #####################################################
#
# 4) У вас есть строка my_string = '0123456789'.
# Сгенерировать целые числа (тип int) от 0 до 99 и поместить их в список.
# Задание нужно выполнить ТОЛЬКО через цикл в цикле(См. пример выше) и приведение типов.
# Генерирование через range или другие "фишки" я засчитывать не буду ))


#############################################################################################################################


#########################################################################################################################
########################################################################################################################
# num = int(input("введите целое число"))
# result = "четное" if num%2==0 else "нечетное число"
# print("Это " +result+" число")


# from random import randint
# case = randint(1, 6)
# # if case > 3:
# #      result = case ** 2
# # else:
# #      result = - case
#
# result = case ** 2 if case > 3 else -case
#
# print("Выпало число:", case, "Результат:", result)
# case = 0
# if case > 2:
#      result = case ** 2
# else:
#      result = - case
#
# # result = case ** 2 if case > 3 else -case
# print(not result)


# 6 (доработано)
#
# my_str = "Sergey"
# result: str = (my_str)    # нужно ли?
# if len(my_str) < 5:
#     result = (my_str) * 2
# elif len(my_str) >= 5:
#     result = (my_str)
# print(result)

###################################################################################
# 7 (доработано)

# my_str = "Serg"
# result: str = (my_str)    # нужно ли?
# if len(my_str) < 5:
#     result = (my_str + my_str[::-1])
# elif len(my_str) >= 5:
#     result = (my_str)
# print(result)
