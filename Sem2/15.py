# Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

Arbuz = int(input("Количество арбузов: "))
VesMin =VesMax= int(input("Вес арбуза: "))
for i in range (1, Arbuz):
    temp = int(input("Вес арбуза: "))
    if temp > VesMax:
        VesMax=temp
    elif temp < VesMin:
        VesMin=temp
print(f"Для тещи {VesMin}, Для себя {VesMax}")