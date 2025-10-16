import numpy as np
from abc import ABC, abstractmethod

class PerformancePredictor(ABC):
    """
    Clase base para predictores de performance.
    Φ(~h) en el algoritmo de Svegliato.
    """
    
    @abstractmethod
    def predict(self, history):
        """
        Predice la calidad futura basándose en el historial.
        
        Args:
            history: Lista de valores de calidad observados [q1, q2, ..., qn]
            
        Returns:
            Lista de calidades predichas para tiempos futuros
        """
        pass


class LinearRegressionPredictor(PerformancePredictor):
    """
    Predictor simple usando regresión lineal.
    Asume que la calidad mejora linealmente con el tiempo.
    """
    
    def __init__(self, future_steps=5):
        self.future_steps = future_steps
    
    def predict(self, history):
        """
        Predice valores futuros usando regresión lineal simple.
        """
        if len(history) < 2:
            # No hay suficiente historial, retorna el último valor
            return [history[-1]] * self.future_steps if history else [0.0] * self.future_steps
        
        # Crear datos para regresión
        n = len(history)
        x = np.arange(n)
        y = np.array(history)
        
        # Regresión lineal simple: y = mx + b
        m = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / (n * np.sum(x**2) - np.sum(x)**2)
        b = (np.sum(y) - m * np.sum(x)) / n
        
        # Predecir valores futuros
        future_x = np.arange(n, n + self.future_steps)
        predictions = m * future_x + b
        
        # Asegurar que las predicciones no excedan 1.0 (calidad máxima)
        predictions = np.clip(predictions, 0.0, 1.0)
        
        return predictions.tolist()


class DiminishingReturnsPredictor(PerformancePredictor):
    """
    Predictor que modela retornos decrecientes usando una función logarítmica.
    Más realista para muchos algoritmos anytime.
    """
    
    def __init__(self, future_steps=5, saturation_point=0.95):
        self.future_steps = future_steps
        self.saturation_point = saturation_point
    
    def predict(self, history):
        """
        Predice usando un modelo de retornos decrecientes.
        """
        if len(history) < 2:
            return [history[-1]] * self.future_steps if history else [0.0] * self.future_steps
        
        # Calcular la tasa de mejora reciente
        recent_improvement = history[-1] - history[0]
        
        if recent_improvement <= 0:
            # No hay mejora, predecir valores constantes
            return [history[-1]] * self.future_steps
        
        # Modelo: q(t) = saturation - (saturation - q0) * exp(-k*t)
        # Estimar k basándose en el historial
        q0 = history[0]
        qn = history[-1]
        n = len(history)
        
        # Evitar división por cero
        if abs(self.saturation_point - qn) < 1e-6:
            return [qn] * self.future_steps
        
        k = -np.log((self.saturation_point - qn) / (self.saturation_point - q0)) / n
        
        # Predecir valores futuros
        predictions = []
        for i in range(1, self.future_steps + 1):
            t = n + i
            q_pred = self.saturation_point - (self.saturation_point - q0) * np.exp(-k * t)
            predictions.append(float(np.clip(q_pred, 0.0, 1.0)))
        
        return predictions


class MovingAveragePredictor(PerformancePredictor):
    """
    Predictor simple basado en promedio móvil.
    """
    
    def __init__(self, window_size=3, future_steps=5):
        self.window_size = window_size
        self.future_steps = future_steps
    
    def predict(self, history):
        """
        Predice usando el promedio de las últimas mejoras.
        """
        if len(history) < 2:
            return [history[-1]] * self.future_steps if history else [0.0] * self.future_steps
        
        # Calcular mejoras recientes
        improvements = [history[i] - history[i-1] for i in range(1, len(history))]
        
        # Promedio de las últimas mejoras
        window = improvements[-self.window_size:] if len(improvements) >= self.window_size else improvements
        avg_improvement = np.mean(window) if window else 0.0
        
        # Predecir valores futuros
        predictions = []
        current = history[-1]
        for _ in range(self.future_steps):
            current = current + avg_improvement
            predictions.append(float(np.clip(current, 0.0, 1.0)))
        
        return predictions