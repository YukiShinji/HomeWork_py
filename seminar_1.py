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
userNumber = int(input ())
dayOfTheWeek (userNumber)
"""
# 2 Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
"""
for x in range(2):
        for y in range(2):
            for z in range(2):
                print(x, y, z, (not (x or y or z) == (not x and not y and not z)))
"""