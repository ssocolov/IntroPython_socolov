#ООП
##############################
# класс (названия классов пишутся с большой буквы)
# экземпляр класса
# атрибут класса
# атрибут экземпляра класса
# метод экземпляра класса
# -------------------------
# наследование
from lesson9_class import DataUser



# начало ООП

# data_user_1 = DataUser()   # экземпляр класса(конкретный представитель)
# data_user_2 = DataUser()
# data_user_3 = DataUser()
#
# DataUser.ip = "127.0.0.1"
# data_user_1.ip = "127.0.0.2"    # запись данных # атрибут экземпляра класса
# data_user_2.ip = "255.255.255.0"  # запись данных # атрибут экземпляра класса
# data_user_1.error_count = 3       # запись новых данных(атрибут экземпляра класса)
#
# print(data_user_1.ip)
# print(data_user_2.ip)
# print(data_user_1, data_user_2, data_user_3)
# print(data_user_1.error_count)
# print(DataUser.ip)
# print(data_user_2.error_count)    # AttributeError: 'DataUser' object has no attribute 'error_count'

################## атрибут класса ################

data_user_1 = DataUser("John", "127.0.0.2", 10.0)
data_user_2 = DataUser("Jack", "255.255.255.0", 0.0)
print(data_user_1.ip)
# print(data_user_2)
# value = str(data_user_1)
# print(value)
print(data_user_1)
# users = [data_user_1, data_user_2]
# print(users)
add_time = 2.0
# data_user_1.increase_user_time(2.0)

## плохая практика
# user_time = data_user_1.user_time
# user_time += add_time
# data_user_1.user_time = user_time

print(data_user_1)

