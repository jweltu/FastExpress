import sqlite3

class Report:
    """Classe para gerar relatórios de custos e desempenho dos veículos."""
    
    @staticmethod
    def _get_conn():
        return sqlite3.connect('data.db')

    @staticmethod
    def vehicleReport():
        conn = Report._get_conn()
        cursor = conn.cursor()
        print("\n--- Relatório: Frota ---")
        try:
            cursor.execute("SELECT COUNT(*) FROM vehicles")
            total = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM vehicles WHERE status = 1")
            available = cursor.fetchone()[0]
            print(f"Total de Veículos: {total}")
            print(f"Disponíveis: {available}")
            print(f"Em uso/manutenção: {total - available}")
        except sqlite3.OperationalError:
            print("Tabela de veículos ainda não criada.")
        conn.close()

    @staticmethod
    def driverReport():
        conn = Report._get_conn()
        cursor = conn.cursor()
        print("\n--- Relatório: Motoristas ---")
        try:
            cursor.execute("SELECT name, tripCount FROM drivers ORDER BY tripCount DESC LIMIT 5")
            top5 = cursor.fetchall()
            print("Top 5 Motoristas com mais viagens:")
            for d in top5:
                print(f"{d[0]}: {d[1]} viagens")
        except sqlite3.OperationalError:
            print("Tabela de motoristas não encontrada.")
        conn.close()

    @staticmethod
    def fuelReport():
        conn = Report._get_conn()
        cursor = conn.cursor()
        print("\n--- Relatório: Combustível ---")
        try:
            cursor.execute("SELECT fuelType, SUM(totalCost), SUM(ltsSupplied) FROM fuel_supply GROUP BY fuelType")
            data = cursor.fetchall()
            for row in data:
                print(f"Tipo: {row[0]} | Gasto Total: R$ {row[1]:.2f} | Volume: {row[2]:.1f} L")
        except sqlite3.OperationalError:
             print("Sem dados de abastecimento.")
        conn.close()

    @staticmethod
    def maintenanceReport():
        conn = Report._get_conn()
        cursor = conn.cursor()
        print("\n--- Relatório: Manutenção ---")
        try:
            cursor.execute("SELECT SUM(cost) FROM maintenances")
            total = cursor.fetchone()[0]
            if total:
                print(f"Custo total com manutenções: R$ {total:.2f}")
            else:
                print("Sem custos registrados.")
        except sqlite3.OperationalError:
            print("Sem dados.")
        conn.close()

    @staticmethod
    def tripReport():
        conn = Report._get_conn()
        cursor = conn.cursor()
        print("\n--- Relatório: Viagens ---")
        try:
            cursor.execute("SELECT COUNT(*), SUM(distanceKm) FROM trips WHERE status = 'Finalizada'")
            data = cursor.fetchone()
            if data and data[0]:
                print(f"Viagens Finalizadas: {data[0]}")
                print(f"Quilometragem Total Percorrida: {data[1]:.1f} km")
            else:
                print("Nenhuma viagem finalizada.")
        except sqlite3.OperationalError:
             print("Sem dados.")
        conn.close()

    @staticmethod
    def generalReport():
        Report.vehicleReport()
        Report.tripReport()
        Report.maintenanceReport()
        Report.fuelReport()