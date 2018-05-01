import numpy as np
import pandas as pd

index = [("California", 2000), ("California", 2010),
         ("New York", 2000), ("New York", 2010),
         ("Texas", 2000), ("Texas", 2010)]
population = [33871648, 37253956,
              18976457, 19378102,
              20851820, 25145561]

pop = pd.Series(population, index = index)
print("pop = ")
print(pop)
print("pop[('California, 2000'): ('Texas', 2010)] = ")
print(pop[("California", 2000): ("Texas", 2010)])
print("pop[[i for i in pop.index if i[1] == 2010]] = ")
print(pop[[i for i in pop.index if i[1] == 2010]])

index = pd.MultiIndex.from_tuples(index)
print("panda.MultiIndex.from_tuples(index) = ")
print(index)
print("pop.reindex(index) = ")
print(pop.reindex(index))
print("pop.reindex(index)[:,2010] = ")
print(pop.reindex(index)[:, 2000])
pop_df = pop.reindex(index).unstack()
print("pop.reindex(index).unstack() = ")
print(pop_df)
print("pop_df.stack() = ")
print(pop_df.stack())
pop = pop.reindex(index)
print("pop = ")
print(pop)
print("pandas.DataFrame({'total': pop,'under18': [9267089, 9284094, 4687374, 4318033, 5906301, 6879014]}) = ")
print(pd.DataFrame({'total': pop,'under18': [9267089, 9284094, 4687374, 4318033, 5906301, 6879014]}))
pop_df = pd.DataFrame({'total': pop,'under18': [9267089, 9284094, 4687374, 4318033, 5906301, 6879014]})
f_u18 = pop_df["under18"] / pop_df["total"]
print("pop_df['under18'] / pop_df['total'] = ")
print(f_u18)
print("(pop_df['under18'] / pop_df['total']).unstack() = ")
print(f_u18.unstack())


data = {("California", 2000): 33871648,
        ("California", 2010): 37253956,
        ("Texas", 2000): 20851820,
        ("Texas", 2010): 25145561,
        ("New York", 2000): 18976457,
        ("New York", 2010): 19378102}
print("pandas.Series(data) = ")
print(pd.Series(data))


print("pandas.MultiIndex.from_arrays([['a', 'a', 'b', b], [1, 2, 1, 2]]) = ")
print(pd.MultiIndex.from_arrays([["a", "a", "b", "b"], [1, 2, 1, 2]]))
print("pandas.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1), ('b', 2)])")
print(pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1), ('b',2)]))

pop.index.names = ['State', 'Year']
pop_flat = pop.reset_index(name = 'Population')
print("pop = ")
print(pop)
print("pop_flat = ")
print(pop_flat)
print(pop_flat.set_index(['State', 'Year']))


# index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]], names = ['year', 'visit'])
# columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], ['HR', 'Temp']], names = ['subject', 'type'])
#
# data = np.round(np.random.rand(4, 6), 1)
# data[:, ::2] *= 10
# data += 37
# health_data = pd.DataFrame(data, index = index, columns = columns)
# print("health_data = ")
# print(health_data)
#
# print(pop)
