# Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.


N=int(input())
list1=[i for i in range(20, N) if i%20==0 or i%21==0]
print(list1)
print(int(input()))
