from matplotlib import pyplot as plt
from scipy.integrate import odeint
import numpy as np
 
s_dev_list = [1, 0.01, 0.02, 0.03, 0.04, 0.05]
interval = 0.01
rec_cnt = 10
x_cur = 0
strgs = []
y0_true = [0, 1]
def f(u, x):
    return(0.1*u[1], 0.1*(-1*(x**2)*np.sin(u[1])))
 
for s_dev in s_dev_list:
    y_final = []
    x_final = []
    y0 = y0_true
    while x_cur < 10:
        xs = np.arange(x_cur, x_cur + interval, 0.001)
        us = odeint(f, y0, xs)
        for elem in us:
            y_final.append(elem[0])
        for elem in xs:
            x_final.append(elem)
        if (s_dev == 1):
            y0 = [us[-1][0], us[-1][1]]
        else:
            y0 = [us[-1][0] + np.random.normal(0, s_dev), us[-1][1] + np.random.normal(0, s_dev)]
        x_cur += interval
    x_cur = 0
    plt.plot(y_final)
    plt.title('5' + '-' + str(s_dev).replace('.', '_'))
    plt.show()
    strg = map(str, y_final)
    strgs.append(strg)
for s_dev, strg in zip(s_dev_list, strgs):
    name = '5' + '-' + str(s_dev).replace('.', '_') + '.txt'
    if s_dev == 1:
        name = '5-normal.txt'
    f = open(name, 'w')
    f.write("\n".join(strg))
    f.close()