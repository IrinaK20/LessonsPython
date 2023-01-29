# Написать функцию, аргументы имена сотрудников, возвращает словарь, 
# ключи — первые буквы имён, значения — списки, 
# содержащие имена, начинающиеся с соответствующей буквы.

def thesaurus(*args):
    dictionary = {}
    for i in sorted(args):
        letter = i[0]
        if letter not in dictionary:
            dictionary[letter] = [i]
        else:
            dictionary[letter] += [i]

    return dictionary

print(thesaurus("Иван", "Мария", "Петр", "Илья", "Марина", "Алина", "Бибочка"))



