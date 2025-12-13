# Classe para gerenciar motoristas da frota.
class Driver:
    def __init__(self, name, cpf, cnh, cnhCategory, isAvaliable=True, tripCount=0):
        self.name = name
        self.__cpf = cpf
        self.__cnh = cnh
        self.cnhCategory = cnhCategory
        self.isAvaliable = isAvaliable
        self.tripCount = tripCount
    
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, newCpf):
        if len(newCpf) == 11 and newCpf.isdigit():
            self.__cpf = newCpf
        else:
            raise ValueError("CPF inválido. Deve conter 11 dígitos numéricos.")
        
    @property
    def cnh(self):
        return self.__cnh
    
    @cnh.setter
    def cnh(self, newCnh):
        if len(newCnh) == 11 and newCnh.isdigit():
            self.__cnh = newCnh
        else:
            raise ValueError("CNH inválida. Deve conter 11 dígitos numéricos.")

    def newDriver(self):
        pass  # Implementar o registro de novo motorista aqui

    def viewDrivers(self):
        pass  # Implementar a visualização de motoristas aqui

    def updateDriver(self):
        pass  # Implementar a atualização de informações do motorista aqui

    def deleteDriver(self):
        pass  # Implementar a exclusão de motorista aqui

    
