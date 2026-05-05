import numpy as np 
import math

#Layer output - Ready to be predicted and analysed
x =[-1.2, 0.4, 0, -0.9, 2.3]
exp_values = []

#Making a matrix into a matrix with each element as e^each element
for i in x: 
    exp_values.append(pow(math.e, i))
print(exp_values)

#Probability finding by = favourible outcome/total outcomes
probability = []
sum_of_exp_values = sum(exp_values)
for i in exp_values:
    probability.append(i/sum_of_exp_values) #Matrix banane k liye humesha append use karo 

#Spits out a matrix of probability of values
print(probability)

#Sum of all probability values = 1 
#We use softmax to convert random nuumbers be confined to 0 to 1, which is essentially probability of each number 
print(sum(probability))
