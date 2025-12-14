import sqlite3

class Vehicle:   
    """Classe para gerenciar veículos da frota."""
    def __init__(self, plate, brand, model, mileage, year, kmPerLt, status=True):
        self.__plate = None
        self.plate = plate  # Aciona o setter para validação
        self.brand = brand
        self.model = model
        self.mileage = mileage
        self.year = year
        self.kmPerLt = kmPerLt
        self.status = status

    @property
    def plate(self):
        return self.__plate
    
    @plate.setter
    def plate(self, newPlate):
        if len(newPlate) == 7:
            self.__plate = newPlate
        else:
            raise ValueError("Placa inválida. Deve conter 7 caracteres.")

    def __str__(self):
        status_str = 'Disponível' if self.status else 'Indisponível'
        return (f"Placa: {self.plate} | Marca: {self.brand} | Modelo: {self.model} | "
                f"Ano: {self.year} | Km: {self.mileage:.1f} | Consumo: {self.kmPerLt:.1f} km/l | "
                f"Status: {status_str}")
    
    @staticmethod
    def _get_db_connection():
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS vehicles
            (plate TEXT PRIMARY KEY,
            brand TEXT,
            model TEXT,
            mileage REAL,
            year INTEGER,
            kmPerLt REAL,
            status BOOLEAN)''')
        conn.commit()
        return conn, cursor

    @staticmethod
    def vehicleTable():
        """Garante que a tabela existe (para compatibilidade)."""
        conn, _ = Vehicle._get_db_connection()
        conn.close()

    @staticmethod
    def newVehicle():
        '''Recebe os dados do veículo e registra no banco de dados.'''
        print("\n--- Cadastro de Veículo ---")
        plate = input("Placa do veículo (7 caracteres): ")
        brand = input("Marca do veículo: ")
        model = input("Modelo do veículo: ")
        
        try:
            mileage = float(input("Quilometragem atual do veículo (km): "))
            year = int(input("Ano de fabricação do veículo: "))
            kmPerLt = float(input("Consumo médio inicial do veículo (km/l): "))
        except ValueError:
            print("Erro: Certifique-se de digitar números válidos para Km, Ano e Consumo.")
            return

        try:
            # Instancia o objeto para validar a placa (e outros dados se houver validação)
            vehicle = Vehicle(plate, brand, model, mileage, year, kmPerLt)
            
            conn, cursor = Vehicle._get_db_connection()
            try:
                cursor.execute('''INSERT INTO vehicles (plate, brand, model, mileage, year, kmPerLt, status)
                                  VALUES (?, ?, ?, ?, ?, ?, ?)''',
                                (vehicle.plate, vehicle.brand, vehicle.model, 
                                 vehicle.mileage, vehicle.year, vehicle.kmPerLt, vehicle.status))
                conn.commit()
                print("Veículo cadastrado com sucesso!")
            except sqlite3.IntegrityError:
                print(f"Erro: Já existe um veículo cadastrado com a placa {vehicle.plate}.")
            finally:
                conn.close()

        except ValueError as e:
            print(f"Erro de validação: {e}")

    @staticmethod
    def viewVehicles():
        conn, cursor = Vehicle._get_db_connection()
        
        plate = input("Digite a placa do veículo para visualizar (ou deixe em branco para todos): ")
        
        if plate:
            cursor.execute("SELECT * FROM vehicles WHERE plate = ?", (plate,))
        else:
            cursor.execute("SELECT * FROM vehicles")
            
        vehicles_data = cursor.fetchall()
        conn.close()

        if not vehicles_data:
            print("Nenhum veículo encontrado.")
            return

        print("\n--- Frota de Veículos ---")
        for v in vehicles_data:
            veh_obj = Vehicle(v[0], v[1], v[2], v[3], v[4], v[5], bool(v[6]))
            print(veh_obj)

    @staticmethod
    def updateVehicle():
        plate_input = input("Digite a placa do veículo a ser atualizado: ")
        conn, cursor = Vehicle._get_db_connection()
        cursor.execute("SELECT * FROM vehicles WHERE plate = ?", (plate_input,))
        vehicle_data = cursor.fetchone()
        
        if vehicle_data:
            print(f"Editando Veículo: {vehicle_data[1]} {vehicle_data[2]}")
            print("Deixe o campo em branco para manter o valor atual.")
            
            newBrand = input(f"Nova marca ({vehicle_data[1]}): ") or vehicle_data[1]
            newModel = input(f"Novo modelo ({vehicle_data[2]}): ") or vehicle_data[2]
            
            try:
                newMileage = input(f"Nova quilometragem ({vehicle_data[3]}): ")
                newMileage = float(newMileage) if newMileage else vehicle_data[3]
                
                newYear = input(f"Novo ano ({vehicle_data[4]}): ")
                newYear = int(newYear) if newYear else vehicle_data[4]
                
                newKmPerLt = input(f"Novo consumo médio ({vehicle_data[5]}): ")
                newKmPerLt = float(newKmPerLt) if newKmPerLt else vehicle_data[5]
                
                current_status_str = '1' if vehicle_data[6] else '0'
                newStatusInput = input(f"Novo status (1 para disponível, 0 para indisponível) (atual: {current_status_str}): ")
                if newStatusInput == '':
                    newStatus = vehicle_data[6]
                else:
                    newStatus = bool(int(newStatusInput))
            
            except ValueError:
                print("Erro: Entrada inválida para campos numéricos.")
                conn.close()
                return

            cursor.execute('''UPDATE vehicles
                              SET brand = ?, model = ?, mileage = ?, year = ?, kmPerLt = ?, status = ?
                              WHERE plate = ?''',
                              (newBrand, newModel, newMileage, newYear, newKmPerLt, newStatus, plate_input))
            conn.commit()
            print("Veículo atualizado com sucesso.")
        else:
            print("Veículo não encontrado.")
        conn.close()

    @staticmethod
    def deleteVehicle():    
        vehicle_plate = input("Digite a placa do veículo a ser excluído: ")
        conn, cursor = Vehicle._get_db_connection()
        cursor.execute("DELETE FROM vehicles WHERE plate = ?", (vehicle_plate,))
        
        if cursor.rowcount > 0:
            conn.commit()
            print("Veículo excluído com sucesso.")
        else:
            print("Veículo não encontrado.")
        conn.close()

    # Método auxiliar para atualizar quilometragem automaticamente (usado pela classe Trip)
    @staticmethod
    def updateMileage(plate, added_distance):
        conn, cursor = Vehicle._get_db_connection()
        cursor.execute("UPDATE vehicles SET mileage = mileage + ? WHERE plate = ?", (added_distance, plate))
        conn.commit()
        conn.close()


# Subclasses mantidas para extensões futuras
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