from metalevel import MetaReasoner
from lib.matrix import Matrix
from lib.neuralnetwork import NeuralNetwork

class Reasoner:
    def __init__(self, mode):
        self._version = "CARINA version 3.0 (Python)"
        self._mode = mode

    def neuralnetwork_test(self):
        print("--- Neural Network Test ---")
        nn = NeuralNetwork(2, 2, 1)
        inputs = [1, 0]
        output = nn.feed_forward(inputs)
        print(f"Input: {inputs}, Output: {output}")
        print("-" * 25)

    def matrix_test(self): # Realiza una operación matemática con matrices
        print("--- Matrix Multiplication Test ---")
        m = Matrix(2, 2)
        m2 = Matrix(2, 2)
        m.randomize()
        m2.randomize()
        
        print("Matrix A:")
        m.print()
        print("Matrix B:")
        m2.print()
        
        m3 = Matrix.multiply(m, m2)
        print("Result (A * B):")
        m3.print()
        print("-" * 25)

    def run(self):
        print("Hello, Carina is running now ;)")
        print(f"Current version: {self._version}")
        print(f"Carina is running in mode: {self._mode}")
        self.matrix_test()
        self.neuralnetwork_test()
        
        metareasoner = MetaReasoner("single")
        metareasoner.run()
