# 1. Написать функцию, которая принимает в виде параметра целое число - количество цитат.
# и возвращает список оветов сервиса http://forismatic.com/ru/api/.
# Если автор не указан, цитату не брать. Цитаты не должны повторяться.
##
# 2. Написать функцию, которая принимает результат предыдущей функции и сохраняет в csv файл.
# ВАЖНО!!! -10 баллов за невыполнение этих пунктов!!!
# 1) Имя файла сделать параметром по умолчанию.
# 2) Заголовки csv файла: Author, Quote, URL.
# 3) Перед сохранением в csv, записи отсортировать по автору (в алфавитном порядке).

import requests
import random
import csv

def get_unique_quote(number):
    unique_quotes = []
    quote_dict = {}
    while len(unique_quotes) != number:
        url = "http://api.forismatic.com/api/1.0/"
        params = {"method": "getQuote",
                  "format": "json",
                  "key": random.randint(1, 999999)
                  }
        response = requests.get(url, params=params)
        raw_quote = response.json()
        if len(raw_quote['quoteAuthor']) != 0:
            quote_dict['Author'] = raw_quote['quoteAuthor']
            quote_dict['Quote'] = raw_quote['quoteText']
            quote_dict['URL'] = raw_quote['quoteLink']
            unique_quotes.append(quote_dict)
        quote_dict = {}
    return unique_quotes
print(get_unique_quote(10))


def write_to_csv(number, filename='unique_quotes.csv'):
    data = get_unique_quote(number)
    sorted_data_by_author_name = sorted(data, key=lambda x: x.get('Author'))
    fieldnames = data[0].keys()
    with open(filename, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sorted_data_by_author_name)


write_to_csv(10)