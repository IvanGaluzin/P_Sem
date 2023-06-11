# Задание 44
# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

## Без get_dummies ##

import pandas as pd
import numpy as np

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})


unique_vals = np.unique(data.whoAmI)
one_hot_dict = {val: [int(x == val) for x in unique_vals] for val in unique_vals}
one_hot_df = pd.DataFrame(data.whoAmI.map(one_hot_dict).tolist(), columns=[f'whoAmI_{val}' for val in unique_vals])

data = pd.concat([data, one_hot_df], axis=1)
data.head()

# C get_dummies #

# import random
# import pandas as pd

# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})


# one_hot_data = pd.get_dummies(data)

# print(one_hot_data.head())