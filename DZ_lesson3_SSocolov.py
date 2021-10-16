# Домашнее задание 3
############################################################################################

# 1) У вас есть список my_list с значениями типа int.
# Распечатать те значения, которые больше 100.
# Задание выполнить с помощью цикла for.

# my_list = [1, 3, 6, 45, 65, 77, 99, 100, 123, 134, 145, 144]
# for symbol in my_list:
#     if symbol > 100:
#         print(symbol)

##############################################################################################

# 2) У вас есть список my_list с значениями типа int, и пустой список my_results.
# Добавить в my_results те значения, которые больше 100.
# Распечатать список my_results.
# Задание выполнить с помощью цикла for.
#

# my_list = [1, 3, 6, 45, 65, 77, 99, 100, 123, 134, 145, 144]
# my_results = []
# for symbol in my_list:
#     if symbol > 100:
#         my_results.append(symbol)
# print(my_results)

####################################################################################################

# 3) У вас есть список my_list с значениями типа int.
# Если в my_list количество элементов меньше 2, то в конец добавить значение 0.
# Если количество элементов больше или равно 2, то добавить сумму последних двух элементов.
# Количество элементов в списке можно получить с помощью функции len(my_list)
#
# my_list = [1, 2, 3]
# if (len(my_list)) < 2:
#     my_list.append(0)
# elif (len(my_list)) >= 2:
#     my_list.append(my_list[-1] + my_list[-2])
# print(my_list)

# my_list = [1, 2, 3]
# if (len(my_list)) < 2:
#     my_list.append(0)
# else:
#     my_list.append(my_list[-2] + my_list[-1])



# #####################################################
# Еще один пример - вложенные циклы (цикл в цикле).
# my_string_1 = "12"
# my_string_2 = "34"
# for symbol_1 in my_string_1:
# 	for symbol_2 in my_string_2:
# 		print(symbol_1 + symbol_2)


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

# my_string = '0123456789'
# res = []
# for symb_1 in my_string:
#     for symb_2 in my_string:
#         res.append(int(symb_1 + symb_2))
# print(res)