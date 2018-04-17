import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

a = np.array([0, 1, 2])
b = np.array([5, 5, 5])
print(a + b)
print(a + 5)

M = np.ones((3, 3))
print(M)
print(M + a)

a = np.arange(3)
b = np.arange(3)[:, np.newaxis]
print(a)
print(b)
print(a + b)

X = np.random.random((10, 3))
Xmean = X.mean(0)
print(Xmean)

x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 50)[:, np.newaxis]
z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)
plt.imshow(z, origin = "lower", extent = [0, 5, 0, 5], cmap = "viridis")
plt.colorbar()
plt.savefig("Images/TwoDimensionVisualized.png")
