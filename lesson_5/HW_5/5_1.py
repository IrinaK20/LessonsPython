# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# #  В тексте используется разделитель пробел.

from random import sample

def list_rand_words(count: int, alp: str = 'абв'):
    words_list = []
    for i in range(count):
        letters = sample(alp, k=3)
        words_list.append("".join(letters))
    return " ".join(words_list)

def delete(rand_list: str):
    return " ".join(rand_list.replace("абв", "").split())

all_list = list_rand_words(int(input("введите кол-во слов: ")))
print(all_list)
print(delete(all_list))
