import numpy as np
from abc import ABC, abstractmethod

class StoppingCondition(ABC):
    """
    Clase base para condiciones de parada.
    C(~p) en el algoritmo de Svegliato.
    """
    
    @abstractmethod
    def should_stop(self, predictions, current_quality, time_elapsed):
        """
        Determina si el algoritmo debe detenerse.
        
        Args:
            predictions: Lista de calidades predichas
            current_quality: Calidad actual de la solución
            time_elapsed: Tiempo transcurrido desde el inicio
            
        Returns:
            bool: True si debe detenerse, False en caso contrario
        """
        pass


class UtilityBasedStoppingCondition(StoppingCondition):
    """
    Condición de parada basada en utilidad esperada.
    Se detiene cuando la utilidad de continuar es menor que la de detenerse.
    """
    
    def __init__(self, time_cost=0.01, quality_weight=1.0, improvement_threshold=0.001):
        """
        Args:
            time_cost: Costo por unidad de tiempo de continuar ejecutando
            quality_weight: Peso de la calidad en la función de utilidad
            improvement_threshold: Mejora mínima esperada para continuar
        """
        self.time_cost = time_cost
        self.quality_weight = quality_weight
        self.improvement_threshold = improvement_threshold
    
    def should_stop(self, predictions, current_quality, time_elapsed):
        """
        Calcula utilidad esperada y decide si detener.
        
        Utilidad de detenerse ahora: U_stop = quality_weight * current_quality
        Utilidad de continuar: U_continue = quality_weight * E[future_quality] - time_cost * expected_time
        """
        if not predictions:
            return True
        
        # Utilidad de detenerse ahora
        u_stop = self.quality_weight * current_quality
        
        # Utilidad esperada de continuar
        # Esperamos mejorar a la primera predicción, lo cual toma Δt adicional
        expected_future_quality = predictions[0]
        expected_improvement = expected_future_quality - current_quality
        
        # Si la mejora esperada es muy pequeña, detener
        if expected_improvement < self.improvement_threshold:
            print(f"[Stopping] Expected improvement {expected_improvement:.6f} below threshold")
            return True
        
        # Calcular utilidad de continuar
        u_continue = self.quality_weight * expected_future_quality - self.time_cost
        
        # Decisión
        should_stop = u_stop >= u_continue
        
        if should_stop:
            print(f"[Stopping] U_stop ({u_stop:.4f}) >= U_continue ({u_continue:.4f})")
        
        return should_stop


class DiminishingReturnsStoppingCondition(StoppingCondition):
    """
    Se detiene cuando la tasa de mejora predicha cae por debajo de un umbral.
    """
    
    def __init__(self, min_improvement_rate=0.001):
        self.min_improvement_rate = min_improvement_rate
    
    def should_stop(self, predictions, current_quality, time_elapsed):
        """
        Detiene si la mejora marginal predicha es muy pequeña.
        """
        if not predictions:
            return True
        
        # Calcular mejora marginal predicha
        predicted_improvement = predictions[0] - current_quality
        
        if predicted_improvement < self.min_improvement_rate:
            print(f"[Stopping] Predicted improvement rate {predicted_improvement:.6f} below threshold")
            return True
        
        return False


class TimeoutStoppingCondition(StoppingCondition):
    """
    Condición de parada simple basada en tiempo máximo.
    """
    
    def __init__(self, max_time=10.0):
        self.max_time = max_time
    
    def should_stop(self, predictions, current_quality, time_elapsed):
        """
        Detiene si se excede el tiempo máximo.
        """
        if time_elapsed >= self.max_time:
            print(f"[Stopping] Timeout reached: {time_elapsed:.2f}s >= {self.max_time}s")
            return True
        return False


class QualityThresholdStoppingCondition(StoppingCondition):
    """
    Se detiene cuando se alcanza una calidad suficientemente buena.
    """
    
    def __init__(self, target_quality=0.90):
        self.target_quality = target_quality
    
    def should_stop(self, predictions, current_quality, time_elapsed):
        """
        Detiene si la calidad actual supera el umbral.
        """
        if current_quality >= self.target_quality:
            print(f"[Stopping] Target quality {self.target_quality} reached: {current_quality:.4f}")
            return True
        return False


class CompositeStoppingCondition(StoppingCondition):
    """
    Combina múltiples condiciones de parada.
    Se detiene si CUALQUIERA de las condiciones se cumple.
    """
    
    def __init__(self, conditions):
        self.conditions = conditions
    
    def should_stop(self, predictions, current_quality, time_elapsed):
        """
        Detiene si cualquier condición se cumple.
        """
        for condition in self.conditions:
            if condition.should_stop(predictions, current_quality, time_elapsed):
                return True
        return False