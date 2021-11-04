# форматы json, csv
# импорт из файлов ####
# assert
# функции сортировки
# регулярные выражения (введение)

############################################ регулярные выражения
import re

my_str = "c.965 - c. 1040"
numbers = re.findall(r"[0-9]+", my_str)
print(numbers)

############################## импорт из файлов
# from DZ_lesson5_SSocolov import new_email
#
# names = ["John", "Pieter", "Sam", "Jim"]
# domains = ["com", "org", "net", "ua"]
#
# email = new_email(names, domains)
# print('4)', email)



# форматы json, csv #################################################
import json

# def read_json(filename):
#     with open(filename, "r") as file:
#         some_data = json.load(file)
#         return some_data
#
# def write_json(filename, some_data):
#     with open(filename, "w") as file:
#         json.dump(some_data, file, indent=4)
#
# some_data = {"data": [12, 23, 34, 45],
#              "date": "2021-10-30",
#              "age": 50}
# filename = "some_data.json"
# data = read_json(filename)
# print(data)
#
# data["name"] = "John"
# wrine_json(filename, data, 8)

# my_list = [1, 2, 3,]
#
# my_list_str_json = json.dumps(my_list)
# print(my_list_str_json, type(my_list_str_json))
#
# new_list = json.loads(my_list_str_json)
# print(new_list)

# csv #################################
# import csv
# filename = "test_2.csv"
# # with open(filename, 'r', encoding="utf-8") as csv_file:
# #     reader = csv.reader(csv_file, delimiter=';')   # считывает всегда в виде строк
# #     data = []
# #     for row in reader:
# #         data.append(row)
# #
# #
# # print(data)
# # data.append([10, 11, 12])
# #
# # with open("test_2.csv", 'w') as csv_file:
# #     writer = csv.writer(csv_file)
# #     writer.writerows(data)
#
# with open(filename, 'r', encoding="utf-8") as csv_file:
#     reader = csv.DictReader(csv_file, delimiter=',')
#     data = []
#     for row in reader:
#         data.append(row)
#
# for row in data:
#     row["Total"] = int(row["Total"]) + 10
# print(data)
#
# with open("test_3.csv", 'w', encoding="utf-8") as сым_+file:
#     # fieldnames = list(data[0].keys())
#     fieldnames = ['Column_1', 'Column_2', 'Column_3', 'Total"]
#     print()
#                   ...................


# assert #########################
#
# price = 10
# assert price > 0, "Negative price"
# value_coef = 100 / price
# print(value_coef)


# функции сортировки ###########

# def sort_by_age(person_dict):
#     age = person_dict["age"]
#     return age
#
# def sort_by_len_name(person_dict):
#     name = person_dict["name"]
#     return len(name)
#
# def sort_by_len_name_and_age(person_dict):
#     name = person_dict["name"]
#     age = person_dict["age"]
#     return len(name), age
#
# persons = [{"name": "John", "age": 15}, {"name": "Nick", "age": 33},
#            {"name": "Jacky", "age": 15}, {"name": "Ben", "age": 49}]
#
# sort_by_age = sorted(persons, key=sort_by_age)
# print(sort_by_age)
# sort_by_len_name = sorted(persons, key=sort_by_len_name)
# print(sort_by_len_name)
# sort_by_len_name_and_age = sorted(persons, key=sort_by_len_name_and_age)
# print(sort_by_len_name_and_age)


# sort_person_by_age = sorted(persons)
# print(sort_person_by_age)

# temperature = [-2, -4, -6, -3, 0, 3, 5, -1, -4]
# sort_temp = sorted(temperature, key=abs)
# print(sort_temp)

# words= ['ajsyg', 'jasy', 'qwe', '124', 'wetertsdf', 'd']
# sort_words = sorted(words, key=len)
# print(sort_words)


