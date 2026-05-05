import numpy as np 

#A Batch of input, with 3 sets of inputs with each containing 4 values
x = [[1.2,-4.5,6.7,-8.7],[4.5,6.7,5.6,3.5],[-3.3,-9.8,-7.5,2.3]]

#weights for 3 neurons, 4 features each
weights = [[3.2,-4.5,-9.7,6.7],[2.5,-7.6,8.7,-5.4], [2.5,-5.4,9.9,-6.5]]

#3 neurons = 3 biases 
biases = (3,2,-6)

output_np = np.dot(x, np.transpose(weights))+biases
print(output_np)