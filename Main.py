import os
from Module_zven import *
import matplotlib.pyplot as plt

K1 = 7.3
K3 = 0.69
K4 = 0.075
K5 = -1.0
K7 = 0.31
T = 0.2
delta = 1

K2 = float(input('Введите значение коэффициента K2: '))
K6 = float(input('Введите значение коэффициента K6: '))
X = 3 * [0] + 100000 * [1]
Y = []
start = [0] * 4
param = [K1, K2, K3, K4, K5, K6, K7, T]

fp = open('output_file.txt', 'w')
fp.write('K2 = ' + str(K2) + ', K6 = ' + str(K6) + '\n')
fp.write('i X[i] Y[i]\n')
for i in range(len(X)):
    Y.append(skhema(X[i], param, start))
    fp.write(str(i+1) + '  ' + str(X[i]) + '   ' + str(round(Y[i], 4)) + '\n')
fp.close()

plt.plot(range(0, len(Y), delta), Y)
plt.title('При K2 = ' + str(K2) + ', K6 = ' + str(K6))
plt.xlabel('t')
plt.ylabel('Y')
plt.grid()
plt.show()

    

