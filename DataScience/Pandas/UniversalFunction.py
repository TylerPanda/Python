import numpy as np
import pandas as pd

rng = np.random.RandomState(42)
ser = pd.Series(rng.randint(0, 10, 4))

print("ser = ")
print(ser)

df = pd.DataFrame(rng.randint(0, 10, (3, 4)), columns = ["A", "B", "C", "D"])
print("df = ")
print(df)

print("numpy.exp(ser) = ")
print(np.exp(ser))

print("sumpy.sin(df * numpy.pi/4) = ")
print(np.sin(df * np.pi/4))

area = pd.Series({"Alaska": 1723337, "Texas": 695662, "California": 423967}, name = "area")
population = pd.Series({"California": 38332521, "Texas": 26448193, "New York": 19651127}, name = "population")
density = population / area
print("population = ")
print(population)
print("area = ")
print(area)
print("population / area = ")
print(density)
print("area.index | population.index = ")
print(area.index | population.index)
print("area.index & population.index = ")
print(area.index & population.index)

A = pd.Series([2, 4, 6], index = [0, 1, 2])
B = pd.Series([1, 3, 5], index = [1, 2, 3])
print(A + B)

print(A.add(B, fill_value = 0))

A = pd.DataFrame(rng.randint(0, 20, (2, 2)), columns = list("AB"))
B = pd.DataFrame(rng.randint(0, 10, (3, 3)), columns = list("ABC"))
print("A = ")
print(A)
print("B = ")
print(B)
print("A + B")
print(A + B)

fill = A.stack().mean()
print(A.add(B, fill_value = fill))

A = rng.randint(10, size = (3, 4))
print("A = ")
print(A)
print("A - A[0] = ")
print(A - A[0])

df = pd.DataFrame(A, columns = list("QRST"))
print("df = ")
print(df)
print("df.iloc[0] = ")
print(df.iloc[0])
print("df - df.iloc[0] = ")
print(df - df.iloc[0])
print("df.subtract(df['R'], axis = 0) = ")
print(df.subtract(df["R"], axis = 0))

halfrow = df.iloc[0, ::2]
print("halfrow = ")
print(halfrow)
print("df - halfrow = ")
print(df - halfrow)
