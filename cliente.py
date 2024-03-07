class cliente:
    def __init__(self, n, fone):
        self._nome = n
        self._telefone = fone
        
# Método Get

    def get_nome(self):
        return self._nome

# Método Set

    def set_nome(self, nome):
        self._nome = nome