import numpy as np
import matplotlib.pyplot as plt
import os

path = os.path.join(os.getcwd(), 'data', 'Day1')
print(path)
os.chdir(path)

# path = os.path.join(os.path.pardir(os.getcwd()), 'data', 'Day1', '01062026DataMUO.txt')

fileData = np.loadtxt('01062026DataMUO.txt', dtype='float', delimiter='\t', skiprows=1)
columnTitles = np.loadtxt('01062026DataMUO.txt', dtype='str', delimiter='\t', max_rows=1)

plt.plot(fileData[:,0],fileData[:,1])
plt.ylim((0,100))
plt.show()