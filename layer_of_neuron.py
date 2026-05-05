import numpy as np 

#4 Inputs = The prev layer had 4 neurons
#Input is (1x4)
x = (4.5,2.3,-9.5,1.3)

# Number of inputs at a time = weights per neuron 
#Weights = (3x4)
weights = [[3.2,-4.5,-9.7,6.7],[2.5,-7.6,8.7,-5.4], [2.5,-5.4,9.9,-6.5]]

#Current Layer mei 3 neurons = 3 biases
biases = (3,2,-6)

output_np = (np.dot(x, np.transpose(weights))+biases)
print(output_np)