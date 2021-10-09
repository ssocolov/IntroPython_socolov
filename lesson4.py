
"""
1) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str.
Напечатать ЧИСЛО сколько раз my_symbol встречается в my_str.
Пример:  my_str="blablacar", my_symbol="bla".
Вывод на экран:
2
"""

# my_str = "blablacarblablacar"
# my_symbol = "bla"
# # result = my_str.count(my_symbol)  # метод count более подходящий
# new_str = my_str.replace(my_symbol, '')
# result = (len(my_str) - len(new_str)) // len(my_symbol)
# print(result)

"""
2) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str. 
Напечатать столько раз my_symbol, сколько он встречается в my_str. 
Пример:  my_str="blablacar", my_symbol="bla". 
Вывод на экран:
bla
bla
"""
# my_str = "blablacar"
# my_symbol="bla"
#
# my_symbol_count = my_str.count(my_symbol)
#
# # result = f"{my_symbol}\n" * my_symbol_count
# # result = result.strip()
# # print(result)
#
# for _ in range(my_symbol_count):
#     print(my_symbol)

"""
3) У вас есть переменная my_str, тип - str. Напечатать ЧИСЛО сколько 
РАЗНЫХ символов встречается в my_str. 
Большая и маленькая буква считается как один символ. 
Пробелы, запятые и т.д. считаем тоже как символы.
Пример:  my_str="bla BLA car". 
Вывод на экран:
6
"""
# my_str = "bla BLA car"
# lower_str = my_str.lower()
# unique_symbols = []
# for symbol in lower_str:
#     if symbol not in unique_symbols:
#         unique_symbols.append(symbol)
# unique_symbols_count = len(unique_symbols)
# print(unique_symbols_count)


"""
4)
Дана строка my_str и пустой список my_list.
Заполнить my_list символами из my_str, 
которые стоят на четных местах в строке (считаем с 0)
"""




# my_str = "wepotrpjhpoerpowet"
# my_list = [111]
# print(id(my_list), my_list)
# new_str = my_str[::2]
# # for symbol in new_str:
# #     my_list.append(symbol)
# my_list += list(new_str)  # не то же самое, что my_list = my_list + list(new_str)
#
# print(id(my_list), my_list)




"""
5)
Дана строка my_str, список str_index целых чисел в диапазоне от 
0 до длинны строки минус 1, пустой список my_list.
Заполнить my_list символами из my_str, которые стоят на местах с 
индексами из str_index
"""
# from string import ascii_lowercase as alphabet
#
# my_str = alphabet
# str_index = [6, 5, 7, 7, 1, 4, 2, 3, 7, 3]
# my_list = []
# for index in str_index:
#     symbol = my_str[index]
#     my_list.append(symbol)
# print(my_list)

"""
6)
Дано целое число (int). Определить сколько цифр в этом числе.
"""
# number = 13224545767345253445654643
# digit_count = len(str(number))
# print(digit_count)

"""
7)
Дано целое число. Определить наибольшую цифру в этом числе.
"""
# number = 13224545876734528534456548643
# max_symbol = max(str(number))
# print(max_symbol)

"""
8)
Дано целое число. Составить число (int) с цифрами в обратном порядке.
"""
# number = 13224545876734528534456548643
#
#  numb_str = str(number)
#  result_numb = int(numb_str[::-1])    # одно и тоже
#
# result_number = int(str(number)[::-1])    # одно и тоже
#
# print(result_number)
"""
9)
Дано целое число. Составить число с цифрами в порядке возрастания(убывания).
"""
# number = 13224545876734520853445065480643
# numb_str = str(number)
# sort_numb_list = sorted(numb_str , reverse=True)
# # new_number = "".join(sort_numb_list)
# # new_number = "".join(sort_numb_list[::-1])
# new_number = "".join(sort_numb_list)
# result = int(new_number)
# print(result)

#___________________________________________

# my_list = [3, 6, 1, 8]
# my_list = sorted(my_list, reverse=True)   # создает новый список и сортирует его
# # my_list.sort(reverse=True)  # сортирует текущий список
# print(my_list)



"""
10) Даны списки my_list_1 и my_list_2.
Создать список my_result в который поместить элементы из my_list_1 и
my_list_2 через один, начиная с my_list_1.
а) кол-во эл-тов одинаковое
б) кол-во эл-тов разное. Оставшиеся дописать в конец.
"""
# my_list_1 = [1, 2, 3]
# my_list_2 = [10, 20, 30, 40 ,50]
# my_result = []
#
#
# for index in range(len(my_list_1)):
#     # my_result.extend([my_list_1[index], my_list_2[index]])
#     my_result.append(my_list_1[index])
#     my_result.append(my_list_2[index])
# print(my_result)


# my_list_1 = [1, 2, 3, 4, 5, 6, 7, 8]
# my_list_2 = [10, 20, 30, 40, 50]
# my_result = []
#
# min_len_lists = min(len(my_list_1), len(my_list_2))
# tail = my_list_1[min_len_lists:] + my_list_2[min_len_lists:]
# print(tail)
# for index in range(min_len_lists):
#     my_result.append(my_list_1[index])
#     my_result.append(my_list_2[index])
# my_result.extend(tail)
# print(my_result)



##############################################



# # ord(), chr()
# print(ord('A'))  #выводит номер символа в таблице 65
# print(chr(34))   # выводит символ по номеру "

# Генераторы списков (list comprehension)
# alphabet_list = []
# for index_ascii in range(ord('a'), ord('z') +1):
#     alphabet_list.append(chr(index_ascii))

# alphabet_list = [chr(index_ascii) for index_ascii in range(ord('a'), ord('z') +1)]
#
# alphabet_list = "".join(alphabet_list)
#
# print(alphabet_list)
#
# # _________________________________________________
# result = [x ** 2 for x in range(25)]
# print(result)
##############################################################

# my_list = [12, -45, 23, 5, 0, 21, 900]
# res = [value for value in my_list if value > 10]
# print(res)
# ответ [12, 23, 21, 900]

# my_list = [12, -45, 23, 5, 0, 21, 900]
# res = [str(value) * 20 for value in my_list if value > 10]
# # for line in res:   # или
# #     print(line)
# [print(line) for line in res]  # или



# #####################################################
# множества (set) - изменяемый тип, только один представитель для каждого объекта, порядок не сохраняется
############### пересмотреть ##########################
# my_list = [1, 2, 3, 4, "5", 5, 5, "1"]
#
# my_set = set(my_list)
# print(my_set, type(my_set))


# unique_symbols_count = len(set(my_str.lower()))
# print(unique_symbols)
#найти символы которые.... пересекаются, объединяются, есть в первом только множестве
# my_str_1 = "rtuyuoefojhgiejgtperwoitperptiore"
# my_str_2 = "eriughdfkfasljhflesrjg;ldfkmnblshf;fkjbn"
# my_str_1_set = set(my_str_1)
# my_str_2_set = set(my_str_2)

# same_symbols = my_str_1_set.intersection(my_str_2_set)  # пересечение
# print(same_symbols)

# all_symbols = my_str_1_set.union(my_str_2_set)  # объединение
# print(all_symbols)

# first_str_unique = my_str_1_set.difference(my_str_2_set)  # только символы которые есть в первой строке, но нет во второй
# print(first_str_unique)









