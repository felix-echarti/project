import numpy as np

par_min = 0
par_max = 0.2
delta_par = 0.1

arg_min = 0
arg_max = 0.2
delta_arg = 0.1

max_attract = 100
min_attract = -100

h = 0.01
t_max = 10.0
from array import *

t = np.arange(0.0, t_max, h)


def x_t(x, y, z, w):
    return (-y - z - w)


def y_t(x, y, z, w):
    return (-x)


def z_t(x, y, z, w, a, b):
    return (a * (y - y ** 2) - b * z)


def w_t(x, y, z, w, c, d):
    return (c * (z / 2 - z ** 2) - d * w)


par_min_int = int(par_min / delta_par)
par_max_int = int(par_max / delta_par)
arg_min_int = int(arg_min / delta_arg)
arg_max_int = int(arg_max / delta_arg)

print('lol')
x = array('d', [0])
y = array('d', [0])
z = array('d', [0])
w = array('d', [0])

for a1 in range(par_min_int, par_max_int):
    for b1 in range(par_min_int, par_max_int):
        print(b1)
        for c1 in range(par_min_int, par_max_int):
            for d1 in range(par_min_int, par_max_int):
                for x_01 in range(arg_min_int, arg_max_int):
                    for y_01 in range(arg_min_int, arg_max_int):
                        for z_01 in range(arg_min_int, arg_max_int):
                            for w_01 in range(arg_min_int, arg_max_int):
                                a = a1 * delta_par
                                b = b1 * delta_par
                                c = c1 * delta_par
                                d = d1 * delta_par
                                x_0 = x_01 * delta_arg
                                y_0 = y_01 * delta_arg
                                z_0 = z_01 * delta_arg
                                w_0 = w_01 * delta_arg

                                x = [x_0]
                                y = [y_0]
                                z = [z_0]
                                w = [w_0]
                                for i in range(1, int(t_max / h)):
                                    if (i == int(t_max / h) - 1):
                                        print(
                                            'a={}, b={}, c={}, d={}, x_0={}, y_0={}, z_0={}, w_0={}'.format(a, b, c, d,
                                                                                                            x_0, y_0,
                                                                                                            z_0, w_0))
                                    new_thing = x[i - 1] + h * x_t(x[i - 1], y[i - 1], z[i - 1], w[i - 1])
                                    if new_thing < max_attract and new_thing > min_attract:
                                        x.append(new_thing)
                                    else:
                                        break
                                    new_thing = y[i - 1] + h * y_t(x[i - 1], y[i - 1], z[i - 1], w[i - 1])
                                    if new_thing < max_attract and new_thing > min_attract:
                                        y.append(new_thing)
                                    else:
                                        break
                                    new_thing = z[i - 1] + h * z_t(x[i - 1], y[i - 1], z[i - 1], w[i - 1], a, b)
                                    if new_thing < max_attract and new_thing > min_attract:
                                        z.append(new_thing)
                                    else:
                                        break
                                    new_thing = w[i - 1] + h * w_t(x[i - 1], y[i - 1], z[i - 1], w[i - 1], c, d)
                                    if new_thing < max_attract and new_thing > min_attract:
                                        w.append(new_thing)
                                    else:
                                        break