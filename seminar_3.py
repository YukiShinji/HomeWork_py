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

# 3 Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов
'''
lst = list(map(float, input("Enter numbers separated by a space:\n").split()))
new_lst = [round(i%1,2) for i in lst if i%1 != 0]
print(max(new_lst) - min(new_lst))
'''

# 4 Напишите программу, которая будет преобразовывать десятичное число в двоичное
'''
s = ""
n = int(input("Enter number:\n"))
while n != 0:
    s = str(n%2) + s
    n //=2
print(s)
'''

# 5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов
'''
def Fibonacci(n):
    if n in [1, 2]:                       
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

def NegaFibonacci(n):
    if n == 1:                       
        return 1
    elif n == 2:                       
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2

list = [0]
userNumber = int(input('Enter any number: '))
for e in range(1, userNumber + 1):
    list.append(Fibonacci(e))
    list.insert(0, NegaFibonacci(e))
print(list)
'''