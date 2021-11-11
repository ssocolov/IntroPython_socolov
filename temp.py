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


# В данном списке первый элемент должен стать последним. Пустой список или список из одного элемента не должен
# измениться.

# def replace_first(my_list):
#     if my_list == []:
#         return []
#     my_list.append(my_list[0])
#     my_list.remove(my_list[0])
#     return my_list
#
#
# print(replace_first([1, 2, 3, 4]))

# самая большая цифра в числе

# def max_digit(a):
#     m_dig = max([int(i) for i in str(a)])
#     return m_dig
#
# print(max_digit(123))

# Разделите строку на пары из двух символов. Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен быть заменен подчеркиванием ('_').

# def split_pairs(pair_symb):
#     if len(pair_symb) % 2 != 0:
#         pair_symb = pair_symb + '_'
#     pair_symb = ([pair_symb[i:i +2]for i in range(0, len(pair_symb), 2)])
#     return pair_symb
# print(split_pairs('wetdsfsdf'))


# количество нулей в начале строки

# def end_zeros(num: int) -> int:
#     return min((i for i, c in enumerate(str(num)[::1], 0) if c != '0'), default=len(num))
#
# print(end_zeros('000'))


# проверка на четность. Четное True, нечетное False

# def is_even(num: int) -> bool:
#     if num % 2 == 0:
#         return True
#     else:
#         return False
#
#
# print(is_even(123))
