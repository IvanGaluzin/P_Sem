# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

from random import randint

n1_set = list(randint(1, 5) for i in range(int(input('Введите кол-во элементов первого множества: '))))
print(n1_set)
def change (list):
    min_num = min(list)
    max_num = max(list)
    for i in range(len(list)):
        if list[i] == max_num:
            list[i] = min_num
    return list

print(change(n1_set))