class Vehicle:
    
    """Classe para gerenciar veículos da frota."""
    def __init__(self, placa, marca, modelo, tipo, km, ano, consumo, status):
        self.__placa = placa
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.__km = km
        self.ano = ano
        self.consumo = consumo
        self.status = status

    # Getters
    @property
    def placa(self):
        return self.__placa
    
    @property
    def km(self):
        return self.__km
    
    @property
    def status(self):
       return self.__status

    # Setters
    @km.setter
    def km(self, valor):
        if valor < 0:
            raise ValueError("A quilometragem não pode ser negativa")
        self.__km = valor
    
    @status.setter
    def status(self, valor):
        status_validos = ['ativo', 'manutenção', 'inativo', 'descartado']
        if valor.lower() not in status_validos:
            raise ValueError(f"Status deve ser um de: {', '.join(status_validos)}")
        self.__status = valor

    def __str__(self):
        return (f"Veículo: {self.marca} {self.modelo} ({self.ano}) - "
                f"Placa: {self.__placa} - Status: {self.__status}")
       
    def __eq__(self, outro):
        if not isinstance(outro, Vehicle):
            return False
        return self.__placa == outro.__placa

    def addVeiculo(self):
        return {
            'placa': self.__placa,
            'marca': self.marca,
            'modelo': self.modelo,
            'tipo': self.tipo,
            'km': self.__km,
            'ano': self.ano,
            'consumo': self.__consumo,
            'status': self.__status
        }

    def viewVeiculo(self):
        return {
            'placa': self.__placa,
            'marca': self.marca,
            'modelo': self.modelo,
            'tipo': self.tipo,
            'quilometragem': self.__km,
            'ano_fabricacao': self.ano,
            'consumo_km_litro': self.__consumo,
            'status': self.__status,
        }

    def updateVeiculo(self, **kwargs):
        atributos_permitidos = ['km', 'status', 'consumo']
        
        for chave, valor in kwargs.items():
            if chave not in atributos_permitidos:
                raise ValueError(f"Atributo '{chave}' não pode ser atualizado")
            
            if chave == 'km':
                self.km = valor
            elif chave == 'status':
                self.status = valor
            elif chave == 'consumo':
                self.consumo = valor

    def removeVeiculo(self):
        self.__status = 'inativo'
        return f"Veículo com placa {self.__placa} foi removido da frota ativa"
    
    def calcular_consumo_total(self, litros_abastecidos):
        if litros_abastecidos < 0:
            raise ValueError("A quantidade de litros abastecidos não pode ser negativa")
        return litros_abastecidos * self.__consumo
    
    def registrar_viagem(self, km_percorridos):
        if km_percorridos < 0:
            raise ValueError("O valor da quilometragem não pode ser negativa")
        
        km_anterior = self.__km
        self.__km += km_percorridos
        
        return {
            'km_anterior': km_anterior,
            'km_adicionados': km_percorridos,
            'km_total': self.__km,
            'placa': self.__placa
        }

class Car(Vehicle):
    def __init__(self):
        pass

class Moto(Vehicle):
    def __init__(self):
        pass

class Truck(Vehicle):
    def __init__(self):
        pass
