import time

class MetaReasoner:
    def __init__(self, mode):
        """
        Inicializa el MetaReasoner.
        
        Args:
            mode (str): El modo de operación.
        """
        self._version = "CARINA meta-reasoner version 0.3 (Python - Svegliato Algorithm)"
        self._mode = mode

    def knowledge_test(self, fact_to_check, knowledge_base):
        """
        Realiza la tarea de razonamiento fundamental: verificar si un hecho existe en la base de conocimiento.
        
        Args:
            fact_to_check (str): El hecho que se quiere verificar.
            knowledge_base (list): La base de conocimiento (una lista de strings) del Nivel de Objeto.
            
        Returns:
            bool: True si el hecho se encuentra, False en caso contrario.
        """
        print(f"Meta-level: Checking for fact '{fact_to_check}'...")
        
        if fact_to_check in knowledge_base:
            print(f"Meta-level: -> SUCCESS: Fact '{fact_to_check}' found in knowledge base.")
            return True
        else:
            print(f"Meta-level: -> FAILURE: Fact '{fact_to_check}' not found in knowledge base.")
            return False

    def svegliato_algorithm(self, anytime_algorithm, performance_predictor, 
                           stopping_condition, delta_t=0.1):
        """
        Implementación del Algoritmo 1 de Svegliato:
        "Meta-Level Control of Anytime Algorithms with Online Performance Prediction"
        
        Args:
            anytime_algorithm: Instancia de AnytimeAlgorithm
            performance_predictor: Instancia de PerformancePredictor (Φ)
            stopping_condition: Instancia de StoppingCondition (C)
            delta_t: Duración entre chequeos (Δt)
            
        Returns:
            Solution: La solución final
        """
        print(f"\n{'='*60}")
        print(f"META-LEVEL: Starting Svegliato Algorithm 1")
        print(f"{'='*60}")
        
        # Línea 1: t ← 0
        t = 0.0
        start_time = time.time()
        
        # Línea 2: ~h ← [ ]
        history = []
        
        # Línea 3: A.Start()
        anytime_algorithm.start()
        print(f"[t={t:.2f}s] Object-level algorithm started")
        
        # Línea 4: while A.Running() do
        iteration = 0
        while anytime_algorithm.running():
            iteration += 1
            
            # Línea 5: α ← A.CurrentSolution()
            alpha = anytime_algorithm.current_solution()
            
            if alpha is None:
                time.sleep(delta_t)
                t = time.time() - start_time
                continue
            
            # Línea 6: q ← α.Quality()
            q = alpha.quality()
            
            # Línea 7: ~h ← ~h ∥ q
            history.append(q)
            
            print(f"\n[Iteration {iteration}] t={t:.2f}s, Quality={q:.4f}")
            
            # Línea 8: ~p = Φ(~h)
            predictions = performance_predictor.predict(history)
            print(f"  Predictions: {[f'{p:.4f}' for p in predictions[:3]]}")
            
            # Línea 9: if C(~p) then
            if stopping_condition.should_stop(predictions, q, t):
                # Línea 10: A.Stop()
                anytime_algorithm.stop()
                print(f"\n{'='*60}")
                print(f"META-LEVEL: Stopping condition met at t={t:.2f}s")
                print(f"Final Quality: {q:.4f}")
                print(f"Total Iterations: {iteration}")
                print(f"Quality History: {[f'{h:.4f}' for h in history]}")
                print(f"{'='*60}\n")
                # Línea 11: return α
                return alpha
            
            # Línea 12: t ← t + Δt
            # Línea 13: Sleep(Δt)
            time.sleep(delta_t)
            t = time.time() - start_time
        
        # Línea 14: return α (si el algoritmo terminó naturalmente)
        alpha = anytime_algorithm.current_solution()
        print(f"\n{'='*60}")
        print(f"META-LEVEL: Algorithm completed naturally at t={t:.2f}s")
        print(f"Final Quality: {alpha.quality() if alpha else 'N/A':.4f}")
        print(f"{'='*60}\n")
        return alpha

    def run(self):
        """
        Método de ejecución original. Ya no se utiliza en el flujo principal,
        pero se mantiene por si se quiere ejecutar el meta-nivel de forma aislada.
        """
        print("----> Carina's Metalevel is running now ")
        print(f"----> Current version: {self._version}")
        print(f"----> Metalevel is running in mode: {self._mode}")