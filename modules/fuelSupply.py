import sqlite3
from datetime import datetime

class FuelSupply:
    def __init__(self, data, vehiclePlate, fuelType, ltsSupplied, costPerLt):
        self.data = data
        self.vehiclePlate = vehiclePlate
        self.fuelType = fuelType
        self.ltsSupplied = ltsSupplied
        self.costPerLt = costPerLt
        
    @property
    def total_cost(self):
        return self.ltsSupplied * self.costPerLt

    @staticmethod
    def _get_db_connection():
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS fuel_supply
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            vehicle_plate TEXT,
            fuelType TEXT,
            ltsSupplied REAL,
            costPerLt REAL,
            totalCost REAL)''')
        conn.commit()
        return conn, cursor

    @staticmethod
    def newSupply():
        plate = input("Placa do veículo: ")
        fuel_type = input("Tipo de Combustível (Gasolina/Diesel/Etanol): ")
        try:
            liters = float(input("Litros abastecidos: "))
            cost_lt = float(input("Preço por litro: "))
        except ValueError:
            print("Valores numéricos inválidos.")
            return

        supply = FuelSupply(datetime.now(), plate, fuel_type, liters, cost_lt)
        
        conn, cursor = FuelSupply._get_db_connection()
        cursor.execute("SELECT plate FROM vehicles WHERE plate = ?", (plate,))
        if not cursor.fetchone():
            print("Veículo não encontrado. Cadastre o veículo antes de abastecer.")
            conn.close()
            return

        cursor.execute('''INSERT INTO fuel_supply (date, vehicle_plate, fuelType, ltsSupplied, costPerLt, totalCost)
                          VALUES (?, ?, ?, ?, ?, ?)''',
                          (datetime.now().strftime("%Y-%m-%d"), plate, fuel_type, liters, cost_lt, supply.total_cost))
        conn.commit()
        conn.close()
        print(f"Abastecimento registrado. Custo Total: R$ {supply.total_cost:.2f}")

    @staticmethod
    def supplyHistory():
        conn, cursor = FuelSupply._get_db_connection()
        cursor.execute("SELECT * FROM fuel_supply")
        rows = cursor.fetchall()
        print("\n--- Histórico de Abastecimentos ---")
        for r in rows:
            print(f"Data: {r[1]} | Veículo: {r[2]} | {r[3]} | {r[4]}L à R${r[5]} o litro | Total: R${r[6]:.2f}")
        conn.close()
        
    @staticmethod
    def updateSupply():
         print("Atualização de abastecimento não implementada.")