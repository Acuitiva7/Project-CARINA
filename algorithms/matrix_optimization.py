import random
import numpy as np
import time
from algorithms.anytime_algorithm import AnytimeAlgorithm, Solution

class MatrixOptimizationAnytime(AnytimeAlgorithm):
    """
    Algoritmo anytime de ejemplo: optimización de multiplicación de matrices.
    
    Simula un algoritmo que intenta encontrar el mejor orden de multiplicación
    de matrices para minimizar operaciones. La calidad mejora con el tiempo
    a medida que explora más posibilidades.
    """
    
    def __init__(self, num_matrices=5, size=10):
        super().__init__()
        self.num_matrices = num_matrices
        self.size = size
        self.matrices = []
        self.best_order = None
        self.best_cost = float('inf')
        self.iterations = 0
        self.max_iterations = 100
        
    def initial_solution(self):
        """
        Genera matrices aleatorias y una solución inicial simple.
        """
        # Generar matrices aleatorias
        self.matrices = [np.random.rand(self.size, self.size) 
                        for _ in range(self.num_matrices)]
        
        # Orden inicial simple (secuencial)
        self.best_order = list(range(self.num_matrices))
        self.best_cost = self._evaluate_order(self.best_order)
        
        # Calidad inicial baja (normalizada entre 0 y 1)
        initial_quality = 1.0 / (1.0 + self.best_cost / 1000.0)
        
        return Solution(
            data={'order': self.best_order.copy(), 'cost': self.best_cost},
            quality_value=initial_quality
        )
    
    def _evaluate_order(self, order):
        """
        Evalúa el costo de un orden de multiplicación dado.
        Simula operaciones de punto flotante necesarias.
        """
        # Simulación simple: el costo depende de cuán "desordenado" está
        cost = 0
        for i in range(len(order) - 1):
            cost += abs(order[i] - order[i+1]) * self.size * self.size
        return cost + random.uniform(0, 100)  # Añade ruido
    
    def compute_step(self):
        """
        Realiza un paso de optimización: prueba un nuevo orden aleatorio.
        """
        if self.iterations >= self.max_iterations:
            return False  # Terminado
        
        self.iterations += 1
        
        # Genera un nuevo orden candidato (perturbación del mejor)
        candidate_order = self.best_order.copy()
        
        # Estrategia: swap aleatorio con probabilidad decreciente de cambios grandes
        swap_magnitude = max(1, int((self.max_iterations - self.iterations) / 20))
        i = random.randint(0, len(candidate_order) - 1)
        j = random.randint(max(0, i - swap_magnitude), 
                          min(len(candidate_order) - 1, i + swap_magnitude))
        candidate_order[i], candidate_order[j] = candidate_order[j], candidate_order[i]
        
        # Evalúa el candidato
        candidate_cost = self._evaluate_order(candidate_order)
        
        # Si es mejor, actualiza
        if candidate_cost < self.best_cost:
            self.best_order = candidate_order
            self.best_cost = candidate_cost
            print(f"    [Object-level] Improved! Cost: {self.best_cost:.2f}")
        
        # Calcula calidad mejorada (se acerca a 1 a medida que el costo disminuye)
        quality = 1.0 / (1.0 + self.best_cost / 1000.0)
        
        # Actualiza la solución
        new_solution = Solution(
            data={'order': self.best_order.copy(), 'cost': self.best_cost},
            quality_value=quality
        )
        self.update_solution(new_solution)
        
        # Simula trabajo computacional
        time.sleep(0.05)
        
        return True  # Puede continuar


class IterativeRefinementAnytime(AnytimeAlgorithm):
    """
    Algoritmo anytime más simple: refinamiento iterativo de una aproximación.
    Ejemplo: cálculo iterativo de π o una integral.
    """
    
    def __init__(self, target_value=np.pi, max_iterations=50):
        super().__init__()
        self.target_value = target_value
        self.max_iterations = max_iterations
        self.current_estimate = 3.0  # Aproximación inicial tosca
        self.iterations = 0
    
    def initial_solution(self):
        """
        Solución inicial: aproximación tosca.
        """
        error = abs(self.current_estimate - self.target_value)
        quality = 1.0 / (1.0 + error)
        
        return Solution(
            data={'estimate': self.current_estimate, 'error': error},
            quality_value=quality
        )
    
    def compute_step(self):
        """
        Refina la estimación usando más términos de una serie.
        """
        if self.iterations >= self.max_iterations:
            return False
        
        self.iterations += 1
        
        # Simula refinamiento: aproximación de π usando serie de Leibniz
        # π/4 = 1 - 1/3 + 1/5 - 1/7 + ...
        n_terms = (self.iterations + 1) * 10
        pi_approx = sum((-1)**n / (2*n + 1) for n in range(n_terms)) * 4
        
        self.current_estimate = pi_approx
        error = abs(self.current_estimate - self.target_value)
        quality = 1.0 / (1.0 + error * 10)  # Escala el error
        
        if self.iterations % 5 == 0:
            print(f"    [Object-level] Iteration {self.iterations}: estimate={pi_approx:.6f}, error={error:.6f}")
        
        # Actualiza solución
        new_solution = Solution(
            data={'estimate': self.current_estimate, 'error': error},
            quality_value=quality
        )
        self.update_solution(new_solution)
        
        # Simula computación
        time.sleep(0.1)
        
        return True