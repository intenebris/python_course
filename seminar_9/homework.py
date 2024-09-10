# Задача 1:  Работать с файлом california_housing_train.csv, который находится в папке sample_data. 
# Определить среднюю стоимость дома(median_house_value), где кол-во людей от 0 до 500 (population)

import pandas as pd
df = pd.read_csv('seminar_9/california_housing_train.csv')

median_value = df.loc[df['population'] < 500, ['median_house_value']].median()
print(f"Средняя медианная стоимость дома \n{median_value}\n")

# Задача 2: Узнать какая максимальная households в зоне минимального значения population

min_zone = df['population'].min() * 1.1

max_housholds = df.loc[df['population'] < min_zone, ['households']].max()

print(f"Максимальное количество домохозяйств \n{max_housholds}\n")
