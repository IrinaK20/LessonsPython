# 1. Напишите программу, которая принимает на вход вещественное число
#    и показывает сумму его цифр. Без работы с методами строк.

num = float (input("введите дробное число:"))
sum=0

power = len(str(num)) - 2    # скоько знаков после запятой
num=num*10**power            # перенос зяпятой в конец

while num:
    sum += num % 10
    num //= 10

print(int(sum))