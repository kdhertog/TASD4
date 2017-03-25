from numpy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


finalx = zeros((271,12))
finalz = zeros((271,12))
finaly = zeros((271,12))

pos = genfromtxt('/Users/Vincent/Google Drive/AE2223-I D4/Data Analysis/Source/sensorlocation.txt',comments='#')
initialx = pos[:,1]
initialz= pos[:,0]
initialy = array(len(initialx)*[0.])

for i in range(0,12):
    testnumber = i + 1
    data = genfromtxt('abaqus_'+str(testnumber)+'.rpt')
    finalpos = data[-1,814:]
    finalx[:,i] = [finalpos[i] for i in range(0,len(finalpos),3)] + initialx
    finaly[:,i] =  [finalpos[j] for j in range(1,len(finalpos),3)] + initialy
    finalz[:,i] = [finalpos[j] for j in range(2,len(finalpos),3)] + initialz

savetxt('finalxposition.txt',finalx)
savetxt('finalyposition.txt',finaly)
savetxt('finalzposition.txt',finalz)
