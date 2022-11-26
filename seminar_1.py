# 1 Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным
"""
def dayOfTheWeek (userNum):
    if (userNum >= 1 and userNum <= 5):
        print ("This day not a weekend")
    elif (userNum >= 6 and userNum <= 7):
        print ("This day a weekend")
    else:
        print ("this day is not the day of the week ")

print ("Enter the day of the week")
userNumber = int(input())
dayOfTheWeek (userNumber)
"""

# 2 Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
"""
for x in range(2):
        for y in range(2):
            for z in range(2):
                print(x, y, z, (not (x or y or z) == (not x and not y and not z)))
"""

# 3 Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
"""
def checkCoordinates(first, second):
    if (first + second == 0):
        print('X = 0 and Y = 0, enter other coordinates')
    elif first > 0 and second > 0:
        print('1 quarter')
    elif first < 0 and second > 0:
        print('2 quarter')
    elif first < 0 and second < 0:
        print('3 quarter')
    elif first > 0 and second < 0:
        print('4 quarter')
    return (first,second)

print ("Enter the coordinate values")
firstCoordinate = float(input("Enter X: "))
secondCoordinate = float(input("Enter Y: "))

checkCoordinates(firstCoordinate, secondCoordinate)
"""

# 4 Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
"""
def dotCoordinates(quarter):
    if quarter == 1:
        print('x > 0, y > 0')
    elif quarter == 2:
        print('x < 0, y > 0')
    elif quarter == 3:
        print('x < 0, y < 0')
    elif quarter == 4:
        print('x > 0, y < 0')
    else:
        print('There are only 4 quarters on the coordinate plane')

userQuarter = int(input('Enter the quarter number: '))
dotCoordinates(userQuarter)
"""

# 5 Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве
"""
ax = float(input('Enter the coordinates of point A along the axis x:'))
ay = float(input('Enter the coordinates of point A along the axis y:'))
bx = float(input('Enter the coordinates of point B along the axis x:'))
by = float(input('Enter the coordinates of point B along the axis y:'))

import math
distans = math.sqrt((ax-bx)**2+(ay-by)**2)
print(f'Distance between point A to point B = {distans}' )
"""