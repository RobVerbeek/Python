import numpy as np
data = np.loadtxt("Files_Chapter_10/student_grades_3.csv", skiprows=1, delimiter=";", dtype=int)
maxn = np.max(data, axis=0)
minn = np.min(data, axis=0)
mean = np.mean(data, axis=0)
print(f"Python max:{maxn[0]} min: {minn[0]} average: {mean[0]}")
print(f"Linux max:{maxn[1]} min: {minn[1]} average: {mean[1]}")
print(f"Python max:{maxn[2]} min: {minn[2]} average: {mean[2]}")




