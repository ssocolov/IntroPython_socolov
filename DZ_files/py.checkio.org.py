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


# текст между маркерами

# import re
#
# def between_markers(string, start, end):
#     len_until_end_of_first_match = string.find(start) + len(start)
#     after_start = string[len_until_end_of_first_match:]
#     return string[string.find(start) + len(start):len_until_end_of_first_match + after_start.find(end)]


# Найдите ближайшее значение к переданному.
#
# Вам даны список значений в виде множества (Set) и значение, относительно которого, надо найти ближайшее.
#
# Например, мы имеем следующий ряд чисел: 4, 7, 10, 11, 12, 17. И нам нужно найти ближайшее значение к цифре 9. Если отсортировать этот ряд по возрастанию, то слева от 9 будет 7, а справа 10. Но 10 - находится ближе, чем 7, значит правильный ответ 10.
#
# Несколько уточнений:
#
# Если 2 числа находятся на одинаковом расстоянии - необходимо выбрать наименьшее из них;
# Ряд чисел всегда не пустой, т.е. размер >= 1;
# Переданное значение может быть в этом ряде, а значит оно и является ответом;
# В ряде могут быть как положительные, так и отрицательные числа, но они всегда целые;
# Ряд не отсортирован и состоит из уникальных чисел.
#
# def nearest_value(values: set, one: int) -> int:
#     return min(values, key=lambda n: (abs(one - n), n))


# На вход Вашей функции будет передано одно предложение. Необходимо вернуть его исправленную копию так, чтобы оно всегда начиналось с большой буквы и заканчивалось точкой.

# def correct_sentence(text ) -> str:
#
#     text = text[0].upper() + text[1:]
#     if(text[-1] != '.'):
#         text += '.'
#
#     return text


# Остров 2

# https://py.checkio.org/station/home/
# все, до задачи Popular Words (включительно)

# Вам дан текст в котором нужно просуммировать числа, но только разделенные пробелом. Если число является частью слова, то его суммировать не нужно.
# Текст состоит из чисел, пробелом и английского алфавита.
text = 'Petersen between 1845 and 1910 year'
def sum_numbers(text: str) -> int:
    return sum(int(i) for i in str.split(text) if i.isdigit())

# print(sum_numbers(text))

# Дан массив целых чисел. Нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд), затем перемножить эту сумму и последний элемент исходного массива.
# Не забудьте, что первый элемент массива имеет индекс 0.
# Для пустого массива результат всегда 0 (ноль).

def checkio(array):
    if len(array) == 0:
        return False

    b = 0
    for index in range(len(array)):
        if index % 2 == 0 and index <= 20:
            b = b + array[index]
    return b * array[index]

# Давайте научим наших роботов отличать слова от чисел.
# Дана строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами). Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд. Для примера, в строке "start 5 one two three 7 end" есть три слова подряд.
# Входные данные: Строка со словами (str).
# Выходные данные: Ответ как логическое выражение (bool), True или False.

def checkio(words):
    count = 0

    for index in words.split():

        if index.isalpha():
            count += 1
            if count == 3:
                return True
        else:
            count = 0

    return False


# Один робот был занят простой задачей: объединить последовательность строк в одно выражение для создания инструкции по обходу корабля. Но робот был левша и зачастую шутил и запутывал своих друзей правшей.
# Дана последовательность строк. Вы должны объединить эти строки в блок текста, разделив изначальные строки запятыми. В качестве шутки над праворукими роботами, вы должны заменить все вхождения слова "right" на слова "left", даже если это часть другого слова. Все строки даны в нижнем регистре.

my_tuple = ("left", "right", "left", "stop")
def left_join(phrases: tuple) -> str:
    return ",".join(list(phrases)).replace("right", "left")
# print(left_join(my_tuple))


# Дана строка и нужно найти ее первое слово.
# При решении задачи обратите внимание на следующие моменты:
# В строке могут встречатся точки и запятые
# Строка может начинаться с буквы или, к примеру, с пробела или точки
# В слове может быть апостроф и он является частью слова
# Весь текст может быть представлен только одним словом и все
# Входные параметры: Строка.
# Выходные параметры: Строка.
import re
pattern=r"[a-zA-Z']+"
def first_word(words_tuple):
    match=re.findall(pattern,words_tuple)
    for i in match:
        if i[0].isalnum():
            return i

# print(first_word("new.text"))




# разница между датами в днях(не решено)

from datetime import datetime

# def days_between(d1, d2):
#     d1 = d1.strftime("%Y-%m-%d")
#     d2 = d2.strftime("%Y-%m-%d")
#     return abs((d2 - d1).days)
#
# print(days_between((1982, 4, 19), (1982, 4, 22)))
# def days_diff(a, b):
#     d1 = datetime.strptime(a, "%d.%m.%Y")
#     d2 = datetime.strptime(b, "%d.%m.%Y")
#     x = (d2 - d1).days
#     return x
# print(days_diff((1982, 4, 19), (1982, 4, 22)))



# Вам нужно подсчитать количество цифр в данной строке.
import re

def count_digits(text):
    count = sum([ 1 for text in text if text.isdigit() ])
    return count

# print(count_digits('5my 6 num2be4rs is 2'))



# Требуется обратить порядок букв в каждом слове предоставленной строки, так чтобы слова остались на своих местах.
s = 'hello world'
lst1 = s.split()



print(lst1)