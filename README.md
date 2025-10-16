# Proyecto CARINA - Implementación del Algoritmo de Svegliato

Este proyecto implementa una arquitectura cognitiva de dos niveles con **meta-razonamiento para control de algoritmos anytime**, basado en el Algoritmo 1 de Svegliato et al.

## 📚 Referencia

**Paper**: "Meta-Level Control of Anytime Algorithms with Online Performance Prediction"  
**Autores**: Justin Svegliato et al.  
**Concepto clave**: Balance dinámico entre calidad de solución y tiempo de cómputo mediante predicción de performance online.

## 🏗️ Arquitectura

### **Nivel de Objeto (Object-Level)**
- Ejecuta algoritmos anytime que mejoran la calidad de sus soluciones con el tiempo
- Puede ser interrumpido en cualquier momento para devolver la mejor solución actual
- Implementaciones de ejemplo:
  - `IterativeRefinementAnytime`: Refinamiento iterativo (ej: cálculo de π)
  - `MatrixOptimizationAnytime`: Optimización del orden de multiplicación de matrices

### **Meta-Nivel (Meta-Level)**
- **Monitorea** la ejecución del nivel de objeto
- **Predice** la mejora futura de calidad usando modelos probabilísticos
- **Decide** cuándo interrumpir el algoritmo basándose en utilidad esperada
- Implementa el **Algoritmo 1 de Svegliato**

## 📁 Estructura del Proyecto

```
Carina2/
├── main.py                          # Punto de entrada
├── objectlevel.py                   # Razonador del nivel de objeto
├── metalevel.py                     # Meta-razonador (Algoritmo Svegliato)
├── lib/
│   ├── __init__.py
│   ├── matrix.py                    # Operaciones de matrices
│   └── neuralnetwork.py             # Red neuronal básica
└── algorithms/
    ├── __init__.py
    ├── anytime_algorithm.py         # Clase base para algoritmos anytime
    ├── performance_predictor.py     # Predictores Φ(~h)
    ├── stopping_condition.py        # Condiciones de parada C(~p)
    └── matrix_optimization.py       # Algoritmos anytime de ejemplo
```

## 🔬 Algoritmo 1 de Svegliato - Explicación

### Pseudocódigo Original
```
Input: Algoritmo anytime A, predictor Φ, condición de parada C, duración Δt
Output: Solución α

1. t ← 0
2. ~h ← [ ]                         # Historial de calidades
3. A.Start()
4. while A.Running() do
5.   α ← A.CurrentSolution()
6.   q ← α.Quality()
7.   ~h ← ~h ∥ q                    # Agregar calidad al historial
8.   ~p = Φ(~h)                     # Predecir calidades futuras
9.   if C(~p) then                  # ¿Condición de parada satisfecha?
10.    A.Stop()
11.    return α
12.   t ← t + Δt
13.   Sleep(Δt)
14. return α
```

### Componentes Clave

#### 1. **Predictor de Performance Φ(~h)**
Predice calidades futuras basándose en el historial:

- **`LinearRegressionPredictor`**: Asume mejora lineal
- **`DiminishingReturnsPredictor`**: Modela retornos decrecientes (más realista)
- **`MovingAveragePredictor`**: Basado en promedio de mejoras recientes

#### 2. **Condición de Parada C(~p)**
Decide cuándo detener el algoritmo:

- **`UtilityBasedStoppingCondition`**: 
  - Compara U_stop vs U_continue
  - U_stop = calidad_actual
  - U_continue = calidad_predicha - costo_tiempo
  - Detiene cuando U_stop ≥ U_continue

- **`DiminishingReturnsStoppingCondition`**: Detiene cuando mejora marginal < umbral

- **`QualityThresholdStoppingCondition`**: Detiene al alcanzar calidad objetivo

- **`TimeoutStoppingCondition`**: Detiene por timeout

- **`CompositeStoppingCondition`**: Combina múltiples condiciones

## 🚀 Instalación y Ejecución

### Requisitos
```bash
pip install numpy
```

### Ejecutar CARINA
```bash
python main.py
```

### Salida Esperada
El programa ejecutará tres demostraciones:

1. **Demo 1**: Refinamiento iterativo con predictor de retornos decrecientes
2. **Demo 2**: Optimización de matrices con múltiples condiciones de parada
3. **Demo 3**: Comparación de diferentes predictores de performance

