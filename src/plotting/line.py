import seaborn as sns
import matplotlib.pyplot as plt
import math
sns.set_style("whitegrid")

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, marker='o', linestyle='-', color='g')
plt.title("Line Plot Example")
plt.xlabel("X-axis")   
plt.ylabel("Y-axis")
plt.show()

# Sin(x) plot
x = []
y = []
for i in range(0, 628):  # 0 to 2π in steps of 0.01 -> 3.14*2 = 6.28
    x.append(i / 100)
    y.append(math.sin(i / 100))

plt.plot(x, y, marker='', linestyle='-', color='b')
plt.title("Sine Wave Plot")
plt.xlabel("X-axis (radians)")
plt.ylabel("sin(x)")
plt.show()