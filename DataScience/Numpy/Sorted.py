import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
import numpy as np
import seaborn

x = np.array([2, 1, 4, 3, 5])
print("x             = ", x)
print("numpy.sort(x) = ", np.sort(x))     #不更動原有的輸入內容
print("x.sort()      = ", x.sort())       #在陣列中直接排序

x = np.array([2, 1, 4, 3 ,5])
i = np.argsort(x)
print("x                = ", x)
print("numpy.argsort(x) = ", np.argsort(x))
print("x[i]             = ", x[i])

rand = np.random.RandomState(42)
x = rand.randint(0, 10, (4, 6))
print("rand.randint(0, 10, (4, 6)) = ", "\n", x)
print("numpy.sort(x, axis = 0)     = ", "\n", np.sort(x, axis = 0))
print("numpy.sort(x, axis = 1)     = ", "\n", np.sort(x, axis = 1))

x = np.array([7, 2, 3, 1, 6, 5, 4])
print("numpy.partition(x, 3) = ", np.partition(x, 3))

x = rand.rand(10, 2)
seaborn.set()
print("x       = ", x)
print("x[:, 0] = ", x[:, 0])
print("x[:, 1] = ", x[:, 1])
# plt.scatter(x[:, 0], x[:, 1], s = 100)
# plt.savefig("Images/knn.png")

print("x[:, np.newaxis, :] = ", x[:, np.newaxis, :])
print("(x[:, np.newaxis, :]).shape = ", (x[:, np.newaxis, :]).shape)
print("x[np.newaxis,:, :] = ", x[np.newaxis,:, :])
print("(x[np.newaxis,:, :]).shape = ", (x[np.newaxis,:, :]).shape)
dist_sq = np.sum((x[:, np.newaxis, :]- x[np.newaxis,:,:]) ** 2, axis = -1)
print(dist_sq)

differences = x[:, np.newaxis, :] - x[np.newaxis,:,:]
# print("differences = ", differences)
print("differences.shape = ", differences.shape)
sq_differences = differences ** 2
print("sq_differences = ", sq_differences)
# print("sq_differences.shape = ", sq_differences.shape)
dist_sq = sq_differences.sum(-1)
print("dist_sq = ", dist_sq)
print("dist_sq.shape = ", dist_sq.shape)
print("dist_sq.diagonal = ", dist_sq.diagonal())
nearest = np.argsort(dist_sq, axis = 1)
print("nearest = ", nearest)
k = 2
nearest_partition = np.argpartition(dist_sq, k+1, axis = 1)
plt.scatter(x[:,0], x[:,1], s = 100)
for i in range(x.shape[0]):
    for j in nearest[i, :k+1]:
        plt.plot(*zip(x[j], x[i]), color = "black")
plt.savefig("Images/knn2.png")
