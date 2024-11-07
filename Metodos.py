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
