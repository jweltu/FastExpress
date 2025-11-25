from datetime import datetime

class Trip:
    """Classe para gerenciar viagens de veículos."""
    
    def __init__(self, data, placa, origem, destino, distancia, carga, valorFrete):
        self.__data = data
        self.__placa = placa
        self.__origem = origem
        self.__destino = destino
        self.__distancia = distancia
        self.__status = 'realizada'
        self.__dataRegistro = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    @property
    def data(self):
        return self.__data
    
    @property
    def placa(self):
        return self.__placa
    
    @property
    def origem(self):
        return self.__origem
    
    @property
    def destino(self):
        return self.__destino
    
    @property
    def distancia(self):
        return self.__distancia
    
    @property
    def status(self):
        return self.__status

    @distancia.setter
    def distancia(self, valor):
        if valor <= 0:
            raise ValueError("Distância deve ser maior que zero")
        self.__distancia = valor

    # Métodos Especiais
    def __str__(self):
        return (f"Viagem - Placa: {self.__placa} | Data: {self.__data} | "
                f"{self.__origem} → {self.__destino} | Distância: {self.__distancia} km | ")
    
    def __repr__(self):
        return (f"Trip(data='{self.__data}', placa='{self.__placa}', "
                f"origem='{self.__origem}', destino='{self.__destino}', "
                f"distancia={self.__distancia},")
    
    def __eq__(self, outro):
        if not isinstance(outro, Trip):
            return False
        return (self.__placa == outro.__placa and 
                self.__data == outro.__data and
                self.__origem == outro.__origem and
                self.__destino == outro.__destino)
    
    def __lt__(self, outro):
        if not isinstance(outro, Trip):
            return NotImplemented
        return self.__distancia < outro.__distancia
    
    def __hash__(self):
        return hash((self.__placa, self.__data, self.__origem, self.__destino))

    def registrarViagem(self):
        return {
            'data': self.__data,
            'placa': self.__placa,
            'origem': self.__origem,
            'destino': self.__destino,
            'distancia_km': self.__distancia,
            'status': self.__status,
            'data_registro': self.__dataRegistro
        }
    
    
    def atualizarViagem(self, **kwargs):
        atributos_permitidos = ['distancia', 'status']
        
        for chave, valor in kwargs.items():
            if chave not in atributos_permitidos:
                raise ValueError(f"Atributo '{chave}' não pode ser atualizado")
            
            if chave == 'distancia':
                self.distancia = valor
            elif chave == 'status':
                self.__status = valor
    
    def obterDetalhes(self):
        return {
            'data': self.__data,
            'placa': self.__placa,
            'origem': self.__origem,
            'destino': self.__destino,
            'distancia_km': self.__distancia,
            'status': self.__status,
            'data_registro': self.__dataRegistro
        }