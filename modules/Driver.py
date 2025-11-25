class Driver:
    """Classe para gerenciar motoristas da frota."""
    
    def __init__(self, name, cpf, expAnos, cnh, disponibilidade, qtdViagens, categoria):
        self.__name = name
        self.__cpf = cpf
        self.expAnos = expAnos
        self.__cnh = cnh
        self.disponibilidade = disponibilidade
        self.qtdViagens = qtdViagens
        self.categoria = categoria

    # Propriedades (Getters)
    @property
    def name(self):
        return self.__name
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def cnh(self):
        return self.__cnh
    
    # Setters
    @name.setter
    def name(self, valor):
        """Define o nome do motorista."""
        if not valor or not isinstance(valor, str):
            raise ValueError("Nome deve ser uma string não vazia")
        self.__name = valor

    def __str__(self):
        status = "Disponível" if self.disponibilidade else "Indisponível"
        return (f"Motorista: {self.__name} | CPF: {self._mascarar_cpf()} | "
                f"CNH: {self.__cnh} ({self.categoria}) | Status: {status}")
    
    def __repr__(self):
        return (f"Driver(name='{self.__name}', cpf='{self.__cpf}', "
                f"expAnos={self.expAnos}, cnh='{self.__cnh}', "
                f"disponibilidade={self.disponibilidade}, qtdViagens={self.qtdViagens}, "
                f"categoria='{self.categoria}')")
    
    def __eq__(self, outro):
        if not isinstance(outro, Driver):
            return False
        return self.__cpf == outro.__cpf

    def addDriver(self):
        return {
            'nome': self.__name,
            'cpf': self.__cpf,
            'experiencia_anos': self.expAnos,
            'cnh': self.__cnh,
            'categoria_cnh': self.categoria,
            'disponibilidade': self.disponibilidade,
            'viagens_realizadas': self.qtdViagens
        }

    def removeDriver(self):
        self.disponibilidade = False
        return f"Motorista {self.__name} (CPF: {self._mascarar_cpf()}) foi removido da frota"

    def updateDriver(self, **kwargs):
        atributos_permitidos = ['name', 'disponibilidade', 'expAnos', 'qtdViagens']
        
        for chave, valor in kwargs.items():
            if chave not in atributos_permitidos:
                raise ValueError(f"Atributo '{chave}' não pode ser atualizado")
            
            if chave == 'name':
                self.name = valor
            elif chave == 'disponibilidade':
                self.disponibilidade = valor
            elif chave == 'expAnos':
                self.expAnos = valor
            elif chave == 'qtdViagens':
                self.qtdViagens = valor

    def viewDriver(self):
        return {
            'nome': self.__name,
            'cpf': self._mascarar_cpf(),
            'experiencia_anos': self.expAnos,
            'cnh': self.__cnh,
            'categoria_cnh': self.categoria,
            'disponibilidade': self.disponibilidade,
            'viagens_realizadas': self.qtdViagens,
            'status': 'Disponível' if self.disponibilidade else 'Indisponível'
        }

    def _mascarar_cpf(self):
        if len(self.__cpf) >= 11:
            return f"{self.__cpf[:3]}.{self.__cpf[3:6]}.{self.__cpf[6:9]}-**"
        return "***.***.***-**"
    
    def incrementar_viagens(self):
        self.__qtdViagens += 1
        return self.__qtdViagens