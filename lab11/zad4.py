import numpy as np
import matplotlib.pyplot as plt


romb = np.array([[0, 1], [1, 0], [0, -1], [-1, 0]])

plt.fill(romb[:, 0], romb[:, 1])
plt.show()

import matplotlib.animation


figure_3 = np.c_[romb, np.array([1,1,1,1])]


def fun(figure, t):
    return figure @ np.array(
        [[np.cos(0.1 * t), -np.sin(0.1 * t), 0], [np.sin(0.1 * t), np.cos(0.1 * t), 0], [0, 0, 1]]) @ np.array(
        [[1, 0, 0.1 * t], [0, 1, 0.2 * t], [0, 0, 1]]).T


fig, ax = plt.subplots(figsize=(7, 7))


def animate(i):
    fig.clear()
    hm = fun(figure_3, i)
    plt.xlim([-1, 10])
    plt.ylim([-1, 10])

    plt.fill(hm[:, 0], hm[:, 1])


ani = matplotlib.animation.FuncAnimation(fig, animate, frames=80, interval=100, repeat=True)
plt.show()