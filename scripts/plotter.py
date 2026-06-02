import numpy as np
import matplotlib.pyplot as plt
import os

import numpy as np
import matplotlib.pyplot as plt

path = os.chdir(os.path.join(os.getcwd(), 'data', 'Day1', '01062026DataMUO.txt'))

# path = os.path.join(os.path.pardir(os.getcwd()), 'data', 'Day1', '01062026DataMUO.txt')

fileData = np.loadtxt(path, dtype='str', delimiter=',', skiprows=1)
columnTitles = np.loadtxt('01062026DataMUO', dtype='str', delimiter=',', max_rows=1)

print(fileData)