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

# value = 99
# new_value = value // 2 if value > 100 else - value
# print(new_value)


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
