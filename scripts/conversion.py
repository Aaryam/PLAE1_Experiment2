import numpy as np
import matplotlib.pyplot as plt
import os
import scipy

delaysList = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4, 4.25, 4.5, 4.75]

def getNonZeroList(data):
    arr = list()
    for i in range(len(data[:,0])):
        if data[:,1][i] > 5:
            arr.append([data[:,0][i], data[:,1][i]])

    newArr = list()
    newArr.append(arr[0][0])
    for i in range(len(arr)):
        if i > 0:
            if abs(arr[i][0] - arr[i - 1][0]) > 1:
                newArr.append(arr[i][0])
    print(newArr)
    return newArr

def fitting_funct(xVal, a, b):
    '''Fitting function for the given datapoints'''
    return a * xVal + b

path = os.path.join(os.getcwd(), 'data', 'Day2')
os.chdir(path)

fileData = np.loadtxt('chanConversion.txt', dtype='float', delimiter='\t', skiprows=1)
columnTitles = np.loadtxt('chanConversion.txt', dtype='str', delimiter='\t', max_rows=1)

popt, _ = scipy.optimize.curve_fit(fitting_funct, delaysList, getNonZeroList(fileData), sigma=1)

realData = scipy.odr.RealData(getNonZeroList(fileData), 
                              delaysList, 
                              sx=[1 for i in range(len(getNonZeroList(fileData)))], 
                              sy=[0.05 for i in range(len(getNonZeroList(fileData)))])
modelODR = scipy.odr.Model(lambda params, xVal: fitting_funct(xVal, params[0], params[1]))
odr      = scipy.odr.ODR(realData, modelODR, beta0=[0,0])
output   = odr.run()

print(output.beta)
print(output.cov_beta)

for i in range(len(output.cov_beta)):
    print(f"Statistical error on parameter parameter {i}: {round(np.sqrt(output.cov_beta[i][i])/(abs(output.beta[i]))*100, 2)}%")

# plt.plot(fileData[:,0],fileData[:,1])
# plt.ylim((0,100))

plt.plot(delaysList,getNonZeroList(fileData))
plt.show()