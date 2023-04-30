# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

dict1 = dict()

symbols = input("Введите буквы: ")

for syn in symbols:
    if syn in dict1:
        dict1[syn] +=1
    else:
        dict1[syn] = 0

    if dict1[syn] == 0:
        print(syn)
    else:
        print(f"{syn}_{dict1[syn]}")