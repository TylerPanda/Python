import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn


rainfall = pd.read_csv("../data/Seattle2014.csv")["PRCP"].values
inches = rainfall / 254
# print(rainfall)
# print(inches)
print(inches.shape)

seaborn.set()
plt.hist(inches)
plt.savefig("Images/Rainfall.png")
