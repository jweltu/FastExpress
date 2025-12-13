from main import *
import sqlite3  
import os

class Vehicle:   
    """Classe para gerenciar veículos da frota."""
    def __init__(self, plate, brand, model, mileage, year, kmPerLt, tripStatus=True):
        self.plate = plate
        self.brand = brand
        self.model = model
        self.mileage = mileage
        self.year = year
        self.kmPerLt = kmPerLt
        self.status = tripStatus
    
    def vehicleReport(self):
        pass  # Implementar o relatório de veículos aqui

    def updateMileage(self, newMileage):
        pass  # Implementar a atualização da quilometragem aqui

    def newVehicle(self):
        '''Recebe os dados do veículo e registra no banco de dados.'''

        plate = input("Placa do veículo: ")
        brand = input("Marca do veículo: ")
        model = input("Modelo do veículo: ")
        mileage = float(input("Quilometragem atual do veículo (km): "))
        year = int(input("Ano de fabricação do veículo: "))
        kmPerLt = float(input("Consumo médio inicial do veículo (km/l): "))
        status = True  # Novo veículo está disponível por padrão   
        # adicionar o código para salvar os dados no banco de dados
        
    def viewVehicles(self):
        pass  # Implementar a visualização de veículos aqui

    def updateVehicle(self):
        pass  # Implementar a atualização de informações do veículo aqui

    def deleteVehicle(self):    
        pass  # Implementar a exclusão de veículo aqui



class Truck(Vehicle):
    def __init__(self, plate, brand, model, mileage, year, kmPerLt, maxLoadKg, status=True):
        super().__init__(plate, brand, model, mileage, year, kmPerLt, status)
        self.maxLoadKg = maxLoadKg

class Car(Vehicle):
    def __init__(self, plate, brand, model, mileage, year, kmPerLt, passengerCapacity, status=True):
        super().__init__(plate, brand, model, mileage, year, kmPerLt, status)
        self.passengerCapacity = passengerCapacity
        
class Motorcycle(Vehicle):
    def __init__(self, plate, brand, model, mileage, year, kmPerLt, engineCapacityCc, status=True):
        super().__init__(plate, brand, model, mileage, year, kmPerLt, status)
        self.engineCapacityCc = engineCapacityCc