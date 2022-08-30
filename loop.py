import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import logsumexp
import matplotlib.pyplot as plt
 
u0, v0, w0 = 0.000001, 0.00000001, 1.05
interval = 0.01
count_rec = 10
x_final = []
y_final = []
# z_final = []
s_dev = 0.01
tmax, n = 100, 10000
param = 0
counter = 0
 
name = '3_normal.txt'
 
def roll(param, a, b):
    while param < 10:
        try:
            soln = solve_ivp(eq, (param, param + interval), (a, b),
                             dense_output=True)
        except:
            raise Exception
        t = np.linspace(param, param + interval, count_rec)
        x, y = soln.sol(t)
        for elem in x:
            x_final.append(elem)
        for elem in y:
            y_final.append(elem)
        a = x_final[-1] + np.random.normal(0, s_dev)
        # a = x_final[-1]
        # b = y_final[-1]
        b = y_final[-1] + np.random.normal(0, s_dev)
 
        param += interval
    return x_final, y_final
 
def eq(t, X):
    x, y = X
    try:
        xp = y
        yp = -x
        return xp, yp
    except RuntimeWarning:
        return 'smth'
 
 
 
flag = 1
while flag == 1:
    try:
        x_final, y_final = roll(0, u0, v0)
        plt.plot(x_final, y_final)
        flag = 0
        plt.show()
        final = map(str, y_final)
        f = open(name, 'w')
        f.write("\n".join(final))
        f.close()
        print(counter)
    except RuntimeWarning:
        counter += 1
        flag = 1
        print("Error\n")
    except:
        counter += 1
        flag = 1
        print("Error\n")