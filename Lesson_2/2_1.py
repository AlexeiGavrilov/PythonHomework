# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

n = int(input('Введите количество монеток на столе: '))
count1 = 0
count2 = 0
for i in range(n):
    temp = int(input('Эта монетка лежит решкой (1) или гербом (0)? '))
    if (temp > 1):
        print('Введены некоректные данные, попробуйте снова')
        break
    if temp == 1:
        count1 += 1
    else:
        count2 += 1
if (count1 >= count2):
    print(f'нужно перевернуть {count2} монеток')
else:
    print(f'нужно перевернуть {count1} монеток')

