import sqlite3
from datetime import datetime

class Admin:

    def agregar_inventario(self):
        """Solicita el ID del producto, la cantidad y la fecha para aumentar el inventario, con validaciones."""
        while True:
            try:
                id_producto = int(input("Ingrese el ID del producto: "))
                if id_producto <= 0:
                    print("El ID del producto debe ser un número positivo.")
                    continue
                break
            except ValueError:
                print("Por favor, ingrese un número válido para el ID del producto.")
        
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad a agregar al inventario: "))
                if cantidad <= 0:
                    print("La cantidad debe ser un número positivo.")
                    continue
                break
            except ValueError:
                print("Por favor, ingrese un número válido para la cantidad.")

        fecha = input("Ingrese la fecha de registro (YYYY-MM-DD) o deje vacío para usar la fecha actual: ")
        if fecha:
            if not self.validar_fecha(fecha):
                print("Formato de fecha no válido. Se usará la fecha actual.")
                fecha = datetime.now().strftime("%Y-%m-%d")
        else:
            fecha = datetime.now().strftime("%Y-%m-%d")
        
        with sqlite3.connect("empresalapices.db") as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE Productos SET stock = stock + ? WHERE id_producto = ?", (cantidad, id_producto))
            print(f"Se ha añadido {cantidad} unidades al inventario del producto con ID {id_producto} en la fecha {fecha}.")

    def registrar_gasto_operativo(self):
        """Solicita el nombre, monto y fecha del gasto operativo con validaciones."""
        nombre = input("Ingrese el nombre del gasto operativo: ").strip()
        if not nombre:
            print("El nombre del gasto no puede estar vacío.")
            return
        
        while True:
            try:
                monto = float(input("Ingrese el monto del gasto operativo: "))
                if monto <= 0:
                    print("El monto debe ser un valor positivo.")
                    continue
                break
            except ValueError:
                print("Por favor, ingrese un monto válido.")
        
        fecha = input("Ingrese la fecha de registro (YYYY-MM-DD) o deje vacío para usar la fecha actual: ")
        if fecha:
            if not self.validar_fecha(fecha):
                print("Formato de fecha no válido. Se usará la fecha actual.")
                fecha = datetime.now().strftime("%Y-%m-%d")
        else:
            fecha = datetime.now().strftime("%Y-%m-%d")
        
        with sqlite3.connect("empresalapices.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO GastosOperativos (nombre, monto, fecha) VALUES (?, ?, ?)", 
                        (nombre, monto, fecha))
            print(f"Gasto operativo registrado: {nombre} - ${monto} en la fecha {fecha}")

    def registrar_ingreso(self):
        """Solicita el nombre, monto y fecha del ingreso con validaciones."""
        nombre = input("Ingrese el nombre del ingreso: ").strip()
        if not nombre:
            print("El nombre del ingreso no puede estar vacío.")
            return
        
        while True:
            try:
                monto = float(input("Ingrese el monto del ingreso: "))
                if monto <= 0:
                    print("El monto debe ser un valor positivo.")
                    continue
                break
            except ValueError:
                print("Por favor, ingrese un monto válido.")
        
        fecha = input("Ingrese la fecha de registro (YYYY-MM-DD) o deje vacío para usar la fecha actual: ")
        if fecha:
            if not self.validar_fecha(fecha):
                print("Formato de fecha no válido. Se usará la fecha actual.")
                fecha = datetime.now().strftime("%Y-%m-%d")
        else:
            fecha = datetime.now().strftime("%Y-%m-%d")
        
        with sqlite3.connect("empresalapices.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO OtrosIngresos (nombre, monto, fecha) VALUES (?, ?, ?)", 
                           (nombre, monto, fecha))
            print(f"Ingreso registrado: {nombre} - ${monto} en la fecha {fecha}")

    def registrar_otro_gasto(self):
        """Solicita el nombre, monto y fecha del otro gasto con validaciones."""
        nombre = input("Ingrese el nombre del otro gasto: ").strip()
        if not nombre:
            print("El nombre del gasto no puede estar vacío.")
            return
        
        while True:
            try:
                monto = float(input("Ingrese el monto del otro gasto: "))
                if monto <= 0:
                    print("El monto debe ser un valor positivo.")
                    continue
                break
            except ValueError:
                print("Por favor, ingrese un monto válido.")
        
        fecha = input("Ingrese la fecha de registro (YYYY-MM-DD) o deje vacío para usar la fecha actual: ")
        if fecha:
            if not self.validar_fecha(fecha):
                print("Formato de fecha no válido. Se usará la fecha actual.")
                fecha = datetime.now().strftime("%Y-%m-%d")
        else:
            fecha = datetime.now().strftime("%Y-%m-%d")
        
        with sqlite3.connect("empresalapices.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO OtrosGastos (nombre, monto, fecha) VALUES (?, ?, ?)", 
                           (nombre, monto, fecha))
            print(f"Otro gasto registrado: {nombre} - ${monto} en la fecha {fecha}")

    def validar_fecha(self, fecha):
        """Valida el formato de fecha ingresado por el usuario."""
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
            return True
        except ValueError:
            return False
        
    def estado_resultado_general(self):
        """Calcula y muestra el estado de resultados general en la consola."""
        with sqlite3.connect("empresalapices.db") as conn:
            cursor = conn.cursor()
            
            # Calcular ingresos totales (Ventas + Otros Ingresos + Ingresos)
            cursor.execute("SELECT SUM(total) FROM Ventas")
            total_ventas = cursor.fetchone()[0] or 0
            
            cursor.execute("SELECT SUM(monto) FROM OtrosIngresos")
            total_otros_ingresos = cursor.fetchone()[0] or 0

            cursor.execute("SELECT SUM(monto) FROM Ingresos")
            total_ingresos = cursor.fetchone()[0] or 0
            
            ingresos_totales = total_ventas + total_otros_ingresos + total_ingresos
            
            # Calcular costos totales (Costo de producción de los productos vendidos)
            cursor.execute("SELECT SUM(costo_produccion) FROM Productos")
            total_costos = cursor.fetchone()[0] or 0
            
            # Calcular gastos operativos
            cursor.execute("SELECT SUM(monto) FROM GastosOperativos")
            gastos_operativos = cursor.fetchone()[0] or 0
            
            # Calcular utilidad bruta y utilidad neta
            utilidad_bruta = ingresos_totales - total_costos
            utilidad_neta = utilidad_bruta - gastos_operativos
            
            # Mostrar resultados
            print("\nEstado de Resultados General")
            print("=" * 30)
            print(f"Ingresos por ventas:        ${total_ventas:,.2f}")
            print(f"Otros ingresos:             ${total_otros_ingresos:,.2f}")
            print(f"Ingresos adicionales:       ${total_ingresos:,.2f}")
            print(f"Ingresos totales:           ${ingresos_totales:,.2f}")
            print(f"Costos de producción:       ${total_costos:,.2f}")
            print(f"Gastos operativos:          ${gastos_operativos:,.2f}")
            print(f"Utilidad bruta:             ${utilidad_bruta:,.2f}")
            print(f"Utilidad neta:              ${utilidad_neta:,.2f}")
            print("=" * 30)

    def estado_resultado_por_periodo(self):
        """Calcula y muestra el estado de resultados por un periodo específico en la consola."""
        
        # Solicitar y validar fechas de inicio y fin
        while True:
            fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
            fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD): ")
            
            try:
                fecha_inicio_dt = datetime.strptime(fecha_inicio, "%Y-%m-%d")
                fecha_fin_dt = datetime.strptime(fecha_fin, "%Y-%m-%d")
                
                if fecha_inicio_dt > fecha_fin_dt:
                    print("La fecha de inicio debe ser anterior a la fecha de fin. Intente nuevamente.")
                else:
                    break
            except ValueError:
                print("Formato de fecha inválido. Use el formato YYYY-MM-DD. Intente nuevamente.")
        
        # Realizar los cálculos dentro del periodo
        with sqlite3.connect("empresalapices.db") as conn:
            cursor = conn.cursor()
            
            # Calcular ingresos por ventas en el periodo
            cursor.execute("""
                SELECT SUM(total) FROM Ventas 
                WHERE fecha BETWEEN ? AND ?
            """, (fecha_inicio, fecha_fin))
            total_ventas = cursor.fetchone()[0] or 0
            
            # Calcular otros ingresos en el periodo
            cursor.execute("""
                SELECT SUM(monto) FROM OtrosIngresos 
                WHERE fecha BETWEEN ? AND ?
            """, (fecha_inicio, fecha_fin))
            total_otros_ingresos = cursor.fetchone()[0] or 0
            
            # Calcular ingresos adicionales en el periodo
            cursor.execute("""
                SELECT SUM(monto) FROM Ingresos 
                WHERE fecha BETWEEN ? AND ?
            """, (fecha_inicio, fecha_fin))
            total_ingresos = cursor.fetchone()[0] or 0
            
            ingresos_totales = total_ventas + total_otros_ingresos + total_ingresos
            
            # Calcular costos totales en el periodo
            cursor.execute("""
                SELECT SUM(costo_produccion) FROM Productos 
                WHERE fecha BETWEEN ? AND ?
            """, (fecha_inicio, fecha_fin))
            total_costos = cursor.fetchone()[0] or 0
            
            # Calcular gastos operativos en el periodo
            cursor.execute("""
                SELECT SUM(monto) FROM GastosOperativos 
                WHERE fecha BETWEEN ? AND ?
            """, (fecha_inicio, fecha_fin))
            gastos_operativos = cursor.fetchone()[0] or 0
            
            # Calcular utilidad bruta y utilidad neta
            utilidad_bruta = ingresos_totales - total_costos
            utilidad_neta = utilidad_bruta - gastos_operativos
            
            # Mostrar resultados
            print(f"\nEstado de Resultados del Periodo ({fecha_inicio} a {fecha_fin})")
            print("=" * 50)
            print(f"Ingresos por ventas:        ${total_ventas:,.2f}")
            print(f"Otros ingresos:             ${total_otros_ingresos:,.2f}")
            print(f"Ingresos adicionales:       ${total_ingresos:,.2f}")
            print(f"Ingresos totales:           ${ingresos_totales:,.2f}")
            print(f"Costos de producción:       ${total_costos:,.2f}")
            print(f"Gastos operativos:          ${gastos_operativos:,.2f}")
            print(f"Utilidad bruta:             ${utilidad_bruta:,.2f}")
            print(f"Utilidad neta:              ${utilidad_neta:,.2f}")
            print("=" * 50)