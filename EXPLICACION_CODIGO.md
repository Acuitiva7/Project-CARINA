🧠 Proyecto CARINA

Versión 3.1 (Python - Conectado)

Carina es un sistema de razonamiento jerárquico implementado en Python.
Está compuesto por dos niveles principales: un nivel de razonamiento base (Object-Level) y un nivel meta (Meta-Level) que supervisa y valida los resultados generados por el primero.


---

📁 Estructura del Proyecto

carina/
│
├── main.py
├── objectlevel.py
├── metalevel.py
└── lib/
    ├── matrix.py
    └── neuralnetwork.py


---

⚙️ Descripción General

El sistema opera en dos niveles complementarios:

Nivel de razonamiento (Object-Level)
Ejecuta tareas lógicas o computacionales, como el procesamiento en una red neuronal.
Los resultados obtenidos se almacenan en una base de conocimiento local.

Nivel meta (Meta-Level)
Supervisa y evalúa los resultados del nivel anterior, verificando su coherencia o existencia dentro de la base de conocimiento.


El flujo de ejecución comienza en main.py, que instancia al razonador base y pone en marcha todo el proceso.


---

🚀 Ejecución del Programa

1. Archivo main.py

Punto de entrada del sistema.
Su función principal es crear una instancia del razonador (Reasoner) y ejecutar su método principal run().

from objectlevel import Reasoner

def main():
    r = Reasoner("single")
    r.run()

if __name__ == "__main__":
    main()

Flujo:

1. Se importa la clase Reasoner.


2. Se crea una instancia con el modo "single".


3. Se ejecuta la función principal run().


4. El programa comienza únicamente si el archivo es ejecutado directamente.




---

2. Archivo objectlevel.py

Define la clase Reasoner, que representa el nivel de razonamiento base.
Este módulo gestiona la lógica principal, genera resultados y los envía al nivel meta para su validación.

from metalevel import MetaReasoner
from lib.matrix import Matrix
from lib.neuralnetwork import NeuralNetwork

class Reasoner:
    def __init__(self, mode):
        self._version = "CARINA version 3.1 (Python - Conectado)"
        self._mode = mode
        self.knowledge_base = []

Componentes principales:

_version: identifica la versión actual del sistema.

_mode: define el modo de ejecución (por ejemplo, "single").

knowledge_base: lista donde se almacenan los hechos generados.


Método neuralnetwork_test()

Ejecuta una prueba de red neuronal y devuelve la salida del modelo.

def neuralnetwork_test(self):
    output = nn.feed_forward(inputs)
    return output

Método run()

Controla el flujo de trabajo del razonador.

def run(self):
    output = self.neuralnetwork_test()
    fact = f"nn_output_is_{output[0]:.4f}"
    self.knowledge_base.append(fact)
    metareasoner = MetaReasoner("single")
    metareasoner.knowledge_test(fact, self.knowledge_base)

Descripción del proceso:

1. Ejecuta el cálculo de la red neuronal.


2. Formatea el resultado en una cadena (fact).


3. Almacena el hecho en la base de conocimiento.


4. Crea una instancia del nivel meta.


5. Envía el hecho y la base para su validación.




---

3. Archivo metalevel.py

Define la clase MetaReasoner, responsable de evaluar la información producida por el razonador del nivel base.

class MetaReasoner:
    def knowledge_test(self, fact_to_check, knowledge_base):
        if fact_to_check in knowledge_base:
            print(f"Meta-level: -> ¡ÉXITO! Nota '{fact_to_check}' encontrada.")
        else:
            print(f"Meta-level: -> ¡FALLO! Nota '{fact_to_check}' no encontrada.")

Funcionamiento:

Recibe un hecho (fact_to_check) y la base de conocimiento (knowledge_base).

Utiliza el operador in para comprobar si el hecho existe dentro de la lista.

Informa el resultado de la verificación mediante salida en consola.



---

🧩 Flujo General del Sistema

1. Inicio:
main.py ejecuta la función principal y crea el razonador.


2. Razonamiento:
Reasoner procesa una tarea (por ejemplo, una red neuronal) y genera un hecho.


3. Almacenamiento:
El hecho se guarda en la base de conocimiento.


4. Supervisión:
MetaReasoner recibe la base y valida si el hecho generado está correctamente registrado.


5. Salida:
El resultado se muestra en consola (éxito o fallo).




---

🧱 Dependencias

Python 3.9+

Módulos internos:

lib.matrix — Operaciones matriciales.

lib.neuralnetwork — Implementación del modelo de red neuronal.




---
