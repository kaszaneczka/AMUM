import numpy as np
import matplotlib.pyplot as plt


romb = np.array([[0, 1], [1, 0], [0, -1], [-1, 0]])

plt.fill(romb[:, 0], romb[:, 1])
plt.show()

import matplotlib.animation


def fun(figure, t):
    return figure @ np.array([[t, 0], [0, 1]])


fig, ax = plt.subplots(figsize=(7, 7))


def animate(i):
    fig.clear()
    hm = fun(romb, i)
    plt.xlim([-10, 10])
    plt.ylim([-10, 10])

    plt.fill(hm[:, 0], hm[:, 1])


ani = matplotlib.animation.FuncAnimation(fig, animate, frames=80, interval=100, repeat=True)
plt.show()
