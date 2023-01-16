import numpy as np
python = np.genfromtxt("Files_Chapter_10/points_python.txt", delimiter=";", dtype=int, filling_values="0")
networks = np.genfromtxt("Files_Chapter_10/points_networks.csv", delimiter=";", dtype=int, filling_values="0")
web = np.genfromtxt("Files_Chapter_10/points_web.txt", delimiter=";", dtype=int,filling_values="0")
linux = np.genfromtxt("Files_Chapter_10/points_linux.csv", delimiter=";", dtype=int, filling_values="0")
data = (python + networks + web + linux)/4
print(data)
print("*"*25)
data[:,1]*=5
print(data)