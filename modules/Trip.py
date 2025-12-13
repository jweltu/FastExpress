from datetime import datetime

class Trip:
    """Classe para gerenciar viagens de veículos."""
    
    def __init__(self, data, vehicle, origin, destination, distanceKm, driver):
        self.data = data
        self.vehicle = vehicle
        self.origin = origin
        self.destination = destination
        self.distanceKm = distanceKm
        self.driver = driver    

    def viewTrips(self):
        pass  # Implementar a visualização de viagens aqui

    def startTrip(self):
        pass  # Implementar o início de viagem aqui

    def endTrip(self):
        pass  # Implementar o encerramento de viagem aqui

    def updateTrip(self):
        pass  # Implementar a atualização de informações da viagem aqui
