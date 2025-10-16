import time
import threading
from abc import ABC, abstractmethod

class AnytimeAlgorithm(ABC):
    """
    Clase base abstracta para algoritmos anytime.
    Un algoritmo anytime puede ser interrumpido en cualquier momento
    y devolver una solución con calidad que mejora con el tiempo.
    """
    
    def __init__(self):
        self._running = False
        self._current_solution = None
        self._thread = None
        self._lock = threading.Lock()
        
    @abstractmethod
    def compute_step(self):
        """
        Ejecuta un paso de computación del algoritmo.
        Debe actualizar self._current_solution.
        Retorna True si puede continuar, False si terminó.
        """
        pass
    
    @abstractmethod
    def initial_solution(self):
        """
        Genera una solución inicial (puede ser de baja calidad).
        """
        pass
    
    def start(self):
        """Inicia la ejecución del algoritmo anytime en un thread separado."""
        if self._running:
            return
        
        self._running = True
        self._current_solution = self.initial_solution()
        self._thread = threading.Thread(target=self._run_loop, daemon=True)
        self._thread.start()
        print(f"[Anytime] Algorithm started")
    
    def _run_loop(self):
        """Loop interno que ejecuta pasos del algoritmo."""
        while self._running:
            can_continue = self.compute_step()
            if not can_continue:
                self._running = False
                print(f"[Anytime] Algorithm completed naturally")
                break
    
    def stop(self):
        """Detiene la ejecución del algoritmo."""
        if self._running:
            self._running = False
            if self._thread:
                self._thread.join(timeout=1.0)
            print(f"[Anytime] Algorithm stopped by meta-level")
    
    def running(self):
        """Retorna True si el algoritmo está ejecutándose."""
        return self._running
    
    def current_solution(self):
        """Retorna la solución actual."""
        with self._lock:
            return self._current_solution
    
    def update_solution(self, new_solution):
        """Actualiza la solución actual de forma thread-safe."""
        with self._lock:
            self._current_solution = new_solution


class Solution:
    """
    Representa una solución con su calidad asociada.
    """
    
    def __init__(self, data, quality_value):
        self.data = data
        self._quality = quality_value
    
    def quality(self):
        """Retorna la calidad de la solución."""
        return self._quality
    
    def __repr__(self):
        return f"Solution(data={self.data}, quality={self._quality:.4f})"