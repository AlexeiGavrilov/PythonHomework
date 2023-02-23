# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Введите число: '))
result = 1
for i in range(n):
    if (result < n):
        print(result)
        result = result * 2
        
        
