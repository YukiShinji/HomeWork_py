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