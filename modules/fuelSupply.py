class Fuelsupply:
    def __init__ (self, data, veiculo, tipoCombustivel, litros, valorLitro, valorTotal):
        self.data = data
        self.veiculo = veiculo
        self.tipoCombustivel = tipoCombustivel
        self.litros = litros
        self.valorLitro = valorLitro
        self.valorTotal = valorTotal

    """Métodos para gerenciamento de abastecimento de combustível."""
    def calcularCustoPorKm(self):
        pass

    def registrarAbastecimento(self):
        pass