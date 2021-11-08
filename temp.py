## первое слово в строке  #####

# def first_word(text):
#     new_txt = text.split()[0]
#     return new_txt
#
# text = "Hello world!"
# print(first_word(text))

## длина пароля больше 6 ####

# def is_acceptable_password(password):
#     if len(password) > 6:
#         return True
#     else:
#         return False
#
# print(is_acceptable_password("123453"))


## количество цифр в числе ####
#
# def number_lenght(a):
#     return len(str(a))
#
#
# print(number_lenght(17810))


## количество нулей вконце числа #####

# def count_zero(num):
#     num = len(str(num)) - len(str(num).strip('0'))
#     return num
#
# print(count_zero(1000023000000000))


## перевернуть слово наоборот ###########
# def mirror_text(text):
#     text = text[::-1]
#     return text
# print(mirror_text("aihpoS"))

## удалить символы до заданного #########
# from typing import Iterable
#
#
# def remove_all_before(items: list, border: int) -> Iterable:
#     k = j = 0
#     for i in items:
#         if i == border:
#             j = k
#             break
#         k += 1
#     return items[j:]
#
# print(list(remove_all_before([1, 2, 3, 4, 5], 3)))

## проверка на большие буквы ####

# def is_all_upper(text: str) -> bool:
#     if text.upper() == text:
#         return True
#     elif len(text) == 0:
#         return True
#     return False


from typing import Iterable


#
from typing import Iterable

#
# def replace_first(items: list) -> Iterable:
#     items = list.index(1, ())
#     return items
# print(replace_first([1, 2, 3, 4]))

my_list_1 = [1, 2, 3, 4]
# my_list_1.index(1)
my_list_2 = []

print(my_list_1.index(1))