import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

def step_function(x):
    return np.array(x > 0, dtype = np.int)

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
print(plt.plot(x, y))
print(plt.ylim(-0.1, 1.1))
print(plt.show())
print(plt.savefig("temp.png"))
