# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input("Введите число: "))
a = 2  # первое простое число
lst = []
while a <= num:
    if num % a == 0:
        lst.append(a)
        num //= a
    else:
        a += 1
print(lst)