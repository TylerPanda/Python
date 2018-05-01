import pandas as pd
import numpy as np


data = pd.Series([0.25, 0.5, 0.75, 1])
print("data        = ", data)
print("data.values = ", data.values)
print("data.index  = ", data.index)
print("data[1]     = ", data[1])
print("data[1:3]   = ", data[1:3])

data = pd.Series([0.25, 0.5, 0.75, 1.0],
                  index = ["a", "b", "c", "d"])
print("data = ", data)

data = pd.Series([0.25, 0.5, 0.75, 1.0],
                  index = [2, 5, 3, 7])
print("data = ", data)

population_dict = {"California" : 38332521,
                   "Texas" : 26448193,
                   "New York" : 19651127,
                   "Florida" : 19552860,
                   "Illinois" : 12882135}
population = pd.Series(population_dict)
print(population)
print('population["California"] = ', population["California"])
print('population["California" : "Illinois"] = ', population["California" : "Illonois"])

data = pd.Series([0.25, 0.5, 0.75, 1.0], index = ["a", "b", "c", "d"])
print("data = ")
print(data)
print("data['b'] = ", data['b'])
print("'a' in data = ", 'a' in data)
print("data.keys() = ", data.keys())
print("list(data.items()) = ", list(data.items()))
data['e'] = 1.25
print("data = ", data)
print("data['a':'c'] = ")
print(data['a':'c'])
print("data[0:2] = ")
print(data[0:2])
print("data[(data > 0.3) & (data < 0.8)] = ")
print(data[(data > 0.3) & (data < 0.8)])
print("data[['a', 'e']] = ")
print(data[['a', 'e']])

data = pd.Series(['a', 'b', 'c'], index = [1, 3, 5])
print("data = ")
print(data)
print("data[1] = ")
print(data[1])
print("data[1:3] = ")
print(data[1:3])
print("data.loc[1] = ")
print(data.loc[1])
print("data.loc[1:3] = ")
print(data.loc[1:3])
print("data.iloc[1] = ")
print(data.iloc[1])
print("data.iloc[1:3] = ")
print(data.iloc[1:3])
