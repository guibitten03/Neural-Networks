import numpy as np

class Neuron():
    def __init__(self, w_size, bias):
        
        self.weights = np.random.random((w_size + 1))
        self.weights[0] = bias
        
        
    def _calculate(self, input):
        output = input * self.weights[1:]
        output = output - self.weights[0]
        output = output.sum()
        return output