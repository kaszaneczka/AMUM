import numpy as np
import matplotlib.pyplot as plt


romb = np.array([[0, 1], [1, 0], [0, -1], [-1, 0]])

plt.fill(romb[:, 0], romb[:, 1])
plt.show()

import matplotlib.animation

cube = np.array([[-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1], [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]])

fig = plt.figure()
ax = fig.add_subplot(projection='3d')


def fun(figure, t):
    return figure @ np.array([[np.cos(0.1 * t), -np.sin(0.1 * t), 0], [np.sin(0.1 * t), np.cos(0.1 * t), 0], [0, 0, 1]])


def animate(i):
    ax.clear()
    hm = fun(cube, i)
    ax.scatter(hm[:, 0], hm[:, 1], hm[:, 2])
    ax.set_xlim3d([-2, 2])
    ax.set_ylim3d([-2, 2])
    ax.set_zlim3d([-2, 2])


ani = matplotlib.animation.FuncAnimation(fig, animate, frames=80, interval=100, repeat=True)
plt.show()