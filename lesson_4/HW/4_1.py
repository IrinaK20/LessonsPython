# Вычислить число c заданной точностью d

from decimal import Decimal
 
number = Decimal(input("введите чисо: "))
number = number.quantize(Decimal("0.01"))
print(number) 