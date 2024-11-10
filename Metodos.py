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
                tipo = input("Digite el tipo o material")
                if tipo == "":
                    input("No debe estar vacio")
                    return
                elif tipo.isnumeric():
                    print(" no puede llevar numeros")
                    return
                
                break
            except ValueError:
                print("Hubo un error")
        
        while True:
            try:
                costo_produccion = float(input("Digite el costo de produccion"))
                if not costo_produccion:
                    print("No debe ir vacio")
                    return
                break
            except ValueError:
                print("ah Habido un error")


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
                INSERT INTO Productos (id_producto, nombre, tipo, costo_produccion, precio_venta, stock)
                VALUES (?, ?, ?, ?)
            """, (nuevo_id, nombre, tipo,costo_produccion, precio, cantidad))

            # Confirmación de que el producto ha sido agregado
            print(f"Producto '{nombre}' agregado con éxito con un precio de ${precio} y una cantidad de {cantidad} unidades.")


    def registrar_gasto_operativo(self):

        # Lista de categorías de gasto operativo
        categorias = [
            "Renta", "Electricidad", "Internet", "Papelería", "Mantenimiento", 
            "Servicios de limpieza", "Seguridad", "Salarios", "Capacitación", 
            "Publicidad", "Transporte", "Consultoría", "Seguro", "Reparaciones", 
            "Insumos varios", "Material de oficina", "Equipo de seguridad", 
            "Flete", "Gastos legales", "Servicios bancarios"
        ]

        # Mostrar categorías y solicitar nombre del gasto
        print("Categorías de gastos operativos:")
        for i, categoria in enumerate(categorias, 1):
            print(f"{i}. {categoria}")
        
        indice_categoria = int(input("Seleccione el número de la categoría de gasto: "))
        if 1 <= indice_categoria <= len(categorias):
            nombre = categorias[indice_categoria - 1]
        else:
            print("Selección no válida.")
            return
        
        # Solicitar valor del gasto
        try:
            valor = float(input(f"Ingrese el valor para '{nombre}': "))
        except ValueError:
            print("Valor no válido. Ingrese un número.")
            return

        # Conectar a la base de datos y actualizar/agregar el gasto
        with sqlite3.connect('mi_base_de_datos.db') as conexion:
            cursor = conexion.cursor()
            
            # Buscar el gasto operativo en la base de datos
            cursor.execute("SELECT valor FROM GastosOperativos WHERE nombre = ?", (nombre,))
            resultado = cursor.fetchone()
            
            if resultado:
                # Si el gasto existe, sumarle el valor al actual
                nuevo_valor = resultado[0] + valor
                cursor.execute("UPDATE GastosOperativos SET valor = ? WHERE nombre = ?", (nuevo_valor, nombre))
                print(f"Actualizado '{nombre}' con nuevo valor: {nuevo_valor}")
            else:
                # Si el gasto no existe, agregarlo como nuevo
                cursor.execute("INSERT INTO GastosOperativos (nombre, valor) VALUES (?, ?)", (nombre, valor))
                print(f"Agregado nuevo gasto '{nombre}' con valor: {valor}")
            


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

    def punto_equilibrio_todos_productos(self):
        """Calcula el punto de equilibrio para todos los productos."""
        try:
            with sqlite3.connect("empresalapices.db") as conn:
                cursor = conn.cursor()
                
                # Obtener costos fijos desde la tabla GastosOperativos
                cursor.execute("SELECT SUM(monto) FROM GastosOperativos WHERE tipo = 'fijo'")  # Asumiendo que hay un campo 'tipo'
                costos_fijos_result = cursor.fetchone()
                
                if costos_fijos_result is None or costos_fijos_result[0] is None:
                    print("Error: No se encontraron costos fijos en la base de datos.")
                    return
                
                costos_fijos = costos_fijos_result[0]
                
                # Obtener todos los productos
                cursor.execute("SELECT id_producto, precio_venta, costo_variable FROM Productos")
                productos = cursor.fetchall()
                
                if not productos:
                    print("No se encontraron productos en la base de datos.")
                    return
                
                puntos_equilibrio = {}
                
                for producto in productos:
                    id_producto, precio_venta, costo_variable = producto
                    if precio_venta > costo_variable:  
                        punto_equilibrio = costos_fijos / (precio_venta - costo_variable)
                        puntos_equilibrio[id_producto] = punto_equilibrio
                    else:
                        puntos_equilibrio[id_producto] = None 
                
                # Mostrar resultados
                for id_producto, punto_equilibrio in puntos_equilibrio.items():
                    if punto_equilibrio is not None:
                        print(f"Punto de equilibrio para el producto ID {id_producto}: {punto_equilibrio:.2f} unidades")
                    else:
                        print(f"No se puede calcular el punto de equilibrio para el producto ID {id_producto} (precio de venta <= costo variable)")
        
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
    
    def punto_equilibrio_producto_especifico(self):
        """Calcula el punto de equilibrio para un producto específico."""
        
        id_producto = input("Por favor, ingrese el ID del producto: ")
        with sqlite3.connect ("empresalapices.db") as conn:
            cursor = conn.cursor()
            cursor.execute("Select * from Productos")
            productos = cursor.fetchall()[0]


        # Verificar si el producto existe
            if id_producto not in productos:
                print("El ID del producto no existe.")
                return
        
        try:
            with sqlite3.connect("empresalapices.db") as conn:
                cursor = conn.cursor()
                
                # Obtener costos fijos desde la tabla GastosOperativos
                cursor.execute("SELECT SUM(monto) FROM GastosOperativos WHERE tipo = 'FIJO'")  # Asumiendo que hay un campo 'tipo'
                costos_fijos_result = cursor.fetchone()
                
                if costos_fijos_result is None or costos_fijos_result[0] is None:
                    print("Error: No se encontraron costos fijos en la base de datos.")
                    return
                
                costos_fijos = costos_fijos_result[0]
                
                # Obtener el producto específico
                cursor.execute("SELECT precio_venta, costo_variable FROM Productos WHERE id_producto = ?", (id_producto,))
                producto = cursor.fetchone()
                
                if producto:
                    precio_venta, costo_variable = producto
                    if precio_venta > costo_variable:
                        punto_equilibrio = costos_fijos / (precio_venta - costo_variable)
                        print(f"Punto de equilibrio para el producto ID {id_producto}: {punto_equilibrio:.2f} unidades")
                    else:
                        print(f"No se puede calcular el punto de equilibrio para el producto ID {id_producto} (precio de venta <= costo variable)")
                else:
                    print(f"Producto con ID {id_producto} no encontrado.")
        
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")