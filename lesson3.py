# ###########################################################################
# count = 0
# do_loop = True
#
# while do_loop:
#     print("This is while loop", count)
#     count += 1
#     if count >= 10:
#         do_loop = False
# #################################
# count = 0
# do_loop = True
#
# while do_loop:
#     print("This is while loop", count)
#     count += 1
#     if count >= 10:
#         break







#################################################################################
# Кортежи (tuple) и списки [list]
# итерируемые объекты
# my_tuple = (1, -10, "qwe", True, 3.14, (-2, 0), ["a", "z"])   # пример кортежа
# my_list = [1, -10, "qwe", True, 3.14, (-2, 0), ["a", "z"]]    # пример списка

# print(my_tuple, type(my_tuple))
# print(my_list, type(my_list))
# index = 2
# print(my_tuple[index], my_list[index])
# print(len(my_tuple), len(my_list))

# срезы как у строк!!!!
# new_tuple = my_tuple[::-1]      # перевернул с конца
# print(new_tuple)
#
# for value in my_list:         # выбрать из списка
#     if type(value) == int:    # значения которые являются числом (int)
#         print(value)
# ##################################################################### отличия
# my_tuple = (1, -10, "qwe", True, 3.14, (-2, 0), ["a", "z"])  # не изменяемый тип данных
# my_list = [1, -10, "qwe", True, 3.14, (-2, 0), ["a", "z"]]   # изменяемый тип данных

# my_list[0] = 100        # заменяет нулевой элемент списка на заданное значение
#
# print(my_list)
#
# my_tuple[0] = 100  # выдаст ошибку так как запрещено
# my_tuple[0] = (100, *my_tuple[1:])
# print(my_tuple)

# распаковка кортежей и списков
# val_1 = 12
# val_2 = 21
# val_1, val_2 = val_2, val_1

# item = val_2, val_1
# print(item, type(item))
# val_1, val_2 = item
# print(val_1, val_2)
#
# my_tuple = (1, 2, "qwe")
# val_int_1, val_int_2, my_str = my_tuple
# print(val_int_1, val_int_2)


# my_tuple = (1, (-2, 0), ["a", "z"])  # не изменяемый тип данных
# my_list = [1, (-2, 0), ["a", "z"]]   # изменяемый тип данных
# my_list[-1][0] = 100
# print(my_tuple)

# 1 2
# 3 24

# my_table = [[1, 2], [3, 4]]
# my_table[1][1] = 24
# print(my_table)
#
# my_tuple = (1, 2, 3)
# print(id(my_tuple))
# my_tuple = (100, *my_tuple[1:])
# print(id(my_tuple))
#
# list_1 = [1, 2]
# list_2 = [3, 4]
#
# new_list = [list_1.copy(), list_2[:]] # срез это всегда копия
# print(new_list)
#
# list_1[0] = 100
# list_2[0] = 300
# print(new_list, list_1)


# value = [10, 20]
# new_list = [value.copy()] * 5
# value[0] = 100
# print(new_list)

############################################################################################
# new_list = []
#
# for symbol in "qwerty":
#     new_list.append(symbol)
# new_list.append(1000)
# print(new_list)
#
# new_list.pop(0)
# print(new_list)
#
# new_tuple = ("qwerty", "asdfgh")
# new_list = list(new_tuple)
# new_list[0] = 123
# print(new_list)
# new_tuple = tuple(new_list)
# print(new_tuple)
#
# new_list = list("new_tuple")
# print(new_list)
# new_list = ["1", "2", "0.3]
# new_str = "$".join(new_list)
# print(new_str)

# filename = "lesson3.py.txt"
# filename = filename.replace(".txt", "")
# filename_parts = filename.split(".")
# filename = ".".join(filename_parts[:-1])

# filename = filename.rsplit(".", 1)[0]   # rsplit разделение с конца
# print(filename)



###########################################################################################
# цикл for
# for врем_перем in итер_объект:
#    итерация

# my_str = "qwerty 123 #%$ ASD"

# for symbol in my_str:
#     if symbol.isdigit():
#         print(symbol)


# for symbol in my_str:
#     if not symbol.lower() in "eyuioa":
#         print(symbol)









########################################################################################
# обоработка исключений

# value = input("Введи целое число")
#
# try:                            # попробуй
#     value_int = int(value)
#     result = 1 / value_int
#     print(result)
# except ValueError:
#     print("Это не число!!!")
# except ZeroDivisionError:
#     print("На ноль делить нельзя!!")
#
#####################################################################################
# игра угадай число

# from random import randint
# min_limit = 10
# max_limit = 20
# comp_value = randint(min_limit, max_limit)
# cur_value = int(input(f"Угадай число от {min_limit} до {max_limit}:"))
# go_game = True
# while cur_value != comp_value:     # условие отсекает все что ниже и сразу выводит победу
#     case_word = "меньше" if cur_value > comp_value else "больше"
#     cur_value = int(input(f"Попробуй число {case_word}"))

    # if cur_value > comp_value:
    #     cur_value = int(input("Попробуй число меньше"))
    # elif cur_value < comp_value:
    #     cur_value = int(input("Попробуй число больше"))
    # else:
    #     go_game = False
    #
    #     print("Победа!!")
