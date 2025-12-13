class Maintenance:
    def __init__ (self, data, vehiclePlate, description, cost=0, maintenanceType=True):
        self.data = data
        self.vehiclePlate = vehiclePlate
        self.maintenanceType = maintenanceType
        self.description = description
        self.cost = cost

    """Registrar a manutenção do veículo."""
    def newMaintenance(self):
        pass  # Implementar o registro de manutenção aqui

    def updateMaintenance(self):
        pass  # Implementar a atualização de dados de manutenção aqui

    def viewMaintenances(self):
        pass  # Implementar a visualização de veículos em manutenção aqui

