# Proyecto CARINA (Versión en Python)

Este proyecto es una traducción a Python del código original en Node.js. CARINA es una simulación de un sistema de razonamiento simple con una arquitectura de dos niveles.

## Arquitectura

El sistema se divide en dos capas principales:

1.  **Nivel de Objeto (`objectlevel.py`)**: Esta capa se encarga de las operaciones y cálculos fundamentales. Realiza pruebas y demostraciones de capacidades básicas como operaciones de álgebra lineal (multiplicación de matrices) y cálculos de redes neuronales (un simple `feed-forward`).
2.  **Meta Nivel (`metalevel.py`)**: Esta capa está diseñada para operar sobre el nivel de objeto. En teoría, su propósito es "razonar" sobre el conocimiento o los estados del nivel inferior. En esta implementación, su funcionalidad es básica y principalmente demostrativa.

## Estructura de Archivos

*   `main.py`: Es el punto de entrada principal de la aplicación. Su única función es instanciar y ejecutar el `Reasoner` del nivel de objeto.
*   `objectlevel.py`: Contiene la clase `Reasoner`, que orquesta las operaciones del nivel de objeto. Llama a los tests de matrices y redes neuronales y luego inicializa el `MetaReasoner`.
*   `metalevel.py`: Contiene la clase `MetaReasoner`. Su implementación actual es simple y se limita a imprimir su estado. Incluye un método `knowledge_test` que fue traducido del original pero cuya lógica era incompleta.
*   `lib/`: Es un paquete de Python que contiene las librerías de bajo nivel.
    *   `__init__.py`: Archivo vacío que convierte al directorio `lib` en un paquete de Python, permitiendo importaciones como `from lib.matrix import Matrix`.
    *   `matrix.py`: Define la clase `Matrix` con métodos para crear matrices, llenarlas con valores aleatorios, imprimirlas y realizar multiplicaciones estáticas.
    *   `neuralnetwork.py`: Define la clase `NeuralNetwork` con una implementación muy simple de una red neuronal, incluyendo una función de activación `sigmoid` y un método `feed_forward`.

## Cómo Funciona

1.  La ejecución comienza con `python main.py`.
2.  `main.py` crea una instancia de `Reasoner` desde `objectlevel.py`.
3.  El `Reasoner` ejecuta su método `run()`, que a su vez llama a:
    *   `matrix_test()`: Crea, imprime y multiplica dos matrices 2x2 con valores aleatorios.
    *   `neuralnetwork_test()`: Realiza un cálculo `feed_forward` simple.
4.  Finalmente, el `Reasoner` crea una instancia de `MetaReasoner` y ejecuta su método `run()`, que imprime un mensaje de estado.

## Cómo Ejecutar el Proyecto

Para ejecutar el código, abre una terminal en el directorio `Carina2` y ejecuta el siguiente comando:

```bash
python main.py
```
"# Project-CARINA" 
