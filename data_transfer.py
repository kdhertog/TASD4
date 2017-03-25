''' Displace data to desired location. Run program and give inputs. - Vincent Meijer.'''
from numpy import *
outputname = input('File output name: ')
key = int(input('Give test number: '))
columns = input('Give column range (e.g. 1:4): ').split(':')
data = genfromtxt('abaqus_'+str(key)+'.rpt')
f = open(outputname+'.txt','w')
for i in range(len(data[:,0])):
    line = ''
    for j in range(int(columns[0]),int(columns[1])+1):
        line = line+(str(data[i,j])+'\t')
    line = line + '\n'
    f.write(line)
f.close()
print('Ready.')
