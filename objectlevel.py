from metalevel import MetaReasoner
from lib.matrix import Matrix
from lib.neuralnetwork import NeuralNetwork

class Reasoner:
    def __init__(self, mode):
        """
        Inicializa el Reasoner del Nivel de Objeto.
        
        Args:
            mode (str): El modo de operación (actualmente no utilizado, pero parte del diseño original).
        """
        self._version = "CARINA version 3.1 (Python - Conectado)"
        self._mode = mode
        # Se añade una 'base de conocimiento' para almacenar los 'hechos' que el Nivel de Objeto aprende.
        self.knowledge_base = []

    def neuralnetwork_test(self):
        """
        Ejecuta una prueba de la red neuronal.
        Ahora devuelve el resultado para que pueda ser utilizado.
        """
        print("--- Neural Network Test ---")
        nn = NeuralNetwork(2, 2, 1)
        inputs = [1, 0]
        output = nn.feed_forward(inputs)
        print(f"Input: {inputs}, Output: {output}")
        print("-" * 25)
        # Devuelve el resultado para que pueda ser convertido en un 'hecho'.
        return output

    def matrix_test(self):
        """
        Ejecuta una prueba de multiplicación de matrices.
        Esta función no está conectada al meta-nivel en este ejemplo, pero podría hacerse de forma similar.
        """
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
        """
        El ciclo de ejecución principal del Nivel de Objeto.
        Ahora se conecta activamente con el Meta Nivel.
        """
        print("Hello, Carina is running now ;)")
        print(f"Current version: {self._version}")
        print(f"Carina is running in mode: {self._mode}")
        
        # Ejecuta las pruebas del nivel de objeto.
        self.matrix_test()
        output = self.neuralnetwork_test()
        
        # --- CONEXIÓN CON EL META NIVEL ---
        # 1. Crear un 'hecho' a partir del resultado de la red neuronal.
        #    El formato del hecho es descriptivo.
        fact = f"nn_output_is_{output[0]:.4f}"
        
        # 2. Añadir el nuevo hecho a la base de conocimiento del Nivel de Objeto.
        self.knowledge_base.append(fact)
        print(f"Object-level: New fact added to knowledge base: '{fact}'\n")

        # 3. Inicializar el Meta Nivel.
        metareasoner = MetaReasoner("single")
        
        # 4. Pedir al Meta Nivel que razone sobre el conocimiento del Nivel de Objeto.
        print("---> Handing over to Meta-Level for reasoning...")
        
        # Prueba 1: Pedirle que verifique el hecho que acabamos de añadir. Debería tener éxito.
        metareasoner.knowledge_test(fact, self.knowledge_base)
        
        print("-" * 15)
        
        # Prueba 2: Pedirle que verifique un hecho que no existe. Debería fallar.
        metareasoner.knowledge_test("non_existent_fact", self.knowledge_base)
        print("---> Reasoning complete.")
