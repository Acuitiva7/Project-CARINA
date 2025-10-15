# Explicación del Código del Proyecto "Carina"

¡Hola! Aquí tienes la explicación detallada del proyecto, pensada para principiantes. Vamos a ver el código como si fueran las instrucciones de un recetario.

Nuestros personajes son:
*   **El Cocinero** (el código en `objectlevel.py`)
*   **El Catador** (el código en `metalevel.py`)

---

### **Archivo 1: `main.py` (El Botón de "Empezar")**

Este es el archivo más simple. Su único trabajo es iniciar todo el proceso.

```python
# 1. "Para empezar, necesito la receta del Cocinero"
#    Importamos la clase "Reasoner" (nuestro Cocinero) desde el archivo objectlevel.py
from objectlevel import Reasoner

# 2. "Esta es la tarea principal que vamos a hacer"
def main():
    # 3. "Contratamos a un Cocinero para que trabaje"
    #    Creamos una copia real y funcional del Cocinero. La guardamos en la variable 'r'.
    r = Reasoner("single")

    # 4. "Cocinero, ¡ponte a trabajar!"
    #    Llamamos a su lista de tareas principal, que se llama 'run'.
    r.run()

# 5. "Cuando le de al 'Play' a este archivo, empieza con la tarea 'main'"
#    Esta línea es un estándar en Python para indicar dónde comienza el programa.
if __name__ == "__main__":
    main()
```

**En resumen:** `main.py` es como el dedo que pulsa el botón de "ON". Contrata a un Cocinero y le dice que empiece a cocinar.

---

### **Archivo 2: `objectlevel.py` (La Receta del Cocinero)**

Este archivo define todo lo que el Cocinero sabe y puede hacer.

```python
# El Cocinero necesita saber quién es el Catador y dónde están sus herramientas
from metalevel import MetaReasoner
from lib.matrix import Matrix
from lib.neuralnetwork import NeuralNetwork

# Aquí definimos el plano de lo que es un "Cocinero"
class Reasoner:
    # Esta es la preparación inicial del Cocinero. Se ejecuta en cuanto lo contratamos.
    def __init__(self, mode):
        # El Cocinero se pone una placa con su nombre.
        self._version = "CARINA version 3.1 (Python - Conectado)"
        self._mode = mode
        
        # IMPORTANTE: El Cocinero prepara su "Tablón de Anuncios".
        # `[]` significa una lista vacía, lista para colgar notas.
        self.knowledge_base = []

    # Esta es la receta para el "pastel de red neuronal".
    def neuralnetwork_test(self):
        # ... (pasos de la receta)
        output = nn.feed_forward(inputs)
        
        # IMPORTANTE: "return" significa "entregar". El Cocinero ahora entrega
        # el resultado (el pastel) a quien se lo pidió.
        return output

    # ... (aquí está la receta de la matriz, que no usamos para la conexión)

    # Esta es la lista de tareas principal del Cocinero.
    def run(self):
        # El Cocinero prepara el pastel y guarda el resultado en la variable 'output'.
        output = self.neuralnetwork_test()
        
        # --- AQUÍ EMPIEZA LA CONEXIÓN ---

        # 1. El Cocinero escribe la nota.
        #    La 'f' antes de las comillas permite meter el resultado (`output`) dentro del texto.
        fact = f"nn_output_is_{output[0]:.4f}"
        
        # 2. El Cocinero cuelga la nota en su Tablón de Anuncios.
        #    `.append()` es la acción de "añadir al final de la lista".
        self.knowledge_base.append(fact)
        
        # 3. El Cocinero contrata a un Catador.
        metareasoner = MetaReasoner("single")
        
        # 4. El Cocinero llama al Catador y le da dos cosas:
        #    - La nota que debe buscar (`fact`).
        #    - El tablón donde debe buscar (`self.knowledge_base`).
        metareasoner.knowledge_test(fact, self.knowledge_base)
```

**En resumen:** El Cocinero hace un cálculo, escribe el resultado en una nota, la cuelga en un tablón y le pide al Catador que la revise.

---

### **Archivo 3: `metalevel.py` (La Receta del Catador)**

Este archivo define lo que el Catador sabe hacer.

```python
# Aquí definimos el plano de lo que es un "Catador"
class MetaReasoner:
    # ... (la preparación del Catador)

    # Esta es la receta de "cómo catar".
    # Recibe la "nota a buscar" y el "tablón de anuncios" del Cocinero.
    def knowledge_test(self, fact_to_check, knowledge_base):
        
        # LA MAGIA OCURRE AQUÍ
        # `in` es una palabra clave de Python para comprobar si un elemento está DENTRO de una lista.
        # Esta línea se traduce como: "¿Está la 'nota a buscar' DENTRO del 'tablón de anuncios'?"
        # Python nos contesta con `True` (Verdadero) o `False` (Falso).
        if fact_to_check in knowledge_base:
            
            # Si la respuesta fue True, anuncia que la encontró.
            print(f"Meta-level: -> ¡ÉXITO! Nota '{fact_to_check}' encontrada.")
        
        else:
            # Si la respuesta fue False, anuncia que no la encontró.
            print(f"Meta-level: -> ¡FALLO! Nota '{fact_to_check}' no encontrada.")
```

**En resumen:** El Catador recibe una nota y un tablón. Usa la palabra mágica `in` de Python para ver si la nota está en el tablón y anuncia el resultado.
