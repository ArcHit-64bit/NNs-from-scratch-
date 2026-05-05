import numpy as np 
import math

#Layer output, ready to be analysed and prediction
x = [[1.2,-4.5,6.7,-8.7],[4.5,6.7,5.6,3.5],[-3.3,-9.8,-7.5,2.3]]
exp_values = []

for j in exp_values:
    for i,j in j:
        exp_values.append(pow(math.e, j))
print(exp_values)


probability = []
for j in exp_values:
    for i,j in j:
        probability.append(j/sum(exp_values, axis= 1, keepdims=True))
print(probability)
print(sum(probability))
