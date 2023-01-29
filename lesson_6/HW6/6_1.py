# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension.

from random import sample
def gg(n):
    list= sample(range(n * 2), n)
    print(list)
    return[list[n] for n in range(1, len(list)) if list[n] >list[n-1]]
 
print(gg(int(input())))


# a= range(0, 21)
# m = [j for i, j in zip(a, a[1:]) if j > i]

# print (m)

