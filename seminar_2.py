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