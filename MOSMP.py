#----------------------5 лаба----------------------
import math
import numpy as np
import random
from prettytable import PrettyTable
import matplotlib.pyplot as plt

h = 0.1
k = 11 #klk liter prizvushcha x0
n = 12 #variant y0

#h = float(input("Введіть h: "))
#k = int(input("Введіть k: "))
#n = int(input("Введіть n: "))

def f(x, y):
    return x**3 - x - 20 + y #0-1 (-20.25)

iter = k * 2 - 1

xi = [0 for i in range(iter)]
yi1 = [0 for i in range(iter)]
yi2 = [0 for i in range(iter)]
yi3 = [0 for i in range(iter)]
yi4 = [0 for i in range(iter)]

yi_exact = [0 for i in range(iter)]

error_RyngeKyt_1 = [0 for i in range(iter)]
error_RyngeKyt_2 = [0 for i in range(iter)]
error_RyngeKyt_3 = [0 for i in range(iter)]
error_RyngeKyt_4 = [0 for i in range(iter)]

for j in range(iter):
    xi[0] = k
    xi[j] = xi[j - 1] + h
#print(" ")
#print("xih = ", xi)

def RyngeKyt_1():
    yi1[0] = n
    for i in range(iter):
        if i < iter - 1:
            k1 = h * f(xi[i], yi1[i])
            yi1[i + 1] = yi1[i] + k1
    return yi1

def RyngeKyt_2():
    yi2[0] = n
    for i in range(iter):
        if i < iter - 1:
            k1 = h * f(xi[i], yi2[i])
            k2 = h * f(xi[i] + h, yi2[i] + k1)
            yi2[i + 1] = yi2[i] + (k1 + k2) / 2
            #yi2[i + 1] = yi2[i] + (h / 2) * (f(xi[i] + (h / 2), yi2[i]) + (h / 2) * f(xi[i], yi2[i]))
    return yi2

def RyngeKyt_3():
    yi3[0] = n
    for i in range(iter):
        if i < iter - 1:
            k1 = h * f(xi[i], yi3[i])
            k2 = h * f(xi[i] + (h / 2), yi3[i] + (k1 / 2))
            k3 = h * f(xi[i] + h, yi3[i] - k1 + 2 * k2)
            yi3[i + 1] = yi3[i] + (k1 + 4*k2 + k3) / 6
            #yi3[i + 1] = yi3[i] + (h / 2) * (f(xi[i], yi3[i]) + 3 * f(xi[i] + (2 / 3) * h, yi3[i] + (2 / 3) * f(xi[i], yi3[i])))
    return yi3

def RyngeKyt_4():
    yi4[0] = n
    for i in range(iter):
        if i < iter - 1:
            k1 = h * f(xi[i], yi4[i])
            k2 = h * f(xi[i] + (h / 2), yi4[i] + (k1 / 2))
            k3 = h * f(xi[i] + (h / 2), yi4[i] + (k2 / 2))
            k4 = h * f(xi[i] + h, yi4[i] + k3)
            yi4[i + 1] = yi4[i] + (k1 + 2*k2 + 2*k3 + k4) / 6
    return yi4

# Call
yi_RyngeKyt_1 = RyngeKyt_1()
yi_RyngeKyt_2 = RyngeKyt_2()
yi_RyngeKyt_3 = RyngeKyt_3()
yi_RyngeKyt_4 = RyngeKyt_4()

# Calculate exact solution
for i in range(iter):
    yi_exact[0] = n
    yi_exact[i] = (1746 / math.exp(11)) * math.exp(xi[i]) - xi[i]**3 - 3*xi[i]**2 - 5*xi[i] + 15
# xi_exact = xi

# Calculate errors
for i in range(iter):
    error_RyngeKyt_1[i] = abs(yi_exact[i] - yi_RyngeKyt_1[i]) 
    error_RyngeKyt_2[i] = abs(yi_exact[i] - yi_RyngeKyt_2[i])
    error_RyngeKyt_3[i] = abs(yi_exact[i] - yi_RyngeKyt_3[i])
    error_RyngeKyt_4[i] = abs(yi_exact[i] - yi_RyngeKyt_4[i])

# Declare tables
rynge_kyt_1 = PrettyTable()
rynge_kyt_1.title = 'Rynge-Kyt 1 Table'
rynge_kyt_1.field_names = ['Node', 'Approximate Solution', 'Exact Solution', 'Error']
for i in range(iter):
    rynge_kyt_1.add_row([xi[i], yi_RyngeKyt_1[i], yi_exact[i], error_RyngeKyt_1[i]])

rynge_kyt_2 = PrettyTable()
rynge_kyt_2.title = 'Rynge-Kyt 2 Table'
rynge_kyt_2.field_names = ['Node', 'Approximate Solution', 'Exact Solution', 'Error']
for i in range(iter):
    rynge_kyt_2.add_row([xi[i], yi_RyngeKyt_2[i], yi_exact[i], error_RyngeKyt_2[i]])

rynge_kyt_3 = PrettyTable()
rynge_kyt_3.title = 'Rynge-Kyt 3 Table'
rynge_kyt_3.field_names = ['Node', 'Approximate Solution', 'Exact Solution', 'Error']
for i in range(iter):
    rynge_kyt_3.add_row([xi[i], yi_RyngeKyt_3[i], yi_exact[i], error_RyngeKyt_3[i]])

rynge_kyt_4 = PrettyTable()
rynge_kyt_4.title = 'Rynge-Kyt 4 Table'
rynge_kyt_4.field_names = ['Node', 'Approximate Solution', 'Exact Solution', 'Error']
for i in range(iter):
    rynge_kyt_4.add_row([xi[i], yi_RyngeKyt_4[i], yi_exact[i], error_RyngeKyt_4[i]])

# Print tables
print(rynge_kyt_1)
print(rynge_kyt_2)
print(rynge_kyt_3)
print(rynge_kyt_4)

# Plot exact solution and methods solutions
plt.plot(xi, yi_exact, label='Exact Solution')
plt.plot(xi, yi_RyngeKyt_1, label='Rynge-Kyt 1')
plt.plot(xi, yi_RyngeKyt_2, label='Rynge-Kyt 2')
plt.plot(xi, yi_RyngeKyt_3, label='Rynge-Kyt 3')
plt.plot(xi, yi_RyngeKyt_4, label='Rynge-Kyt 4')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Approximate and Exact Solutions')
plt.legend()
plt.grid(True) #grid line on every tick
plt.show()