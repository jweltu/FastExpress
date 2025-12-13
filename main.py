from modules.driver import Driver
from modules.vehicle import Vehicle 
from modules.trip import Trip
from modules.maintenance import Maintenance
from modules.fuelSupply import FuelSupply
from modules.report import Report
import os

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("\nPressione Enter para continuar...")


"""Módulo principal do sistema FastExpress."""
def main():
    clearScreen()
    cmd = int(input(f"""
{"="*30}  
    FastExpress - Menu
{"="*30}

O que posso fazer por você hoje?

[1] Motorista
[2] Veículo
[3] Viagem
[4] Manutenção
[5] Abastecimento
[6] Relatórios
[0] Sair
Escolha uma opção: """))
    if cmd == 1:
        driverMenu()
    elif cmd == 2:
        vehicleMenu() 
    elif cmd == 3:
        tripMenu()
    elif cmd == 4:
        maintenanceMenu()
    elif cmd == 5:
        fuelSupplyMenu()
    elif cmd == 6:
        reportMenu()
    elif cmd == 0:
        clearScreen()
        print("\nAté logo!\n\n© FastExpress 2026\n")
    else:
        print("Opção inválida. Tente novamente.")

def driverMenu():
    clearScreen()
    cmd = int(input(f"""
{"="*30}    
    Menu - Motorista
{"="*30}
O que você deseja fazer?
[1] Registrar Novo Motorista
[2] Visualizar Motoristas
[3] Atualizar Informações do Motorista
[4] Excluir Motorista
[0] Voltar ao Menu Principal
Escolha uma opção: """))
    if cmd == 1:
        Driver.newDriver()
    elif cmd == 2:
        Driver.viewDrivers()
    elif cmd == 3:
        Driver.updateDriver()
    elif cmd == 4:
        Driver.deleteDriver()
    elif cmd == 0:
        main()
    else:
        print("Opção inválida. Tente novamente.")

def vehicleMenu():
    clearScreen()
    cmd = int(input(f"""
{"="*30}    
    Menu - Veículo
{"="*30}    
O que você deseja fazer?

[1] Relatório de Veículos
[2] Registrar Novo Veículo
[4] Visualizar Veículos
[5] Atualizar Informações do Veículo
[6] Excluir Veículo
[0] Voltar ao Menu Principal

Escolha uma opção: """))
    if cmd == 1:
        Vehicle.vehicleReport()
    elif cmd == 2:
        Vehicle.newVehicle()
    elif cmd == 4:
        Vehicle.viewVehicles()
    elif cmd == 5:
        Vehicle.updateVehicle()
    elif cmd == 6:
        Vehicle.deleteVehicle()
    elif cmd == 0:
        main()
    else:
        print("Opção inválida. Tente novamente.")

def tripMenu():
    clearScreen()
    cmd = int(input(f"""
{"="*30}    
    Menu - Viagem
{"="*30}
O que você deseja fazer?

[1] Iniciar uma viagem
[2] Visualizar viagens ativas e encerradas
[3] Atualizar Informações da Viagem
[4] finalizar viagem
[0] Voltar ao Menu Principal    
Escolha uma opção: """))
    if cmd == 1:
        Trip.startTrip()
    elif cmd == 2:
        Trip.viewTrips()
    elif cmd == 3:
        Trip.updateTrip()
    elif cmd == 4:
        Trip.endTrip()
    elif cmd == 0:
        main()
    else:
        print("Opção inválida. Tente novamente.")

def maintenanceMenu():
    clearScreen()
    cmd = int(input(f"""
{"="*30}    
    Menu - Manutenção
{"="*30}
O que você deseja fazer?

[1] Registrar Nova Manutenção
[2] Visualizar veículos em manutenção
[3] Atualizar Informações da Manutenção
[0] Voltar ao Menu Principal
Escolha uma opção: """))
    if cmd == 1:
        Maintenance.newMaintenance()
    elif cmd == 2:
        Maintenance.viewMaintenances()
    elif cmd == 3:
        Maintenance.updateMaintenance()
    elif cmd == 0:
        main()
    else:
        print("Opção inválida. Tente novamente.")

def fuelSupplyMenu():
    clearScreen()
    cmd = int(input(f"""
{"="*30}    
    Menu - Abastecimento
{"="*30}
O que você deseja fazer?

[1] Registrar Novo abastecimento
[2] Visualizar histórico de abastecimentos
[3] Atualizar Informações do abastecimento
[0] Voltar ao menu principal
Escolha uma opção: """))
    if cmd == 1:
        FuelSupply.newSupply()
    elif cmd == 2:
        FuelSupply.supplyHistory()
    elif cmd == 3:
        FuelSupply.updateSupply()
    elif cmd == 0:
        main()
    else:
        print("Opção inválida. Tente novamente.")

def reportMenu():
    clearScreen()
    cmd = int(input(f"""
{"="*30}    
    Menu - Relatórios
{"="*30}
O que você deseja fazer?

[1] Relatório de Veículos
[2] Relatório de Motoristas
[3] Relatório de uso de combustível
[4] Relatório de Manutenções
[5] Relatório de Viagens
[6] Relatório Geral
[0] Voltar ao Menu Principal
Escolha uma opção: """))
    if cmd == 1:
        Report.vehicleReport()
    elif cmd == 2:
        Report.driverReport()
    elif cmd == 3:
        Report.fuelReport()
    elif cmd == 4:
        Report.maintenanceReport()
    elif cmd == 5:
        Report.tripReport()
    elif cmd == 6:
        Report.generalReport()
    elif cmd == 0:
        main()
    else:
        print("Opção inválida. Tente novamente.")
    
if __name__ == "__main__":
    main()