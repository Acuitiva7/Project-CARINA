class MetaReasoner:
    def __init__(self, mode):
        self._version = "CARINA meta-reasoner version 0.1 (Python)"
        self._mode = mode

    def knowledge_test(self, p, l):
        # Nota: La lógica original en JS era incompleta y no funcional.
        # El bucle 'for (var i in objeto)' no se pudo traducir porque la variable 'objeto' no estaba definida.
        # Este era el código original problemático en JavaScript:
        #
        # for (var i in objeto) {
        #     if (objeto.hasOwnProperty(i)) {
        #         resultado += `${nombreObjeto}.${i} = ${objeto[i]}\n`;
        #     }
        # }
        #
        # La lógica del bucle se ha simplificado en la traducción.
        result = ""
        i = 0
        while i < 5:
            i += 1
            result += str(i)
        
        print(result)

        if p in l:
            return "Yes"
        else:
            return "No"

    def run(self):
        print("----> Carina's Metalevel is running now ")
        print(f"----> Current version: {self._version}")
        print(f"----> Metalevel is running in mode: {self._mode}")
