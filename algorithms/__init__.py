# Paquete de algoritmos anytime y meta-razonamiento para CARINA

from .anytime_algorithm import AnytimeAlgorithm, Solution
from .performance_predictor import (
    PerformancePredictor,
    LinearRegressionPredictor,
    DiminishingReturnsPredictor,
    MovingAveragePredictor
)
from .stopping_condition import (
    StoppingCondition,
    UtilityBasedStoppingCondition,
    DiminishingReturnsStoppingCondition,
    TimeoutStoppingCondition,
    QualityThresholdStoppingCondition,
    CompositeStoppingCondition
)
from .matrix_optimization import (
    MatrixOptimizationAnytime,
    IterativeRefinementAnytime
)

__all__ = [
    'AnytimeAlgorithm',
    'Solution',
    'PerformancePredictor',
    'LinearRegressionPredictor',
    'DiminishingReturnsPredictor',
    'MovingAveragePredictor',
    'StoppingCondition',
    'UtilityBasedStoppingCondition',
    'DiminishingReturnsStoppingCondition',
    'TimeoutStoppingCondition',
    'QualityThresholdStoppingCondition',
    'CompositeStoppingCondition',
    'MatrixOptimizationAnytime',
    'IterativeRefinementAnytime'
]