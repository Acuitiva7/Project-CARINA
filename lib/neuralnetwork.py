import math

class NeuralNetwork:
    def __init__(self, input_nodes, hidden_nodes, output_nodes):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes

    # función de activación
    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def feed_forward(self, inputs):
        # aquí hacemos un cálculo muy simplificado
        hidden = [self.sigmoid(v) for v in inputs]
        output = sum(hidden) / len(hidden)
        return [output] # salida como lista
