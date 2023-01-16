import numpy as np
from matplotlib import pyplot as plt
data = np.loadtxt("Files_Chapter_10/Temperatures.txt", delimiter=",", dtype=int)
days = np.array(data[:,0], str)
temperature = data[:,1]
plt.plot(days,temperature, label="temperature")
plt.xlabel("days")
plt.title("Temp/days")
plt.xticks(rotation=90)
plt.ylabel("Temperature")
plt.legend()
plt.show()
