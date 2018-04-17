import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn

data = pd.read_csv("../data/president_heights.csv")
heights = np.array(data["height(cm)"])

print(heights)
print("Mean height:        ", heights.mean())
print("Standard deviation: ", heights.std())
print("Minimum heights:    ", heights.min())
print("Maximum heights:    ", heights.max())
print("25th percentile:    ", np.percentile(heights, 25))
print("Median:             ", np.median(heights))
print("75th percentile:    ", np.percentile(heights, 75))

seaborn.set()
plt.hist(heights)
plt.title("Height Distribution od US Presidents")
plt.xlabel("height (cm)")
plt.ylabel("number")
plt.savefig("Images/President_hieght.png")
