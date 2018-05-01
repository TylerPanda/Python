import pandas as pd
import numpy as np

area_dict = {"California": 423967,
             "Texas": 695662,
             "New York": 141297,
             "Florida": 170312,
             "Illinois": 149995}
area = pd.Series(area_dict)
print("area =\n", area)
population_dict = {"California" : 38332521,
                   "Texas" : 26448193,
                   "New York" : 19651127,
                   "Florida" : 19552860,
                   "Illinois" : 12882135}
population = pd.Series(population_dict)
print("population = ")
print(population)
states = pd.DataFrame({"population": population,
                       "area": area})
print("states =\n", states)
print("states.index = \n", states.index)
print("states.columns = \n", states.columns)
print("states['area'] = \n", states["area"])
print("states['population'] = \n", states["population"])

print("pandas.DataFrame(population, columns = ['population']) = \n", pd.DataFrame(population, columns = ['population']))

data = [{"a": i, "b": 2 * i} for i in range(3)]
print("data = \n", data)
print("pandas.DataFrame(data) =  ")
print( pd.DataFrame(data))

data = [{"a": 1, "b": 2}, {"b": 2, "c": 4}]
print("data =")
print(data)
print("pandas.DataFrame(data) = ")
print(pd.DataFrame(data))

print("pandas.DataFrame({'population': population,'area': area}) = ")
print(pd.DataFrame({"population": population, "area": area}))

data = pd.DataFrame(np.random.rand(3, 2),
                    columns = ["foo", "bar"],
                    index = ["a", "b", "c"])
print("pandas.DataFrame(numpy.random.rand(3, 2), columns = ['foo', 'bar'], index = ['a', 'b', 'c']) = ")
print(data)

A = np.zeros(3, dtype = [("A", "i8"), ("B", "<f8")])
print("numpy.zeros =")
print(A)
print("panda.DataFrame(A) = ")
print(pd.DataFrame(A))

ind = pd.Index([2, 3, 5, 7, 11])
print("ind")
print(ind)
print(ind.size,  ind.shape, ind.ndim, ind.dtype)

indA = pd.Index([1, 3, 5, 7, 9])
indB = pd.Index([2, 3, 5, 7, 11])
print("indA = ")
print(indA)
print("indB = ")
print(indB)
print("indA & indB = ")
print(indA & indB)
print("indA | indB = ")
print(indA | indB)
print("indA ^ indB = ")
print(indA ^ indB)

area = pd.Series({"California": 423967, "Texas": 695662, "New York": 141297, "Florida": 170312, "Illinois": 149995})
pop = pd.Series({"California": 38332521, "Texas": 26448193, "New York": 19651127, "Florida": 19552860, "Illinois": 12882135})
data = pd.DataFrame({"area": area, "pop": pop})
print("data = ")
print(data)
print("data['area'] = ")
print(data['area'])
print("data['pop'] = ")
print(data['pop'])

data['density'] = data['pop'] / data['area']
print("data = ")
print(data)
print("data.values = ")
print(data.values)
print("data.T = ")
print(data.T)

print("data.loc[data.density > 100, ['pop', 'density']] = ")
print(data.loc[data.density > 100, ['pop', 'density']])
