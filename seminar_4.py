# 1 Вычислить число c заданной точностью d
'''
from math import pi

d =  int(input("Enter a number for the specified precision of the number pi:\n"))
print(f'The number of Pi with a given accuracy {d} equally {round(pi, d)}')
'''

# 2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
'''
n = int(input('Enter the number N: '))
list = []
a = n
if n > 1:
    restart = True
    while restart:
        restart = False
        for i in range (2, n+1):
            if n % i == 0:
                list.append(i)
                n = int(n/i)
                restart = True
                break

    print(f'Prime factors of a number {a} - {list}')
elif n == 1:
    print(f'Prime factors of a number {a} - [1]')
else:
    print(f'You entered the wrong number')
'''

# 3 Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности
'''
lstMassive = list(map(int, input("Enter numbers separated by a space:\n").split()))
print(f"Start massive: {lstMassive}")
newMassive = [i for i in lstMassive if lstMassive.count(i)==1]
print(f"A list of non-repeating elements: {newMassive}")
'''

# 4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k
'''
import random


def writeFile(st):
    with open('file33.txt', 'w') as data:
        data.write(st)


def rnd():
    return random.randint(0,101)


def createMn(k):
    lst = [rnd() for i in range(k+1)]
    return lst
    

def createStr(sp):
    lst= sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr

k = int(input("Enter the natural degree k = "))
koef = createMn(k)
writeFile(createStr(koef))
'''

# 5 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов (складываются числа, у которых "х" в одинаковых степенях)