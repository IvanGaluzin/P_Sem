# Задача №3.
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

n = int(input("Количество учеников в первом класе: "))
m = int(input("Количество учеников в втором класе: "))
b = int(input("Количество учеников в третьем класе: "))
print(f"Понадобится {int(((m+n+b+1)/2))} парты")