import random

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def randomize(self):
        self.data = [[random.random() for _ in range(self.cols)] for _ in range(self.rows)]

    def print(self):
        # A simple print format, not as neat as console.table
        for row in self.data:
            print(" ".join(f"{x:.4f}" for x in row))
        print()

    @staticmethod
    def multiply(a, b):
        if a.cols != b.rows:
            raise ValueError("Las columnas de A deben coincidir con las filas de B")
        
        result = Matrix(a.rows, b.cols)
        for i in range(result.rows):
            for j in range(result.cols):
                sum_val = 0
                for k in range(a.cols):
                    sum_val += a.data[i][k] * b.data[k][j]
                result.data[i][j] = sum_val
        return result
