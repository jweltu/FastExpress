from datetime import datetime
import sqlite3

class Trip:
    """Classe para gerenciar viagens de veículos."""
    def __init__(self, data, vehicle_plate, origin, destination, distanceKm, driver_cpf, status="Ativa"):
        self.data = data
        self.vehicle_plate = vehicle_plate
        self.origin = origin
        self.destination = destination
        self.distanceKm = distanceKm
        self.driver_cpf = driver_cpf
        self.status = status

    @staticmethod
    def _get_db_connection():
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        from modules.vehicle import Vehicle
        from modules.driver import Driver
        Vehicle.vehicleTable()
        Driver._get_db_connection()

        cursor.execute('''CREATE TABLE IF NOT EXISTS trips
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            vehicle_plate TEXT,
            origin TEXT,
            destination TEXT,
            distanceKm REAL,
            driver_cpf TEXT,
            status TEXT)''')
        conn.commit()
        return conn, cursor

    @staticmethod
    def startTrip():
        conn, cursor = Trip._get_db_connection()
        
        # Selecionar Veículo Disponível
        print("\n--- Veículos Disponíveis ---")
        cursor.execute("SELECT plate, model FROM vehicles WHERE status = 1")
        avail_vehicles = cursor.fetchall()
        if not avail_vehicles:
            print("Nenhum veículo disponível.")
            conn.close()
            return
        
        for v in avail_vehicles:
            print(f"Placa: {v[0]} - Modelo: {v[1]}")
            
        plate = input("Digite a placa do veículo: ")
        
        # Selecionar Motorista Disponível
        print("\n--- Motoristas Disponíveis ---")
        cursor.execute("SELECT cpf, name FROM drivers WHERE isAvaliable = 1")
        avail_drivers = cursor.fetchall()
        if not avail_drivers:
            print("Nenhum motorista disponível.")
            conn.close()
            return

        for d in avail_drivers:
            print(f"CPF: {d[0]} - Nome: {d[1]}")
            
        driver_cpf = input("Digite o CPF do motorista: ")
        
        origin = input("Origem: ")
        destination = input("Destino: ")
        try:
            distance = float(input("Distância estimada (km): "))
        except ValueError:
            print("Distância inválida.")
            conn.close()
            return

        date_now = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        # Registrar Viagem
        cursor.execute('''INSERT INTO trips (date, vehicle_plate, origin, destination, distanceKm, driver_cpf, status)
                          VALUES (?, ?, ?, ?, ?, ?, ?)''',
                          (date_now, plate, origin, destination, distance, driver_cpf, "Ativa"))
        
        # Atualizar status do veículo e motorista
        cursor.execute("UPDATE vehicles SET status = 0 WHERE plate = ?", (plate,))
        cursor.execute("UPDATE drivers SET isAvaliable = 0 WHERE cpf = ?", (driver_cpf,))
        
        conn.commit()
        conn.close()
        print("Viagem iniciada com sucesso!")

    @staticmethod
    def viewTrips():
        conn, cursor = Trip._get_db_connection()
        cursor.execute("SELECT * FROM trips")
        trips = cursor.fetchall()
        
        print("\n--- Histórico de Viagens ---")
        for t in trips:
            print(f"ID: {t[0]} | Data: {t[1]} | Veículo: {t[2]} | Motorista: {t[6]} | "
                  f"{t[3]} -> {t[4]} ({t[5]}km) | Status: {t[7]}")
        conn.close()

    @staticmethod
    def endTrip():
        conn, cursor = Trip._get_db_connection()
        
        # Buscar viagens ativas
        cursor.execute("SELECT * FROM trips WHERE status = 'Ativa'")
        active_trips = cursor.fetchall()
        
        if not active_trips:
            print("Nenhuma viagem ativa no momento.")
            conn.close()
            return
            
        print("\n--- Viagens Ativas ---")
        for t in active_trips:
             print(f"ID: {t[0]} | Veículo: {t[2]} | Motorista: {t[6]} | Origem: {t[3]} -> Destino: {t[4]}")
             
        trip_id = input("Digite o ID da viagem a finalizar: ")
        
        # Recuperar dados da viagem para atualizar as entidades
        cursor.execute("SELECT vehicle_plate, driver_cpf, distanceKm FROM trips WHERE id = ? AND status = 'Ativa'", (trip_id,))
        trip_data = cursor.fetchone()
        
        if trip_data:
            plate, cpf, dist = trip_data
            
            # Finalizar viagem
            cursor.execute("UPDATE trips SET status = 'Finalizada' WHERE id = ?", (trip_id,))
            
            # Liberar veículo e somar quilometragem
            cursor.execute("UPDATE vehicles SET status = 1, mileage = mileage + ? WHERE plate = ?", (dist, plate))
            
            # Liberar motorista e somar contador de viagens
            cursor.execute("UPDATE drivers SET isAvaliable = 1, tripCount = tripCount + 1 WHERE cpf = ?", (cpf,))
            
            conn.commit()
            print("Viagem finalizada com sucesso.")
        else:
            print("ID inválido ou viagem já finalizada.")
            
        conn.close()

    @staticmethod
    def updateTrip():
        print("Funcionalidade de atualizar detalhes da viagem ainda não implementada (use Iniciar/Finalizar para fluxo normal).")