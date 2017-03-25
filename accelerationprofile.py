from numpy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

testnumber = 1

A = genfromtxt('abaqus_'+str(testnumber)+'.rpt')
pos = genfromtxt('sensorlocation.txt')
x = pos[:,0]
y = pos[:,1]

fig = plt.figure()
ax = fig.add_subplot(111,projection ='3d')
plt.ion()
plt.show()

for i in range(len(A[:,0])):
    z = A[i,5:(5+len(x))]
    print(z)
    ax.plot_surface(x,y,z)
    plt.draw()

print('Ready.')





