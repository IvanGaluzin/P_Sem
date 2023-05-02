# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def degree (a, b, c):
    if b != 0:
        c *= a
        b -= 1
    else:
        return c
    return degree(a, b, c)

num1 = int(input("Введи число А: "))

num2 = int(input("Введи число Б: "))

c = 1

print(degree(num1, num2, c))