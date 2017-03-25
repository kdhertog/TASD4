'Scatter plot of initial sensor location (in blue) and final sensor location (in red).\
start by running the program.. Authors: Vincent Meijer, Tristan Hamers'


from numpy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class PointBrowser(object):

    def __init__(self):
        self.lastind = 1
        self.update()

    def onpress(self, event):
        if self.lastind is None:
            return
        if event.key not in ('n', 'p'):
            return
        if event.key == 'n':
            inc = 1
        else:
            inc = -1

        self.lastind += inc
        self.lastind = clip(self.lastind, 1, 12)
        self.update()

    def update(self):
        if self.lastind is None:
            return

        dataind = self.lastind -1

        ax.cla()
        ax.scatter(initialx, initialz, initialy, c='b',label= 'Initial')
        ax.scatter(finalx[:,dataind],finalz[:,dataind],finaly[:,dataind],c='r',label= 'Final')
        ax.set_zlim(-100.,100.)
        ax.set_xlabel('X [mm]')
        ax.set_ylabel('Z[mm]')
        ax.set_zlabel('Y[mm]')
        ax.legend()
        ax.set_title('Test '+str(dataind + 1))


        fig.canvas.draw()

pos = genfromtxt('sensorlocation.txt',comments='#')
initialx = pos[:,1]
initialz= pos[:,0]
initialy = array(len(initialx)*[0.])
finalx = genfromtxt('finalxposition.txt')
finalz = genfromtxt('finalzposition.txt')
finaly = genfromtxt('finalyposition.txt')

fig = plt.figure()
fig.suptitle(" Press 'n' for next test and 'p' for previous test ")
ax = fig.add_subplot(111,projection ='3d')
browser = PointBrowser()
fig.canvas.mpl_connect('key_press_event', browser.onpress)

plt.show()



