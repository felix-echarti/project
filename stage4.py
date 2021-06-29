import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
% matplotlib
notebook
a0 = -1
b0 = 9.1
c0 = 1.2
d0 = 0.2
a = a0
b = b0
c = c0
d = d0
h = 0.01
t_max = 100.0
from array import *

t = np.arange(0.0, t_max, h)
x_0 = 0.1
y_0 = 0.1
z_0 = 0.1
w_0 = 0.1
x = array('d', [x_0]);
y = array('d', [y_0]);
z = array('d', [z_0]);
w = array('d', [w_0]);


def x_t(x, y, z, w):
    return (-y - z - w)


def y_t(x, y, z, w):
    return (x)


def z_t(x, y, z, w, a, b):
    return (a * (y - y ** 2) - b * z)


def w_t(x, y, z, w, c, d):
    return (c * (z / 2 - z ** 2) - d * w)


for i in range(1, int(t_max / h)):
    x.append(x[i - 1] + h * x_t(x[i - 1], y[i - 1], z[i - 1], w[i - 1]))
    y.append(y[i - 1] + h * y_t(x[i - 1], y[i - 1], z[i - 1], w[i - 1]))
    z.append(z[i - 1] + h * z_t(x[i - 1], y[i - 1], z[i - 1], w[i - 1], a, b))
    w.append(w[i - 1] + h * w_t(x[i - 1], y[i - 1], z[i - 1], w[i - 1], c, d))
    if x[i] < -100 or x[i] > 100 or y[i] < -100 or y[i] > 100 or z[i] < -100 or z[i] > 100 or w[i] < -100 or w[i] > 100:
        break
print(len(x))
print(len(y))
print(len(z))
print(len(w))
# print(x)
# print(y)
# print(z)
# print(w)
import matplotlib.pyplot as plt_3d
from mpl_toolkits.mplot3d import Axes3D

fig_3d = plt_3d.figure()
ax_3d = fig_3d.add_subplot(111, projection='3d')
ax_3d.plot(x, y, z, label='parametric curve')
plt_3d.axis([-1000, 1000, -1000, 1000])

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.55)

l, = plt.plot(x, y, lw=2, color='red')
plt.axis([-100, 100, -100, 100])

axcolor = 'lightgoldenrodyellow'
ax_param_a = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
ax_param_b = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
ax_param_c = plt.axes([0.25, 0.2, 0.65, 0.03], facecolor=axcolor)
ax_param_d = plt.axes([0.25, 0.25, 0.65, 0.03], facecolor=axcolor)

s_param_a = Slider(ax_param_a, 'a', -10, 10.0, valinit=a0)
s_param_b = Slider(ax_param_b, 'b', -10, 10.0, valinit=b0)
s_param_c = Slider(ax_param_c, 'c', -10, 10.0, valinit=c0)
s_param_d = Slider(ax_param_d, 'd', -10, 10.0, valinit=d0)

ax_param_x0 = plt.axes([0.25, 0.3, 0.65, 0.03], facecolor=axcolor)
ax_param_y0 = plt.axes([0.25, 0.35, 0.65, 0.03], facecolor=axcolor)
ax_param_z0 = plt.axes([0.25, 0.4, 0.65, 0.03], facecolor=axcolor)
ax_param_w0 = plt.axes([0.25, 0.45, 0.65, 0.03], facecolor=axcolor)

s_param_x0 = Slider(ax_param_x0, 'x_0', -10, 10.0, valinit=x_0)
s_param_y0 = Slider(ax_param_y0, 'y_0', -10, 10.0, valinit=y_0)
s_param_z0 = Slider(ax_param_z0, 'z_0', -10, 10.0, valinit=z_0)
s_param_w0 = Slider(ax_param_w0, 'w_0', -10, 10.0, valinit=w_0)


def update(val):
    plt_3d.show()
    a = s_param_a.val
    b = s_param_b.val
    c = s_param_c.val
    d = s_param_d.val

    x_0 = s_param_x0.val
    y_0 = s_param_y0.val
    z_0 = s_param_z0.val
    w_0 = s_param_w0.val

    x = [x_0]
    y = [y_0]
    z = [z_0]
    w = [w_0]

    for i in range(1, int(t_max / h)):
        x.append(x[i - 1] + h * x_t(x[i - 1], y[i - 1], z[i - 1], w[i - 1]))
        y.append(y[i - 1] + h * y_t(x[i - 1], y[i - 1], z[i - 1], w[i - 1]))
        z.append(z[i - 1] + h * z_t(x[i - 1], y[i - 1], z[i - 1], w[i - 1], a, b))
        w.append(w[i - 1] + h * w_t(x[i - 1], y[i - 1], z[i - 1], w[i - 1], c, d))
        if x[i] < -100 and x[i] > 100 and y[i] < -100 and y[i] > 100 and z[i] < -100 and z[i] > 100 and w[i] < -100 and \
                w[i] > 100:
            break

    l.set_ydata(y)
    l.set_xdata(x)
    fig.canvas.draw_idle()


resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')
s_param_a.on_changed(update)
s_param_b.on_changed(update)
s_param_c.on_changed(update)
s_param_d.on_changed(update)
s_param_x0.on_changed(update)
s_param_y0.on_changed(update)
s_param_z0.on_changed(update)
s_param_w0.on_changed(update)


def reset(event):
    s_param_a.reset()
    s_param_b.reset()
    s_param_c.reset()
    s_param_d.reset()
    s_param_x0.reset()
    s_param_y0.reset()
    s_param_z0.reset()
    s_param_w0.reset()


button.on_clicked(reset)
rax = plt.axes([0.025, 0.5, 0.1, 0.3], facecolor=axcolor)
radio = RadioButtons(rax, ('x_y', 'x_z', 'x_w', 'y_z', 'y_w', 'z_w'), active=0)


def type_graph(label):
    if label == 'x_y':
        l.set_ydata(y)
        l.set_xdata(x)
    elif label == 'x_z':
        l.set_ydata(z)
        l.set_xdata(x)
    elif label == 'x_w':
        l.set_ydata(w)
        l.set_xdata(x)
    elif label == 'y_z':
        l.set_ydata(z)
        l.set_xdata(y)
    elif label == 'y_w':
        l.set_ydata(w)
        l.set_xdata(y)
    elif label == 'z_w':
        l.set_ydata(w)
        l.set_xdata(z)
    fig.canvas.draw_idle()


radio.on_clicked(type_graph)