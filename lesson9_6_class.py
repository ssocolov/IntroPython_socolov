 import os
from string import ascii_lowercase as alphabet
from random import shuffle

class AlphabetWorker:
    def __init__(self, dir_name):
        self.dir_name = dir_name
        self.crate_folder()


    def create_folder(self):
        os.makedirs(self.dir_name, exist_ok=True)

    def create_file(self, symbol):
        filename = f"{symbol}.txt"
        with open(f"{self.dir_name}/{filename}", "w") as txt_file:   # менеджер контекста "with"
            txt_file.write(alphabet.replace(symbol, symbol.upper()))

    def create_alphabet_files(self):
        for symbol in alphabet:
            self.create_file(symbol, self.dir_name)

def do_tanos_click(dir_name):
    files = os.listdir(dir_name)
    shuffle(files)
    for filename in files[:len(files) // 2]:
        os.remove(os.path.join(dir_name, filename))


dir_name = "alphabet2"
alphabet_worker =




# create_folder(dir_name)
# create_alphabet_files(dir_name)
# do_tanos_click(dir_name)
