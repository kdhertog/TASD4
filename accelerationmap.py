from numpy import *


class PointBrowser(object):

    def __init__(self):
        self.lastind = 0
        self.dir = 0
        self.text = ax.text(0.05, 0.95, 'selected: 1',
                            transform=ax.transAxes, va='top')
        self.selected, = ax.plot(X[0],Z[0], 'o', ms=12, alpha=0.4,
                                 color='yellow', visible=False)

    def onpress(self, event):
        inc = 0
        if self.lastind is None:
            return
        if event.key not in ('n','p','x','y','z'):
            return
        if event.key == 'n':
            inc = 1
            self.dir = 0
        if event.key == 'p':
            inc = -1
            self.dir = 0
        if event.key == 'x':
            self.dir = 0
        if event.key == 'y':
            self.dir = 1
        if event.key == 'z':
            self.dir = 2
       

        self.lastind += inc
        self.lastind = clip(self.lastind, 0, 271)
        self.update()

    def onpick(self, event):

        if event.artist != line:
            return True

        N = len(event.ind)
        if not N:
            return True

        # the click locations
        x = event.mouseevent.xdata
        y = event.mouseevent.ydata

        distances = hypot(x - X[event.ind], y - Z[event.ind])
        indmin = distances.argmin()
        dataind = event.ind[indmin]

        self.lastind = dataind
        self.update()

    def update(self):
        if self.lastind is None:
            return
        sensornumber = self.lastind
        dataind = self.lastind  + self.dir
        ax1.cla()
        ax1.plot(T,data[:,(812 + dataind)])
        ax1.set_xlabel = 'Time [s]'
        ax1.set_ylabel = 'Displacement [mm]'
        ax2.cla()
        ax2.plot(T,data[:,dataind])
        ax2.set_xlabel = 'Time [s]'
        ax2.set_ylabel = 'Acceleration [m/s2]'
        self.selected.set_visible(True)
        self.selected.set_data(X[sensornumber], Z[sensornumber])

        self.text.set_text('selected: %d' % sensornumber)
        fig.canvas.draw()


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    data = genfromtxt('abaqus_12.rpt')
    pos = genfromtxt('sensorlocation.txt',comments='#')
    X = pos[:,1]
    Z = pos[:,0]
    T = data[:,0]
    data = data[:,1:]

    fig, (ax, ax1, ax2 )= plt.subplots(3, 1)
    ax.set_title("Click on point to plot displacement and acceleration history. Use 'n' and 'p' to browse.\n \ "
                 "Change plot direction by using 'x','y' and 'z'" )
    ax.set_xlabel = 'X [mm]'
    ax.set_ylabel = 'Z [mm]'
    ax.set_ylim(0,3000.)
    line, = ax.plot(X,Z, 'o', picker=5)  # 5 points tolerance
    browser = PointBrowser()

    fig.canvas.mpl_connect('pick_event', browser.onpick)
    fig.canvas.mpl_connect('key_press_event', browser.onpress)

    plt.show()


