# 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах
'''
def sumOddIndex(lst):
    sum = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            sum += lst[i]
    print(f"Summ is: {sum}")

lstmas = [2, 3, 5, 9, 3]
sumOddIndex(lstmas)
lstmas = list(map(int, input("Enter numbers separated by a space:\n").split()))
sumOddIndex(lstmas)
'''

# 2 Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д
'''
from random import randint

number = int(input('Enter the size of the list '))
list = []
list2 = []

for i in range(number):
    list.append(randint(0, 9))

for i in range(len(list)):
    while i < len(list)/2 and number > len(list)/2:
        number = number - 1
        a = list[i] * list[number]
        list2.append(a)
        i += 1

print(list)
print(list2)
'''