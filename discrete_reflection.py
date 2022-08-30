mport numpy as np
r_list = [2, 3.3, 3.6, 3.8, 3.97]
s_dev_list = [1, 0.01, 0.02, 0.03, 0.04, 0.05]
s_dev = 0.01
x0 = 0.4
for r in r_list:
    for s in s_dev_list:
        final = [x0]
        for i in range(2, 10001):
            if s == 1:
                final.append(r * final[-1] * (1 - final[-1]))
            else:final.append(r * final[-1] * (1 - final[-1]) + np.random.normal(0, s_dev) * (i % 10 == 0))
        final = map(str, final)
        if s == 1:
            name = '4-'+ str(r).replace('.', '_') + '-normal.txt'
        else: name = '4-' + str(r).replace('.', '_') + '-' + str(s).replace('.', '_') + '.txt'
        f = open(name, 'w')
        f.write("\n".join(final))
        f.close()