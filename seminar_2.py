# 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр
"""
def  Sumnumber(Number):
    sum = 0
    while(Number > 0):
        count = Number % 10
        sum = sum + count
        Number = Number//10
    return sum

userNumber = int(input("Enter number: "))
print(Sumnumber(userNumber))
"""

# 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
"""
def productsOfNumbers (Number):
    cout = 1
    for i in range(Number):
        i = i + 1
        cout = i * cout
        print (cout, end=" ")

userNumber = int(input("Enter number: "))
productsOfNumbers(userNumber)
"""

# 3 Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму
"""
def listConsequence(n):
    summ = [((1 + 1/i)**i) for i in range(1, n + 1)]
    return sum(summ)

userNumber = int(input("Enter number: "))
print(listConsequence(userNumber))
"""

# 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел

numbers = [-3, -2, -1, 0, 1, 2, 3]

def countNumbers (numbers, newIndexes):



userIndexes = input('Enter a list of numbers separated by a space: ').split()
newIndexes = list(map(int, userIndexes))
countNumbers(numbers,newIndexes)


# 5 Реализуйте алгоритм перемешивания списка.
"""
import random
lst = [random.randint(0,10) for i in range(random.randint(5,20))]
print(f"source list:\n {lst}")
random.shuffle(lst)
print(f"list after mixing:\n{lst}")
"""