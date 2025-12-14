from modules.driver import Driver
from modules.vehicle import Vehicle 
from modules.trip import Trip
from modules.maintenance import Maintenance
from modules.fuelSupply import FuelSupply
from modules.report import Report
import os

def clearScreen():
    # Limpa a tela do terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("\nPressione Enter para continuar...")

def main():
    while True:
        clearScreen()
        print(f"""
{"="*40}  
    FastExpress - Menu Principal
{"="*40}

O que posso fazer por você hoje?

[1] Gestão de Motoristas
[2] Gestão de Veículos
[3] Gestão de Viagens
[4] Gestão de Manutenções
[5] Gestão de Abastecimentos
[6] Relatórios Gerenciais
[0] Sair
""")
        try:
            cmd = int(input("Escolha uma opção: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            pause()
            continue

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
            break
        else:
            print("Opção inválida. Tente novamente.")
            pause()

def driverMenu():
    while True:
        clearScreen()
        print(f"""
{"="*30}    
    Menu - Motorista
{"="*30}
[1] Registrar Novo Motorista
[2] Visualizar Motoristas
[3] Atualizar Informações
[4] Excluir Motorista
[0] Voltar ao Menu Principal
""")
        try:
            cmd = int(input("Escolha uma opção: "))
        except ValueError:
            continue

        if cmd == 1:
            Driver.newDriver()
            pause()
        elif cmd == 2:
            Driver.viewDrivers()
            pause()
        elif cmd == 3:
            Driver.updateDriver()
            pause()
        elif cmd == 4:
            Driver.deleteDriver()
            pause()
        elif cmd == 0:
            break
        else:
            print("Opção inválida.")
            pause()

def vehicleMenu():
    while True:
        clearScreen()
        print(f"""
{"="*30}    
    Menu - Veículo
{"="*30}    
[1] Registrar Novo Veículo
[2] Visualizar Veículos
[3] Atualizar Veículo
[4] Excluir Veículo
[0] Voltar ao Menu Principal
""")
        try:
            cmd = int(input("Escolha uma opção: "))
        except ValueError:
            continue

        if cmd == 1:
            Vehicle.newVehicle() 
            pause()
        elif cmd == 2:
            Vehicle.viewVehicles()
            pause()
        elif cmd == 3:
            plate = input("Digite a placa do veículo a ser atualizado: ")
            Vehicle.updateVehicle()
            pause()
        elif cmd == 4:
            Vehicle.deleteVehicle()
            pause()
        elif cmd == 0:
            break
        else:
            print("Opção inválida.")
            pause()

def tripMenu():
    while True:
        clearScreen()
        print(f"""
{"="*30}    
    Menu - Viagem
{"="*30}
[1] Iniciar uma viagem
[2] Visualizar histórico/ativas
[3] Finalizar viagem
[0] Voltar ao Menu Principal    
""")
        try:
            cmd = int(input("Escolha uma opção: "))
        except ValueError:
            continue

        if cmd == 1:
            Trip.startTrip()
            pause()
        elif cmd == 2:
            Trip.viewTrips()
            pause()
        elif cmd == 3:
            Trip.endTrip()
            pause()
        elif cmd == 0:
            break
        else:
            print("Opção inválida.")
            pause()

def maintenanceMenu():
    while True:
        clearScreen()
        print(f"""
{"="*30}    
    Menu - Manutenção
{"="*30}
[1] Registrar Nova Manutenção
[2] Visualizar Histórico
[3] Atualizar Manutenção (Não implementado)
[0] Voltar ao Menu Principal
""")
        try:
            cmd = int(input("Escolha uma opção: "))
        except ValueError:
            continue

        if cmd == 1:
            Maintenance.newMaintenance()
            pause()
        elif cmd == 2:
            Maintenance.viewMaintenances()
            pause()
        elif cmd == 3:
            Maintenance.updateMaintenance()
            pause()
        elif cmd == 0:
            break
        else:
            print("Opção inválida.")
            pause()

def fuelSupplyMenu():
    while True:
        clearScreen()
        print(f"""
{"="*30}    
    Menu - Abastecimento
{"="*30}
[1] Registrar Novo Abastecimento
[2] Visualizar Histórico
[3] Atualizar (Não implementado)
[0] Voltar ao Menu Principal
""")
        try:
            cmd = int(input("Escolha uma opção: "))
        except ValueError:
            continue

        if cmd == 1:
            FuelSupply.newSupply()
            pause()
        elif cmd == 2:
            FuelSupply.supplyHistory()
            pause()
        elif cmd == 3:
            FuelSupply.updateSupply()
            pause()
        elif cmd == 0:
            break
        else:
            print("Opção inválida.")
            pause()

def reportMenu():
    while True:
        clearScreen()
        print(f"""
{"="*30}    
    Menu - Relatórios
{"="*30}
[1] Relatório Geral da Frota
[2] Relatório de Motoristas
[3] Relatório de Combustível
[4] Relatório de Manutenções
[5] Relatório de Viagens
[6] Visão Geral (Todos)
[0] Voltar ao Menu Principal
""")
        try:
            cmd = int(input("Escolha uma opção: "))
        except ValueError:
            continue

        if cmd == 1:
            Report.vehicleReport()
            pause()
        elif cmd == 2:
            Report.driverReport()
            pause()
        elif cmd == 3:
            Report.fuelReport()
            pause()
        elif cmd == 4:
            Report.maintenanceReport()
            pause()
        elif cmd == 5:
            Report.tripReport()
            pause()
        elif cmd == 6:
            Report.generalReport()
            pause()
        elif cmd == 0:
            break
        else:
            print("Opção inválida.")
            pause()
    
if __name__ == "__main__":
    main()