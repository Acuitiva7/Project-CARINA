from objectlevel import Reasoner

def main():
    """
    Punto de entrada principal de CARINA.
    
    Ahora incluye demostraciones del Algoritmo 1 de Svegliato para
    meta-level control de algoritmos anytime con predicción de performance online.
    """
    print("\n")
    print("╔════════════════════════════════════════════════════════════╗")
    print("║                                                            ║")
    print("║              Welcome to CARINA v4.0                        ║")
    print("║     Cognitive Architecture for Reasoning with Anytime      ║")
    print("║                                                            ║")
    print("║  Implementation of Svegliato's Algorithm 1:                ║")
    print("║  Meta-Level Control with Online Performance Prediction     ║")
    print("║                                                            ║")
    print("╚════════════════════════════════════════════════════════════╝")
    print("\n")
    
    # Crear e iniciar el razonador
    r = Reasoner("svegliato_demo")
    r.run()
    
    print("\n")
    print("╔════════════════════════════════════════════════════════════╗")
    print("║                                                            ║")
    print("║              CARINA Shutdown Complete                      ║")
    print("║                                                            ║")
    print("╚════════════════════════════════════════════════════════════╝")
    print("\n")

if __name__ == "__main__":
    main()