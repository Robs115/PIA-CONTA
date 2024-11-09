import sqlite3
from datetime import datetime

class Admin:

    def agregar_producto(self):
        """Solicita los datos del producto y los agrega a la base de datos, con validaciones, y genera el ID en Python."""

        # Solicitar los datos del producto
        nombre = input("Ingrese el nombre del producto: ").strip()
        if not nombre:
            print("El nombre del producto no puede estar vacío.")
            return

        while True:
            try:
                precio = float(input("Ingrese el precio del producto: "))
                if precio <= 0:
                    print("El precio debe ser un valor positivo.")
                    continue
                break
            except ValueError:
                print("Por favor, ingrese un precio válido.")

        while True:
            try:
                cantidad = int(input("Ingrese la cantidad del producto en inventario: "))
                if cantidad < 0:
                    print("La cantidad no puede ser negativa.")
                    continue
                break
            except ValueError:
                print("Por favor, ingrese una cantidad válida.")

        # Abrir conexión a la base de datos
        with sqlite3.connect("empresalapices.db") as conn:
            cursor = conn.cursor()

            # Obtener el último ID_PRODUCTO para generar el siguiente ID automáticamente
            cursor.execute("SELECT MAX(id_producto) FROM Productos")
            ultimo_id = cursor.fetchone()[0]

            # Si no hay productos en la tabla, empezar con id_producto = 1
            nuevo_id = 1 if ultimo_id is None else ultimo_id + 1

            # Insertar el nuevo producto
            cursor.execute("""
                INSERT INTO Productos (id_producto, nombre, precio, stock)
                VALUES (?, ?, ?, ?)
            """, (nuevo_id, nombre, precio, cantidad))

            # Confirmación de que el producto ha sido agregado
            print(f"Producto '{nombre}' agregado con éxito con un precio de ${precio} y una cantidad de {cantidad} unidades.")


    def registrar_gasto_operativo(self):
        """Solicita una categoría de gasto operativo, muestra su valor actual y luego incrementa su valor en la base de datos."""
        categorias_gasto = [
            "Transporte", "Servicios de limpieza", "Servicios bancarios", "Seguro", "Seguridad",
            "Salarios", "Reparaciones", "Renta", "Publicidad", "Papelería", "Material de oficina",
            "Mantenimiento", "Internet", "Insumos varios", "Gastos legales", "Flete", "Equipo de seguridad",
            "Electricidad", "Consultoría", "Capacitación"
        ]
        # Mostrar las categorías disponibles
        print("Categorías de gastos operativos disponibles:")
        for index, categoria in enumerate(categorias_gasto, 1):
            print(f"{index}. {categoria}")

        # Solicitar la categoría al usuario
        while True:
            try:
                opcion = int(input("Seleccione el número de la categoría a la que desea incrementar el valor: "))
                if 1 <= opcion <= len(categorias_gasto):
                    categoria_seleccionada = categorias_gasto[opcion - 1]
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")
            except ValueError:
                print("Por favor ingrese un número válido.")

        # Abrir conexión a la base de datos
        with sqlite3.connect("empresalapices.db") as conn:
            cursor = conn.cursor()

            # Consultar el valor actual registrado para la categoría seleccionada
            cursor.execute("SELECT valor FROM GastosOperativos WHERE categoria = ?", (categoria_seleccionada,))
            categoria = cursor.fetchone()

            if categoria:
                # Mostrar el valor actual de la categoría
                print(f"El valor actual registrado para '{categoria_seleccionada}' es: ${categoria[0]}")
                valor_actual = categoria[0]
            else:
                # Si no existe un valor, mostrar que no se ha registrado
                print(f"No se ha registrado un valor para '{categoria_seleccionada}'.")
                valor_actual = 0

            # Solicitar el valor a incrementar
            while True:
                try:
                    incremento = float(input(f"Ingrese el valor a incrementar para '{categoria_seleccionada}': "))
                    if incremento <= 0:
                        print("El valor debe ser mayor que 0.")
                        continue
                    break
                except ValueError:
                    print("Por favor ingrese un valor válido.")

            # Verificar si la categoría existe en la tabla
            if categoria:
                # Si ya existe, incrementar el valor
                nuevo_valor = valor_actual + incremento
                cursor.execute("UPDATE GastosOperativos SET valor = ? WHERE categoria = ?", (nuevo_valor, categoria_seleccionada))
                print(f"Se ha incrementado el valor de '{categoria_seleccionada}' en ${incremento}. Nuevo valor: ${nuevo_valor}.")
            else:
                # Si no existe, agregar un nuevo registro con el valor inicial
                cursor.execute("INSERT INTO GastosOperativos (categoria, valor) VALUES (?, ?)", (categoria_seleccionada, incremento))
                print(f"Se ha registrado un nuevo gasto operativo de '${incremento}' para la categoría '{categoria_seleccionada}'.")

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