#cmap = 'jet'

import numpy as np

import matplotlib.pyplot as plt

import matplotlib.animation


def f1(x,y): return 0.5*np.sin(x**3) + 0.25*np.sin((y + np.pi)**2)

def zad1():
    n = 100
    x = np.linspace(-np.pi/2,np.pi/2,n)
    y = np.linspace(-np.pi,np.pi/2,n)


    X,Y = np.meshgrid(x, y)
    z = f1(X,Y)

    plt.contourf(X, Y, z, cmap='jet')
    plt.contour(X, Y, z, cmap='jet')
    plt.show()

def f(x, y, t): return 0.5*np.sin(x**3) + 0.25*np.sin((y - t)**2)




class animate(zad):
    def animate(i):
        fig.clear()
        n = 100
        x = np.linspace(-np.pi / 2, np.pi / 2, n)
        y = np.linspace(0, np.pi * 1.5, n)

        z = [[f(xx, yy, i) for xx in x] for yy in y]

        X, Y = np.meshgrid(x, y)

        plt.contourf(X, Y, z, cmap='jet')
        plt.contour(X, Y, z, cmap='jet')


    def zad2():
        n = 100
        x = np.linspace(-np.pi / 2, np.pi / 2, n)
        y = np.linspace(0, np.pi * 1.5, n)

        z = [[f(xx, yy, 0) for xx in x] for yy in y]

        X, Y = np.meshgrid(x, y)

        fig, ax = plt.subplots(figsize=(10, 7))

        ax.set_xlim(-np.pi / 2, np.pi / 2)
        ax.set_ylim(0, np.pi * 1.5)

        plt.contourf(X, Y, z, cmap='jet')
        plt.contour(X, Y, z, cmap='jet')

        ani = matplotlib.animation.FuncAnimation(fig, animate, frames=80, interval=100, repeat=False)
        plt.show()

zad2()
#zad1()







# plt.scatter(x_test[:, 0], x_test[:, 1], marker="o", c=y_test, s=25, edgecolor="k")