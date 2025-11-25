from datetime import datetime

class FuelSupply:
    """Classe para gerenciar abastecimento de combustível."""
    
    def __init__(self, data, placa, tipoCombustivel, litros, valorLitro, consumoVeiculo):
        self.__data = data
        self.__placa = placa
        self.__tipoCombustivel = tipoCombustivel
        self.__litros = litros
        self.__valorLitro = valorLitro
        self.__valorTotal = litros * valorLitro
        self.__consumoVeiculo = consumoVeiculo

    @property
    def data(self):
        return self.__data
    
    @property
    def placa(self):
        return self.__placa
    
    @property
    def tipoCombustivel(self):
        return self.__tipoCombustivel
    
    @property
    def litros(self):
        return self.__litros
    
    @property
    def valorLitro(self):
        return self.__valorLitro
    
    @property
    def valorTotal(self):
        return self.__valorTotal
    
    @property
    def consumoVeiculo(self):
        return self.__consumoVeiculo

    @litros.setter
    def litros(self, valor):
        if valor <= 0:
            raise ValueError("Quantidade de litros deve ser maior que zero")
        self.__litros = valor
        self.__valorTotal = valor * self.__valorLitro
    
    @valorLitro.setter
    def valorLitro(self, valor):
        if valor < 0:
            raise ValueError("Valor por litro não pode ser negativo")
        self.__valorLitro = valor
        self.__valorTotal = self.__litros * valor

    def __str__(self):
        return (f"Abastecimento - Placa: {self.__placa} | Data: {self.__data} | "
                f"Tipo: {self.__tipoCombustivel} | Litros: {self.__litros:.2f} | "
                f"Valor: R$ {self.__valorTotal:.2f}")
    
    def __repr__(self):
        return (f"FuelSupply(data='{self.__data}', placa='{self.__placa}', "
                f"tipoCombustivel='{self.__tipoCombustivel}', litros={self.__litros}, "
                f"valorLitro={self.__valorLitro}, consumoVeiculo={self.__consumoVeiculo})")
    
    def __eq__(self, outro):
        if not isinstance(outro, FuelSupply):
            return False
        return self.__placa == outro.__placa and self.__data == outro.__data
    
    def __lt__(self, outro):
        if not isinstance(outro, FuelSupply):
            return NotImplemented
        return self.__valorTotal < outro.__valorTotal

    def calcularCustoPorKm(self):
        if self.__consumoVeiculo <= 0:
            raise ValueError("Consumo do veículo deve ser maior que zero")
        autonomia = self.__litros * self.__consumoVeiculo
        if autonomia == 0:
            return 0
        return self.__valorTotal / autonomia

    def calcularAutonomia(self):
        return self.__litros * self.__consumoVeiculo

    def registrarAbastecimento(self):
        return {
            'data': self.__data,
            'placa': self.__placa,
            'tipo_combustivel': self.__tipoCombustivel,
            'litros': self.__litros,
            'valor_litro': self.__valorLitro,
            'valor_total': self.__valorTotal,
            'autonomia_km': self.calcularAutonomia(),
            'custo_por_km': self.calcularCustoPorKm()
        }
    
    def atualizarValorCombustivel(self, novoValor):
        self.valorLitro = novoValor
        return {
            'novo_valor_litro': self.__valorLitro,
            'novo_valor_total': self.__valorTotal,
            'novo_custo_por_km': self.calcularCustoPorKm()
        }