from metalevel import MetaReasoner
from lib.matrix import Matrix
from lib.neuralnetwork import NeuralNetwork
from algorithms.matrix_optimization import MatrixOptimizationAnytime, IterativeRefinementAnytime
from algorithms.performance_predictor import (
    LinearRegressionPredictor, 
    DiminishingReturnsPredictor,
    MovingAveragePredictor
)
from algorithms.stopping_condition import (
    UtilityBasedStoppingCondition,
    DiminishingReturnsStoppingCondition,
    TimeoutStoppingCondition,
    QualityThresholdStoppingCondition,
    CompositeStoppingCondition
)

class Reasoner:
    def __init__(self, mode):
        """
        Inicializa el Reasoner del Nivel de Objeto.
        
        Args:
            mode (str): El modo de operación.
        """
        self._version = "CARINA version 4.0 (Python - Svegliato Integration)"
        self._mode = mode
        self.knowledge_base = []

    def neuralnetwork_test(self):
        """
        Ejecuta una prueba de la red neuronal.
        """
        print("\n" + "="*60)
        print("--- Neural Network Test ---")
        print("="*60)
        nn = NeuralNetwork(2, 2, 1)
        inputs = [1, 0]
        output = nn.feed_forward(inputs)
        print(f"Input: {inputs}, Output: {output}")
        print("="*60 + "\n")
        return output

    def matrix_test(self):
        """
        Ejecuta una prueba de multiplicación de matrices.
        """
        print("\n" + "="*60)
        print("--- Matrix Multiplication Test ---")
        print("="*60)
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
        print("="*60 + "\n")

    def demo_basic_anytime(self):
        """
        Demostración básica del algoritmo de Svegliato con un algoritmo anytime simple.
        """
        print("\n" + "#"*60)
        print("# DEMO 1: Basic Anytime Algorithm (Iterative Refinement)")
        print("#"*60 + "\n")
        
        # Crear componentes
        anytime_algo = IterativeRefinementAnytime(max_iterations=50)
        predictor = DiminishingReturnsPredictor(future_steps=5, saturation_point=0.98)
        stopping_cond = UtilityBasedStoppingCondition(
            time_cost=0.02,
            quality_weight=1.0,
            improvement_threshold=0.0005
        )
        
        # Ejecutar con meta-nivel
        metareasoner = MetaReasoner("anytime")
        solution = metareasoner.svegliato_algorithm(
            anytime_algorithm=anytime_algo,
            performance_predictor=predictor,
            stopping_condition=stopping_cond,
            delta_t=0.15
        )
        
        if solution:
            print(f"✓ Final Solution: {solution.data}")
            print(f"✓ Final Quality: {solution.quality():.6f}\n")
            
            # Agregar a base de conocimiento
            fact = f"refinement_quality_{solution.quality():.4f}"
            self.knowledge_base.append(fact)
    
    def demo_matrix_optimization(self):
        """
        Demostración con optimización de matrices.
        """
        print("\n" + "#"*60)
        print("# DEMO 2: Matrix Optimization Anytime Algorithm")
        print("#"*60 + "\n")
        
        # Crear componentes con diferentes configuraciones
        anytime_algo = MatrixOptimizationAnytime(num_matrices=4, size=8)
        predictor = LinearRegressionPredictor(future_steps=5)
        
        # Condición compuesta: detener si calidad > 0.7 O timeout > 8s
        stopping_cond = CompositeStoppingCondition([
            QualityThresholdStoppingCondition(target_quality=0.70),
            TimeoutStoppingCondition(max_time=8.0),
            DiminishingReturnsStoppingCondition(min_improvement_rate=0.0001)
        ])
        
        # Ejecutar
        metareasoner = MetaReasoner("anytime")
        solution = metareasoner.svegliato_algorithm(
            anytime_algorithm=anytime_algo,
            performance_predictor=predictor,
            stopping_condition=stopping_cond,
            delta_t=0.2
        )
        
        if solution:
            print(f"✓ Best Matrix Order: {solution.data['order']}")
            print(f"✓ Best Cost: {solution.data['cost']:.2f}")
            print(f"✓ Final Quality: {solution.quality():.6f}\n")
            
            # Agregar a base de conocimiento
            fact = f"matrix_optimization_cost_{solution.data['cost']:.2f}"
            self.knowledge_base.append(fact)

    def demo_comparison(self):
        """
        Demuestra diferentes predictores y condiciones de parada.
        """
        print("\n" + "#"*60)
        print("# DEMO 3: Comparing Different Predictors")
        print("#"*60 + "\n")
        
        predictors = [
            ("Linear Regression", LinearRegressionPredictor(future_steps=5)),
            ("Diminishing Returns", DiminishingReturnsPredictor(future_steps=5)),
            ("Moving Average", MovingAveragePredictor(window_size=3, future_steps=5))
        ]
        
        for name, predictor in predictors:
            print(f"\n>>> Testing with {name} Predictor <<<\n")
            
            anytime_algo = IterativeRefinementAnytime(max_iterations=30)
            stopping_cond = UtilityBasedStoppingCondition(
                time_cost=0.03,
                improvement_threshold=0.001
            )
            
            metareasoner = MetaReasoner("comparison")
            solution = metareasoner.svegliato_algorithm(
                anytime_algorithm=anytime_algo,
                performance_predictor=predictor,
                stopping_condition=stopping_cond,
                delta_t=0.15
            )
            
            if solution:
                print(f"  → {name}: Quality = {solution.quality():.6f}\n")

    def run(self):
        """
        El ciclo de ejecución principal del Nivel de Objeto.
        Ahora incluye demostraciones del algoritmo de Svegliato.
        """
        print("\n" + "█"*60)
        print("█" + " "*58 + "█")
        print("█" + "  CARINA - Cognitive Architecture with Meta-Reasoning  ".center(58) + "█")
        print("█" + " "*58 + "█")
        print("█"*60)
        print(f"\nCurrent version: {self._version}")
        print(f"Running in mode: {self._mode}\n")
        print("█"*60 + "\n")
        
        # Pruebas básicas originales
        self.matrix_test()
        output = self.neuralnetwork_test()
        
        # Agregar resultado a base de conocimiento
        fact = f"nn_output_is_{output[0]:.4f}"
        self.knowledge_base.append(fact)
        print(f"✓ Added to knowledge base: '{fact}'\n")
        
        # NUEVAS DEMOSTRACIONES DEL ALGORITMO DE SVEGLIATO
        print("\n" + "█"*60)
        print("█  SVEGLIATO META-LEVEL CONTROL DEMONSTRATIONS")
        print("█"*60 + "\n")
        
        # Demo 1: Algoritmo anytime básico
        self.demo_basic_anytime()
        
        # Demo 2: Optimización de matrices
        self.demo_matrix_optimization()
        
        # Demo 3: Comparación de predictores
        self.demo_comparison()
        
        # Resumen final
        print("\n" + "█"*60)
        print("█  FINAL KNOWLEDGE BASE")
        print("█"*60)
        print(f"\nTotal facts in knowledge base: {len(self.knowledge_base)}")
        for i, fact in enumerate(self.knowledge_base, 1):
            print(f"  {i}. {fact}")
        
        print("\n" + "█"*60)
        print("█  CARINA EXECUTION COMPLETED")
        print("█"*60 + "\n")