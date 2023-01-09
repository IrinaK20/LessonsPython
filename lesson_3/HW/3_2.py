# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import sample

def rand_list (count: int):
    if count < 0:
        print("введите значение больше нуля")
        return[]

    list_nums = sample(range(1,count * 2), k=count)
    return(list_nums)    

def mult_list(list_nums):
   new_list=[]
   l = len(list_nums)
   for k in range(l//2):
       new_list.append(list_nums[k]*list_nums[l-k-1])
   if l % 2:
       new_list.append(list_nums[l // 2])
   return new_list    

list = rand_list (int(input("введите количество чисел в списке: ")))
print(list)
print(mult_list(list))
