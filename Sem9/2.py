# Задача 42: Узнать какая максимальная households в зоне минимального значения population.

# Ссылка на код с занятия: https://colab.research.google.com/drive/119PmgTc8uf_-Minwticwe23KTzLkyaeg?usp=sharing

import pandas as pd

df = pd.read_csv('/content/sample_data/california_housing_train.csv')

min_population = df['population'].min()
zone = df[df['population'] == min_population]

max_households = zone['households'].max()

print('Макс значение households в зоне с Мин population:', max_households)