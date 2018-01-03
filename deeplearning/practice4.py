import numpy as np
from function import *
import matplotlib
matplotlib.use('agg')
import matplotlib.pylab as plt

t = [0, 0, 1, 0, 0, 0, 0, 0 , 0, 0]
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
print(mean_squared_error(np.array(y), np.array(t)))

print(cross_entropy_error(np.array(y), np.array(t)))


def function_1(x):
    return 0.01 * x ** 2 + 0.1 * x

x = np.arange(0.0, 20.0, 0.1)
y = function_1(x)
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y)
plt.savefig("temp4.png")
