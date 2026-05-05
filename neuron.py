import numpy as np
import math 
import random 


#Calculating the output of a single neuron with 3 inputs manually
X = [4.6,2.3,9.7]
weight = [-4.5,-9.5,-3]
bias = 3

output_manual = ((X[0]*weight[0]+X[1]*weight[1]+X[2]*weight[2])+bias)
print(output_manual)

#Calculating the output of a single neuron with 3 inputs using numpy
output_numpy = (np.dot(X, weight)+bias)
print(output_numpy)

