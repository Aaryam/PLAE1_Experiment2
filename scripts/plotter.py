import numpy as np
import matplotlib.pyplot as plt
import os

path = os.path.join(os.getcwd(), 'data', 'Day1')
print(path)
os.chdir(path)

fileData = np.loadtxt('01062026DataMUO.txt', dtype='float', delimiter='\t', skiprows=1)
columnTitles = np.loadtxt('01062026DataMUO.txt', dtype='str', delimiter='\t', max_rows=1)

plt.plot(fileData[:,0],fileData[:,1])
plt.ylim((0,100))
plt.show()