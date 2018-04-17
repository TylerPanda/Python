import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
import numpy as np
import seaborn

rand = np.random.RandomState(42)

x = rand.randint(100, size = 10)
print("x = ", x)
print("x[3] = ", x[3])
print("x[7] = ", x[7])
print("x[2] = ", x[2])
ind = [3, 7, 2]
print("ind = ", ind)
print("x[ind] = ", x[ind])
ind = np.array([[3, 7],
                [4, 5]])
print("ind = ", ind)
print("x[ind] = ", x[ind])

x = np.arange(12).reshape((3, 4))
print("x = ", x)
row = np.array([0, 1, 2])
col = np.array([2, 1, 3])
print("row = ", row)
print("col = ", col)
print("x[row, col] = ", x[row, col])
print("x[row[:, np.newsaxis], col] = ", x[row[:, np.newaxis], col])

mean = [0, 0]
cov = [[1, 2],
       [2, 5]]
x = rand.multivariate_normal(mean, cov, 100)
print("x       = ", x)
print("x.shape = ", x.shape)
seaborn.set()
plt.scatter(x[:,0], x[:,1])
plt.savefig("Images/normal_scatter.png")

indices = np.random.choice(x.shape[0], 20, replace = False)
print("indices = ", indices)
selection = x[indices]
print("selection.shape = ", selection.shape)
plt.scatter(x[:, 0], x[:, 1], alpha = 1)
plt.scatter(selection[:, 0], selection[:, 1], facecolor = "none", s = 200 )
plt.savefig("Images/normal_scatter_20.png")

np.random.seed(42)
x = np.random.randn(100)

bins = np.linspace(-5, 5, 20)
counts = np.zeros_like(bins)
i = np.searchsorted(bins, x)
np.add.at(counts, i, 1)
seaborn.set()
plt.plot(bins, counts, linestyle = "steps")
print("bins   = ", bins)
print("counts = ", counts)
print("i      = ", i)
print("numpy.add.at(counts, i, 1) = ", np.add.at(counts, i, i))
plt.savefig("Images/BinningData.png")
