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
    ax.plot(hm[:4, 0], hm[:4, 1], hm[:4, 2], c='b')
    ax.plot(hm[4:, 0], hm[4:, 1], hm[4:, 2], c='b')

    ax.plot(hm[[3, 7], 0], hm[[3, 7], 1], hm[[3, 7], 2], c='b')
    ax.plot(hm[[2, 6], 0], hm[[2, 6], 1], hm[[2, 6], 2], c='b')
    ax.plot(hm[[1, 5], 0], hm[[1, 5], 1], hm[[1, 5], 2], c='b')
    ax.plot(hm[[0, 4], 0], hm[[0, 4], 1], hm[[0, 4], 2], c='b')
    ax.plot(hm[[0, 3], 0], hm[[0, 3], 1], hm[[0, 3], 2], c='b')
    ax.plot(hm[[4, 7], 0], hm[[4, 7], 1], hm[[4, 7], 2], c='b')

    ax.set_xlim3d([-2, 2])
    ax.set_ylim3d([-2, 2])
    ax.set_zlim3d([-2, 2])


ani = matplotlib.animation.FuncAnimation(fig, animate, frames=80, interval=100, repeat=True)
plt.show()