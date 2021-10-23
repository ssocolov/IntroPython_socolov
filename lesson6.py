# параметры функций
# модуль os
# работа с файлами
# практическая работа
########################## практическая работа #########################################################
# import os
# from string import ascii_lowercase as alphabet
# from random import shuffle
#
# def create_folder(folder_name="alphabet"):
#     os.makedirs(folder_name, exist_ok=True)
#
# def create_file(symbol, folder_name):
#     filename = f"{symbol}.txt"
#     with open(f"{folder_name}/{filename}", "w") as txt_file:   # менеджер контекста "with"
#         txt_file.write(alphabet.replace(symbol, symbol.upper()))
#
# def create_alphabet_files(folder_name):
#     for symbol in alphabet:
#         create_file(symbol, folder_name)
#
# def do_tanos_click(dir_name):
#     files = os.listdir(dir_name)
#     shuffle(files)
#     for filename in files[:len(files) // 2]:
#         os.remove(os.path.join(dir_name, filename))
#
#
# dir_name = "alphabet"
# # create_folder(dir_name)
# # create_alphabet_files(dir_name)
# do_tanos_click(dir_name)


##################### работа с файлами #######################################################################

# with open("test/1.txt", "w") as txt_file:   # рекомендовано!!!
#     # data = file.read()      # считал всё одной строкой
#     txt_file.writelines(data)
# print(data)

# file = open("test/1.txt", "r")        # можно использовать в редких случаях
# data = file.read()
# file.close()          # если забыть написать file.close, то файл будет висеть открытым
#
# print(data)

################## модуль os ########################################################################
# import os
#
# dir = os.listdir("test")
# print(dir)
#
# filename = 'lesson3.py'
# folder = ()
# path = f"{folder}/{filename}"
# path = os.path.join(os.getcwd(), folder, filename)
# print(path)
# os.mkdir("test/test2")  ## не рекомендую ))
# os.makedirs("test3", exist_ok=True)   # рекомендую!!!!!
#
# for filename in sorted(dir):
#     file_path = os.path.join("test", filename)
#     if os.path.isfile(file_path):
#         print(f"{filename=}")

###################################################################################################
# def test_func(par_1: str, par_2: str, par_3: str, par_4: str = "asdfgh") -> int:
#     return len(f"{len(par_1)}_{len(par_2)}_{len(par_3)}_{len(par_4)}")

# def test_func_2(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#
# print(test_func_2("John", 24, job="programmer", animal="dog"))

#################################################################################################
# from random import randint
#
# MIN_LIMIT = 1
# MAX_LIMIT = 10


# triangle_abc = {"A":(2, 3),
#             "B": (-4, 7),
#             "C": (0, 0)}
#
# def create_point(min_limit=MIN_LIMIT, max_limit=MAX_LIMIT):
#     return (randint(min_limit, max_limit), randint(min_limit, max_limit))


# def create_triangle(min_limit, max_limit):
#     triangle_dict = {"A": create_point(min_limit, max_limit),   # DRY
#                     "B": create_point(min_limit, max_limit),
#                     "C": create_point(min_limit, max_limit)}
#     return triangle_dict

# def create_triangle(name="ABC"):
#
#     triangle_dict = {name[0]: create_point(),   # DRY
#                     name[1]: create_point(),
#                     name[2]: create_point()}
#     return triangle_dict
#
#
# def create_triangles_list(nuber=3):
#     return [create_triangle("QWE") for _ in range(number)]


# triangle_abc = create_triangle()
# print(triangle_abc)


# triangle_abc = create_triangles_list()
# print(triangle_abc)