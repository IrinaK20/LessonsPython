# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

from random import sample

def rand_list (count: int):
    if count < 0:
        print("введите значение больше нуля")
        return[]

    list_nums = sample(range(1,count * 2), k=count)
    return(list_nums)    

def sum (list_nums):
    sum_nums=0
    for k in range(0,len(list_nums), 2):
        sum_nums+= list_nums[k]
    return sum_nums

list = rand_list (int(input("введите количество чисел в списке: ")))
print(list)
print (sum(list))
