# Посчитать факториал (произведение 1 до N) и треугольное число (сумма чисел от 1 до N) для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов

def fact(a):
    if a == 1:
        return 1
    return a * fact(a-1)

def factT(a):
    if a == 1:
        return 1
    return fact(a - 1) + a
    

a = int(input())
print(f"факториал {fact(a)}")
print(f"треугольное число {factT(a)}")