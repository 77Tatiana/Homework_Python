# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума). Список можно задавать рандомно
# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

# если вводить заданные числа 
list_1 = [1, 5, 88, 100, 2, -4]
min = 33
max = 200
list_2 = []
for i in range(len(list_1)):
    if list_1[i] >= min and list_1[i] <= max:
      list_2.append(i)
print(list_2)

# или второй вариант 
list_1 = [1, 5, 88, 100, 2, -4]
min = 33
max = 200
print ([i for i in range(len(list_1)) if list_1[i] >= min and list_1[i] <= max])

# если вводить рандомные спиок и мин и макс значения
from random import randint
list_1 = [randint(1, 100) for _ in range (int(input('Введите кол-во элементов массива: ')))]
print(list_1)
min = int(input('Задайте минимальную границу диапазона: '))
max = int(input('Задайте максимальную границу диапазона: '))
print ([i for i in range(len(list_1)) if list_1[i] >= min and list_1[i] <= max])





