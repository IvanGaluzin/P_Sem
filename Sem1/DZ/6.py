# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

a = int(input("Введите число: "))
a1 = int(a/100000)
a2 = int(a/10000%10)
a3 = int(a/1000%10)
a4 = int(a/100%10)
a5 = int(a/10%10)
a6 = int(a%10)
aSum1 = int(a1+a2+a3)
aSum2 = int(a4+a5+a6)
print(f"{a1} + {a2} + {a3} = {a4} + {a5} + {a6}")
print(f"{aSum1} = {aSum2}")
if (a > 99999 and a < 1000000):
    if(aSum1 == aSum2):
        print(f"Да")
    else:
        print("Нет")
else:
    print("Введите шестизначное число!")