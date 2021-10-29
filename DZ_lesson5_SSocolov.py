
# 1 ##################################
from collections import defaultdict
import statistics


persons = [{"name": "John", "age": 15}, {"name": "Nick", "age": 33},
           {"name": "Jacky", "age": 15}, {"name": "Ben", "age": 49}]

age_by_names = defaultdict(list)
len_name_by_names = defaultdict(list)
ages = []

for person in persons:
    name = person["name"]
    age = person["age"]
    age_by_names[age].append(name)
    len_name_by_names[len(name)].append(name)
    ages.append(age)

min_age = min(age_by_names)
print('min_age:', *age_by_names[min_age])

max_len_name = max(len_name_by_names)
print('max_len_name:', *len_name_by_names[max_len_name])

for item in persons:
    ages.append(item['age'])
res_mean = statistics.mean(ages)
print('average age:', res_mean)

# 2 ########################################
# а ########################################

my_dict_1 = {1:1, 2:1, 3:2, 4:7, 5:9, 6:13}
my_dict_2 = {1:2, 2:1, 3:5, 4:7, 5:9, 6:12}

def func_1(my_dict_1, my_dict_2):
    new_dict = dict()
    for key, value in my_dict_1.items():
        if key in my_dict_2 and value == my_dict_2[key]:
            new_dict[key] = value

    return new_dict
d = list(func_1(my_dict_1, my_dict_2))
print('2-а)',d)

# б ##########################################

def func_2(my_dict_1, my_dict_2):
    new_dict = dict()
    for key, value in my_dict_1.items():
        if key in my_dict_2 and value != my_dict_2[key]:
            new_dict[key] = value

    return new_dict
d = list(func_2(my_dict_1, my_dict_2))
print('2-б)', d)

# в ###########################################

d = func_2(my_dict_1, my_dict_2)
print('2-в)', d)

# г ###########################################

res = dict()

for item in my_dict_1.items():
    if item[0] not in my_dict_2:
        res[item[0]] = item[1]
    else:
        res[item[0]] = [item[1], my_dict_2[item[0]]]
for item in my_dict_2.items():
    if item[0] not in my_dict_1:
        res[item[0]] = item[1]
    else:
        res[item[0]] = [item[1], my_dict_1[item[0]]]
print('2-г)', res)
# 3 #############################################
my_list = ["qwe", "asd", "zxc", "qaz", "xsw", "edc"]

def new_list(my_list):
    result = []
    for index in range(len(my_list)):
        if not index % 2:
            result.append(my_list[index][::-1])
        else:
            result.append(my_list[index])
    return result

print('3)', new_list(my_list))

# 4 ##############################################
import random
import string

names = ["John", "Pieter", "Sam", "Jim"]
domains = ["com", "org", "net", "ua"]

def new_email(names):
    return str(random.choice(names)) + '.' + str(random.randint(100, 999)) + '@' + str(''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(5, 7)))) + '.' + str(random.choice(domains))
email = str(new_email(names))
print('4)', email)


