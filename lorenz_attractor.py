import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
 
sigma, beta, rho = 20, 5.31, 56
u0, v0, w0 = 2, 2, 2.1
interval = 0.1
count_rec = 10
t_cur = 0
x_final = []
y_final = []
z_final = []
s_dev = 0.05
tmax, n = 100, 10000
 
def lorenz_1(t, X, sigma, beta, rho):
    """The Lorenz equations."""
    u, v, w = X
    up = -sigma*(u - v)
    vp = rho*u - v - u*w
    wp = -beta*w + u*v
    return up, vp, wp
 
while t_cur < 100:
    soln = solve_ivp(lorenz_1, (t_cur, t_cur + interval), (u0, v0, w0),
                     args=(sigma, beta, rho), dense_output=True)
    t = np.linspace(t_cur, t_cur + interval, count_rec)
    x, y, z = soln.sol(t)
    for elem in x:
        x_final.append(elem)
    for elem in y:
        y_final.append(elem)
    for elem in z:
        z_final.append(elem)
    u0 = x_final[-1] + np.random.normal(0, s_dev)
    v0 = y_final[-1] +  np.random.normal(0, s_dev)
    w0 = z_final[-1] + np.random.normal(0, s_dev)
    t_cur += interval
 
final = map(str, y_final)
name = ('1_0' + str(s_dev)[2:] + '.txt.') if len(str(s_dev))>=4 else  '1_0' + str(s_dev)[1:] + '.txt.' if len(str(s_dev)) ==2 else '1_0' + str(s_dev) + '.txt'
f = open(name, 'w')
f.write("\n".join(final))
f.close()
plt.plot(y_final)
plt.show()