import sqlite3
from datetime import datetime

class Maintenance:
    def __init__ (self, data, vehiclePlate, description, cost=0, maintenanceType="Preventiva"):
        self.data = data
        self.vehiclePlate = vehiclePlate
        self.maintenanceType = maintenanceType
        self.description = description
        self.cost = cost

    @staticmethod
    def _get_db_connection():
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        from modules.vehicle import Vehicle
        Vehicle.vehicleTable() 
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS maintenances
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            vehicle_plate TEXT,
            description TEXT,
            cost REAL,
            maintenanceType TEXT)''')
        conn.commit()
        return conn, cursor

    @staticmethod
    def newMaintenance():
        plate = input("Digite a placa do veículo: ")
        description = input("Descrição da manutenção: ")
        m_type = input("Tipo (Preventiva/Corretiva): ")
        try:
            cost = float(input("Custo (R$): "))
        except ValueError:
            print("Valor inválido.")
            return

        date_now = datetime.now().strftime("%Y-%m-%d")
        
        conn, cursor = Maintenance._get_db_connection()
        
        # Verifica se veículo existe
        cursor.execute("SELECT plate FROM vehicles WHERE plate = ?", (plate,))
        if not cursor.fetchone():
            print("Veículo não encontrado.")
            conn.close()
            return
            
        cursor.execute('''INSERT INTO maintenances (date, vehicle_plate, description, cost, maintenanceType)
                          VALUES (?, ?, ?, ?, ?)''', (date_now, plate, description, cost, m_type))
        conn.commit()
        conn.close()
        print("Manutenção registrada.")

    @staticmethod
    def viewMaintenances():
        conn, cursor = Maintenance._get_db_connection()
        cursor.execute("SELECT * FROM maintenances")
        recs = cursor.fetchall()
        print("\n--- Histórico de Manutenções ---")
        for r in recs:
            print(f"Data: {r[1]} | Veículo: {r[2]} | Tipo: {r[5]} | Custo: R$ {r[4]:.2f} | Desc: {r[3]}")
        conn.close()

    @staticmethod
    def updateMaintenance():
        print("Funcionalidade de atualização não implementada nesta versão.")
