class MetaReasoner:
    def __init__(self, mode):
        """
        Inicializa el MetaReasoner.
        
        Args:
            mode (str): El modo de operación.
        """
        self._version = "CARINA meta-reasoner version 0.2 (Python - Conectado)"
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
        # El comentario original sobre el código JS se ha eliminado para mayor claridad,
        # ya que esta función ahora es funcional y está conectada.
        print(f"Meta-level: Checking for fact '{fact_to_check}'...")
        
        # El 'razonamiento' se reduce a esta simple comprobación.
        if fact_to_check in knowledge_base:
            print(f"Meta-level: -> SUCCESS: Fact '{fact_to_check}' found in knowledge base.")
            return True
        else:
            print(f"Meta-level: -> FAILURE: Fact '{fact_to_check}' not found in knowledge base.")
            return False

    def run(self):
        """
        Método de ejecución original. Ya no se utiliza en el flujo principal,
        pero se mantiene por si se quiere ejecutar el meta-nivel de forma aislada.
        """
        print("----> Carina's Metalevel is running now ")
        print(f"----> Current version: {self._version}")
        print(f"----> Metalevel is running in mode: {self._mode}")
