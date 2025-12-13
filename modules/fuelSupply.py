
# Classe para gerenciar abastecimentos de combustível nos veículos da frota.
class FuelSupply:
    def __init__(self, data, vehiclePlate, fuelType, ltsSupplied, costPerLt):
        self.data = data
        self.__vehiclePlate = vehiclePlate
        self.fuelType = fuelType
        self.ltsSupplied = ltsSupplied
        self.costPerLt = costPerLt

    def newSupply(self):
        pass  # Implementar o registro de abastecimento aqui

    def costPerMonth(self):
        pass  # Implementar o cálculo de custo mensal aqui
    
    def supplyHistory(self):
        pass  # Implementar o histórico de abastecimentos aqui 

