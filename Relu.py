import numpy as np

x = [-1.2, 0.4, 0, -0.9, 2.3]

#ReLU is a function - i<0 put 0; i>0 put i 
output_ReLU_manual = [0, 0.4, 0, 0, 2.3]

#Making a class Activation_Relu, In which we define a method - forward for processing 
#that produces an output
class Activation_ReLU:
    def forward(self, input):
        self.output = np.maximum(0,input)

Relu_output_np = Activation_ReLU() #Variable
Relu_output_np.forward(x)
print(Relu_output_np.output)


#Without numpy
class Activation_Relu_Manual:
    def forward(self, input):
        self.output = []
        for i in input:
            self.output.append(max(0,i))

#delcaring a variable, processing the class and extracting output
Relu_output_manual = Activation_Relu_Manual()
Relu_output_manual.forward(x)
print(Relu_output_manual.output)