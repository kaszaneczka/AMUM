#cmap = 'jet'

import numpy as np

import matplotlib.pyplot as plt

import matplotlib.animation

from matplotlib.offsetbox import (TextArea, DrawingArea, OffsetImage,
                                  AnnotationBbox)



class lab8:

    def __init__(self):



        with open('animals.npz', 'rb') as f:
            self.animals = np.load(f)['animals']
        self.wzrost = [float(i) for i in self.animals[:, 3]]
        self.waga = [float(i) for i in self.animals[:, 2]]
        self.zdj = self.animals[:, 4]

    def f1(self, x, y): return 0.5 * np.sin(x ** 3) + 0.25 * np.sin((y + np.pi) ** 2)

    def f(self, x, y, t): return 0.5 * np.sin(x ** 3) + 0.25 * np.sin((y - t) ** 2)

    def zad1(self):
        self.fig, self.ax = plt.subplots(figsize=(10, 7))
        n = 100
        x = np.linspace(-np.pi / 2, np.pi / 2, n)
        y = np.linspace(-np.pi, np.pi / 2, n)

        X, Y = np.meshgrid(x, y)
        self.ax.set_xlim(-np.pi / 2, np.pi / 2)
        self.ax.set_ylim(-np.pi, np.pi / 2)
        z = self.f1(X, Y)

        plt.contourf(X, Y, z, cmap='jet')
        plt.contour(X, Y, z, cmap='jet')
        plt.show()

    def animate(self,i):
        self.fig.clear()
        n = 100
        x = np.linspace(-np.pi / 2, np.pi / 2, n)
        y = np.linspace(0, np.pi * 1.5, n)

        z = [[self.f(xx, yy, i*0.2) for xx in x] for yy in y]

        X, Y = np.meshgrid(x, y)

        plt.contourf(X, Y, z, cmap='jet')
        plt.contour(X, Y, z, cmap='jet')

    def zad2(self):
        self.fig, self.ax = plt.subplots(figsize=(10, 7))
        n = 100
        x = np.linspace(-np.pi / 2, np.pi / 2, n)
        y = np.linspace(0, np.pi * 1.5, n)

        z = [[self.f(xx, yy, 0) for xx in x] for yy in y]

        self.ax.set_xlim(-np.pi / 2, np.pi / 2)
        self.ax.set_ylim(0, np.pi * 1.5)

        X, Y = np.meshgrid(x, y)


        plt.contourf(X, Y, z, cmap='jet')
        plt.contour(X, Y, z, cmap='jet')

        ani = matplotlib.animation.FuncAnimation(self.fig, self.animate, frames=80, interval=100, repeat=False)
        plt.show()

    def plot_3d(self):
        self.fig1 = plt.figure(figsize=(10, 9))
        self.ax1 = self.fig1.add_subplot(projection='3d')
        n = 100
        x = np.linspace(-np.pi / 2, np.pi / 2, n)
        y = np.linspace(0, np.pi * 1.5, n)
        X, Y = np.meshgrid(x, y)
        z = self.f1(X, Y)


        self.ax1.set_xlim3d([-np.pi / 2, np.pi / 2])
        self.ax1.set_ylim3d([0, np.pi * 1.5])
        self.ax1.plot_surface(X, Y, z,cmap="gist_ncar")
        plt.show()

    def animate_3dd(self,i):
        self.ax1.clear()
        n = 100
        x = np.linspace(-np.pi / 2, np.pi / 2, n)
        y = np.linspace(0, np.pi * 1.5, n)
        X, Y = np.meshgrid(x, y)
        z = self.f(X, Y, i*0.1)
        self.ax1.plot_surface(X, Y, z, cmap="gist_ncar")

    def animate_3d(self):
        self.fig1 = plt.figure(figsize=(10, 9))
        self.ax1 = self.fig1.add_subplot(projection='3d')
        n = 100
        x = np.linspace(-np.pi / 2, np.pi / 2, n)
        y = np.linspace(0, np.pi * 1.5, n)
        X, Y = np.meshgrid(x, y)
        z = self.f(X, Y,0)

        self.ax1.set_xlim3d([-np.pi / 2, np.pi / 2])
        self.ax1.set_ylim3d([0, np.pi * 1.5])
        self.ax1.plot_surface(X, Y, z, cmap="gist_ncar")
        ani = matplotlib.animation.FuncAnimation(self.fig1, self.animate_3dd, frames=80, interval=200, repeat=False)
        plt.show()

    def location(self,event):

        for a in range(9):
            try:
                if event.ydata < self.wzrost[a] + 0.2 and event.ydata > self.wzrost[a] - 0.2 and event.xdata < self.waga[a] + 0.2 and event.xdata > self.waga[a] -0.2:
                    print('wartosc x',event.xdata)
                    print('wartosc y',event.ydata)

                    self.boxy[a].set_visible(True)
                    self.ax2.add_artist(self.boxy[a])
                    plt.show()
                else:
                    self.boxy[a].set_visible(False)
                    print('wartosc x', event.xdata)
                    print('wartosc y', event.ydata)
                    plt.show()
            except:
                pass

    def zadanie5(self):

        self.fig2, self.ax2 = plt.subplots(figsize=(10, 7))
        plt.plot(self.waga,self.wzrost,'bo',picker=True, pickradius=200)
        plt.xlabel('waga')
        plt.ylabel('wzrost')
        self.zdjecia = []
        self.boxy = []
        for a in range(len(self.animals[:,4])):
            self.zdjecia.append(matplotlib.image.imread(self.zdj[a]))
            imagebox = OffsetImage(self.zdjecia[a], zoom=0.2)
            imagebox.image.axes = self.ax2
            xy = (self.waga[a], self.wzrost[a])
            self.boxy.append(AnnotationBbox(imagebox, xy,
                                     xybox=(len(self.zdjecia[a][0])*0.1, len(self.zdjecia[a])*0.1),
                                     xycoords='data',
                                     boxcoords="offset points",
                                     pad=0.1
                                     ))
            self.boxy[a].set_visible(False)
        print(len(self.zdjecia[0][0]))

        self.fig2.suptitle('Najedź myszką na punkt')

        self.fig2.canvas.mpl_connect('motion_notify_event', self.location)


        print(self.animals)
        plt.show()
        print(self.animals[:,1])






wizualizacja = lab8()
#wizualizacja.zad2()
#wizualizacja.zad1()
#wizualizacja.plot_3d()
#wizualizacja.animate_3d()
wizualizacja.zadanie5()






# plt.scatter(x_test[:, 0], x_test[:, 1], marker="o", c=y_test, s=25, edgecolor="k")