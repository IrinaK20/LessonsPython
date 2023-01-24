# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.



from itertools import groupby, starmap
from os import path


def rle_compression( text="text.txt", comp_text="RLE.txt"):
    if path.exists(text):
        with open(text) as my_f, \
                open(comp_text, "a", encoding="utf-8") as my_f_2:
            for i in my_f:
                my_f_2.write("".join([f"{len(list(v))}{ch}" for ch, v in groupby(i)]))
    else:
        print("данного файла нет")

def recovery (name):
    if path.exists(name):
        with open(name) as my_f:
            n = ""
            for k in my_f:
                word_nums = []
                for i in k.strip():
                    if i.isdigit():
                        n += i
                    else:
                        word_nums.append([int(n), i])
                        n = ""
                print("".join(starmap(lambda x, y: x * y, word_nums)))
    else:
        print("данного файла нет")


rle_compression (input("введите имя файла: "))
recovery (input("введите имя файла для восстановления: "))

    

