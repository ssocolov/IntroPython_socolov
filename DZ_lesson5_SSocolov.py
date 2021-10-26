# 1) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена самых молодых.
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
# в) Посчитать среднее количество лет всех людей из списка.
# Это одно задание. При выполнении пунктов можно использовать объекты полученные в предыдущих пунктах.
####################################################################################################################

# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена самых молодых. #########

# persons = [{"name": "John", "age": 15}, {"name": "Jack", "age": 15}, {"name": "Nick", "age": 32},
#            {"name": "Ben", "age": 45}]
# list_person = []
# min_age = float('inf')
# for person in persons:
#     if person["age"] < min_age:
#         min_age = person["age"]
# names_min_age = [person["name"] for person in persons if person["age"] == min_age]
# print(names_min_age)
####################################################################################################################

# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.########
#
# persons = [{"name": "John", "age": 15}, {"name": "Jack", "age": 15}, {"name": "Nick", "age": 32},
#            {"name": "Ben", "age": 45}]
# list_name = []
# max_len = float('-inf')
# for person in persons:
#     if len(person["name"]) > max_len:
#         max_len = len(person["name"])
# names_max_len = [persons['name'] for persons in persons if len(persons['name']) == max_len]
# print(names_max_len)
####################################################################################################################

# в) Посчитать среднее количество лет всех людей из списка.  #######################

# import statistics
#
# persons = [{"name": "John", "age": 15}, {"name": "Jack", "age": 15}, {"name": "Nick", "age": 32},
#            {"name": "Ben", "age": 45}]
# results = []
# for item in persons:
#     results.append(item['age'])
# res_mean = statistics.mean(results)
# print(res_mean)
######################################################################################################################

# 2) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
# {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}
# Это одно задание. При выполнении пунктов можно использовать объекты полученные в предыдущих пунктах.

##################################################################################################################
# а) Создать список из ключей, которые есть в обоих словарях.#####################################################

# my_dict_1 = {1:1, 2:1, 3:2, 4:7, 5:9, 6:13}
# my_dict_2 = {1:2, 2:1, 3:5, 4:7, 5:9, 6:12}
# def operator_important(my_dict_1, my_dict_2):
#     new_dict = dict()
#     for key, value in my_dict_1.items():
#         if key in my_dict_2 and value == my_dict_2[key]:
#             new_dict[key] = value
#
#     return new_dict
# d = operator_important(my_dict_1, my_dict_2)
# print(list(d))

######################################################################################################################
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.######################################

# my_dict_1 = {1:1, 2:1, 3:2, 4:7, 5:9, 6:13}
# my_dict_2 = {1:2, 2:1, 3:5, 4:7, 5:9, 6:12}
# def operator_important(my_dict_1, my_dict_2):
#     new_dict = dict()
#     for key, value in my_dict_1.items():
#         if key in my_dict_2 and value != my_dict_2[key]:
#             new_dict[key] = value
#
#     return new_dict
# d = operator_important(my_dict_1, my_dict_2)
# print(list(d))

######################################################################################################################
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.#######

# my_dict_1 = {1:1, 2:1, 3:2, 4:7, 5:9, 6:13}
# my_dict_2 = {1:2, 2:1, 3:5, 4:7, 5:9, 6:12}
# def operator_important(my_dict_1, my_dict_2):
#     new_dict = dict()
#     for key, value in my_dict_1.items():
#         if key in my_dict_2 and value != my_dict_2[key]:
#             new_dict[key] = value
#
#     return new_dict
# d = operator_important(my_dict_1, my_dict_2)
# print(d)

#######################################################################################################################
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
# {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}###########################################################

# my_dict_1 = {1:1, 2:1, 3:2, 4:7, 5:9, 6:13, 7:65}
# my_dict_2 = {1:2, 2:1, 3:5, 4:7, 5:9, 6:12, 8:33}
#
# res = dict()
#
# for item in my_dict_1.items():
#     if item[0] not in my_dict_2:
#         res[item[0]] = item[1]
#     else:
#         res[item[0]] = [item[1], my_dict_2[item[0]]]
# for item in my_dict_2.items():
#     if item[0] not in my_dict_1:
#         res[item[0]] = item[1]
#     else:
#         res[item[0]] = [item[1], my_dict_1[item[0]]]
# print(res)
######################################################################################################################
######################################################################################################################
#
# 3. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.

# my_list = ["qwe", "asd", "zxc", "qaz", "xsw", "edc"]
#
# def new_list(my_list):
#     result = []
#     for index in range(len(my_list)):
#         if index % 2:
#             result.append(my_list[index][::-1])
#         else:
#             result.append(my_list[index])
#     return result
#
# print(new_list(["qwe", "asd", "zxc", "qaz", "xsw", "edc"]))

#####################################################################################################################
#
# 4.Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.случайное_число_от_100_до_999@строка_случайных_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
#
# Пример использования функции:
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(domains, names)
# print(e_mail)
# >>>miller.249@sgdyyur.com

#
import random
import string


def new_email():
    return str(random.choice(names)) + '.' + str(rand_numb) + '@' + str(rand_word) + '.' + str(random.choice(domains))


names = ["John", "Pieter", "Sam", "Jim"]
domains = ["com", "org", "net", "ua"]
rand_numb = random.randint(100, 999)
rand_word = random.choice(string.ascii_lowercase)
# for s in range(randint(5, 7)):

# e_mail = str(random.choice(names)) + '.' + str(rand_numb) + '@' + str(rand_word) + '.' + str(random.choice(domains))

print(str(new_email()))