## 🎯 Ejemplo de Uso Personalizado

```python
from metalevel import MetaReasoner
from algorithms.matrix_optimization import IterativeRefinementAnytime
from algorithms.performance_predictor import DiminishingReturnsPredictor
from algorithms.stopping_condition import UtilityBasedStoppingCondition

# 1. Crear algoritmo anytime
anytime_algo = IterativeRefinementAnytime(max_iterations=100)

# 2. Configurar predictor
predictor = DiminishingReturnsPredictor(
    future_steps=5,
    saturation_point=0.95
)

# 3. Configurar condición de parada
stopping_cond = UtilityBasedStoppingCondition(
    time_cost=0.01,           # Costo por segundo
    quality_weight=1.0,       # Peso de la calidad
    improvement_threshold=0.001  # Mejora mínima para continuar
)

# 4. Ejecutar con meta-nivel
metareasoner = MetaReasoner("custom")
solution = metareasoner.svegliato_algorithm(
    anytime_algorithm=anytime_algo,
    performance_predictor=predictor,
    stopping_condition=stopping_cond,
    delta_t=0.1  # Chequear cada 0.1 segundos
)

print(f"Solución final: {solution.data}")
print(f"Calidad final: {solution.quality()}")
```

## 📊 Métricas y Análisis

Durante la ejecución, el meta-nivel imprime:
- **Iteración actual** y tiempo transcurrido
- **Calidad actual** de la solución
- **Predicciones** de calidad futura
- **Decisión** de continuar o detener
- **Historial completo** de calidades

## 🔧 Crear Tu Propio Algoritmo Anytime

```python
from algorithms.anytime_algorithm import AnytimeAlgorithm, Solution
import time

class MiAlgoritmoAnytime(AnytimeAlgorithm):
    
    def __init__(self):
        super().__init__()
        self.iterations = 0
        self.max_iterations = 100
    
    def initial_solution(self):
        """Genera solución inicial rápida pero de baja calidad."""
        return Solution(
            data={'resultado': 'inicial'},
            quality_value=0.1  # Calidad baja
        )
    
    def compute_step(self):
        """Un paso de refinamiento."""
        if self.iterations >= self.max_iterations:
            return False  # Terminado
        
        self.iterations += 1
        
        # Tu lógica de mejora aquí
        # ...
        
        # Actualizar solución
        nueva_calidad = self.calcular_calidad()
        nueva_solucion = Solution(
            data={'resultado': 'mejorado'},
            quality_value=nueva_calidad
        )
        self.update_solution(nueva_solucion)
        
        time.sleep(0.05)  # Simular trabajo
        return True  # Puede continuar
```

## 📈 Ventajas del Enfoque de Svegliato

1. **Adaptativo**: Se ajusta dinámicamente según el progreso observado
2. **Eficiente**: No desperdicia tiempo computacional cuando las mejoras son marginales
3. **Fundamentado**: Basado en teoría de decisión y utilidad esperada
4. **Práctico**: Funciona con cualquier algoritmo anytime sin conocer su estructura interna

## 🎓 Conceptos Clave

- **Algoritmo Anytime**: Algoritmo que puede ser interrumpido en cualquier momento y devolver una solución cuya calidad mejora con el tiempo
- **Meta-Razonamiento**: Razonamiento sobre el propio proceso de razonamiento
- **Performance Profile**: Predicción de cómo cambiará la calidad con el tiempo
- **Utilidad Esperada**: Balance entre calidad de solución y costo computacional

## 🔮 Extensiones Futuras

- [ ] Implementar perfiles de performance paramétricos más sofisticados
- [ ] Aprendizaje online de modelos de predicción
- [ ] Manejo de múltiples algoritmos anytime en paralelo
- [ ] Integración con problemas de planificación reales
- [ ] Visualización en tiempo real del proceso de meta-razonamiento

## 📖 Referencias

- Svegliato, J., et al. "Meta-Level Control of Anytime Algorithms with Online Performance Prediction"
- Zilberstein, S. "Using Anytime Algorithms in Intelligent Systems"
- Russell, S., & Wefald, E. "Do the Right Thing: Studies in Limited Rationality"

## 👨‍💻 Autor

**Proyecto CARINA** - Arquitectura Cognitiva con Meta-Razonamiento

---

**Versión**: 4.0  
**Fecha**: Octubre 2025  
**Licencia**: MIT