import sqlite3

class Driver:
    def __init__(self, name, cpf, cnh, cnhCategory, isAvaliable=True, tripCount=0):
        self.name = name
        self.__cpf = None  
        self.cpf = cpf     
        self.__cnh = None
        self.cnh = cnh
        self.cnhCategory = cnhCategory
        self.isAvaliable = isAvaliable
        self.tripCount = tripCount
    
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, newCpf):
        # Remove caracteres não numéricos se houver
        clean_cpf = "".join(filter(str.isdigit, str(newCpf)))
        if len(clean_cpf) == 11:
            self.__cpf = clean_cpf
        else:
            raise ValueError("CPF inválido. Deve conter 11 dígitos numéricos.")
        
    @property
    def cnh(self):
        return self.__cnh
    
    @cnh.setter
    def cnh(self, newCnh):
        clean_cnh = "".join(filter(str.isdigit, str(newCnh)))
        if len(clean_cnh) == 11:
            self.__cnh = clean_cnh
        else:
            raise ValueError("CNH inválida. Deve conter 11 dígitos numéricos.")

    def __str__(self):
        status = "Disponível" if self.isAvaliable else "Ocupado"
        return (f"Nome: {self.name} | CPF: {self.cpf} | CNH: {self.cnh} ({self.cnhCategory}) | "
                f"Viagens: {self.tripCount} | Status: {status}")

    @staticmethod
    def _get_db_connection():
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS drivers
            (cpf TEXT PRIMARY KEY,
            name TEXT,
            cnh TEXT,
            cnhCategory TEXT,
            isAvaliable BOOLEAN,
            tripCount INTEGER)''')
        conn.commit()
        return conn, cursor

    @staticmethod
    def newDriver():
        print("\n--- Cadastro de Motorista ---")
        name = input("Nome: ")
        cpf = input("CPF (11 dígitos): ")
        cnh = input("CNH (11 dígitos): ")
        category = input("Categoria CNH: ")
        
        try:
            # Instancia para usar a validação dos setters e __init__
            driver = Driver(name, cpf, cnh, category)
            
            conn, cursor = Driver._get_db_connection()
            try:
                cursor.execute('''INSERT INTO drivers (cpf, name, cnh, cnhCategory, isAvaliable, tripCount)
                                  VALUES (?, ?, ?, ?, ?, ?)''',
                               (driver.cpf, driver.name, driver.cnh, driver.cnhCategory, 
                                driver.isAvaliable, driver.tripCount))
                conn.commit()
                print("Motorista cadastrado com sucesso!")
            except sqlite3.IntegrityError:
                print("Erro: Já existe um motorista com este CPF.")
            finally:
                conn.close()

        except ValueError as e:
            print(f"Erro na validação: {e}")

    @staticmethod
    def viewDrivers():
        conn, cursor = Driver._get_db_connection()
        cursor.execute("SELECT * FROM drivers")
        drivers_data = cursor.fetchall()
        conn.close()

        if not drivers_data:
            print("Nenhum motorista cadastrado.")
            return

        print("\n--- Lista de Motoristas ---")
        for d in drivers_data:
            # Reconstrói o objeto para usar o __str__
            driver_obj = Driver(d[1], d[0], d[2], d[3], bool(d[4]), d[5])
            print(driver_obj)

    @staticmethod
    def updateDriver():
        cpf_input = input("Digite o CPF do motorista a atualizar: ")
        
        conn, cursor = Driver._get_db_connection()
        cursor.execute("SELECT * FROM drivers WHERE cpf = ?", (cpf_input,))
        data = cursor.fetchone()
        
        if data:
            print(f"Editando motorista: {data[1]}")
            new_name = input(f"Novo nome ({data[1]}): ") or data[1]
            new_cnh_cat = input(f"Nova Categoria CNH ({data[3]}): ") or data[3]
            
            # Atualiza apenas campos editáveis simples
            cursor.execute('''UPDATE drivers SET name = ?, cnhCategory = ? WHERE cpf = ?''',
                           (new_name, new_cnh_cat, cpf_input))
            conn.commit()
            print("Dados atualizados.")
        else:
            print("Motorista não encontrado.")
        conn.close()

    @staticmethod
    def deleteDriver():
        cpf_input = input("Digite o CPF do motorista para excluir: ")
        conn, cursor = Driver._get_db_connection()
        cursor.execute("DELETE FROM drivers WHERE cpf = ?", (cpf_input,))
        if cursor.rowcount > 0:
            print("Motorista excluído com sucesso.")
        else:
            print("Motorista não encontrado.")
        conn.commit()
        conn.close()