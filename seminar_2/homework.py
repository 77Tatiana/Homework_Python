# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, 
# которые нужно перевернуть.

# я от себя добавила, как разлечить монетки. по-другому не смогла найти решение 

n = int(input('Введите число монеток на столе '))
k = 0
for i in range(n):
    v = int(input('Введите как лежат монетки, где 1 если монетка лежит решкой вверх и 0 если вверх гербом '))
    if v == 1:
        k += 1
if k < n/2:
    print(f'Нужно перевернуть {k} монеток')
else:
    print(f'Нужно перевернуть {n-k} монеток')


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

S = int(input('Введите сумму чисел: '))
P = int(input('Введите произведение чисел: '))
import math
X = (S - math.sqrt(S**2-4*P))/2
Y = S - X
if X<=1000 and Y<=1000:
    print(f'Задуманные Петей числа: {int(X)} и {int(Y)}')

    
# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
    
N = int(input('Введите число N: '))
m = 1
while m <= N:
    print (m, end=' ')
    m = m * 2