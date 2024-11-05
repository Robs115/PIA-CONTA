#prueba muy basica 
#no creo que lo dejemos asi

import sqlite3

def estado_de_resultados():
    # Conectar a la base de datos
    conexion = sqlite3.connect('empresa_lapices.db')
    cursor = conexion.cursor()
    
    # Obtener ventas netas y costo de ventas
    cursor.execute("""
        SELECT p.nombre, p.precio_venta, p.costo_produccion, SUM(v.cantidad_vendida) AS total_vendido
        FROM Productos p
        JOIN Ventas v ON p.id_producto = v.id_producto
        GROUP BY p.id_producto
    """)
    
    ventas_netas = 0
    costo_ventas = 0
    
    for producto in cursor.fetchall():
        nombre, precio_venta, costo_produccion, total_vendido = producto
        ventas_producto = precio_venta * total_vendido
        costo_producto = costo_produccion * total_vendido
        
        ventas_netas += ventas_producto
        costo_ventas += costo_producto
    
    utilidad_bruta = ventas_netas - costo_ventas

    # Obtener gastos operativos
    cursor.execute("SELECT SUM(monto) FROM GastosOperativos")
    gastos_operativos = cursor.fetchone()[0] or 0

    # Obtener otros ingresos y otros gastos
    cursor.execute("SELECT SUM(monto) FROM OtrosIngresos")
    otros_ingresos = cursor.fetchone()[0] or 0
    
    cursor.execute("SELECT SUM(monto) FROM OtrosGastos")
    otros_gastos = cursor.fetchone()[0] or 0
    
    # Calcular utilidades
    utilidad_operativa = utilidad_bruta - gastos_operativos

    utilidad_antes_impuestos = utilidad_operativa + otros_ingresos - otros_gastos

    impuestos = utilidad_antes_impuestos * 0.30  # Tasa de impuestos del 30%

    utilidad_neta = utilidad_antes_impuestos - impuestos

    # Mostrar el estado de resultados completo
    print("\nEstado de Resultados Completo")
    print("-----------------------------")
    print(f"Ventas Netas:              ${ventas_netas:,.2f}")
    print(f"(-) Costo de Ventas:       ${costo_ventas:,.2f}")
    print(f"= Utilidad Bruta:          ${utilidad_bruta:,.2f}")
    print(f"(-) Gastos Operativos:     ${gastos_operativos:,.2f}")
    print(f"= Utilidad Operativa:      ${utilidad_operativa:,.2f}")
    print(f"(+) Otros Ingresos:        ${otros_ingresos:,.2f}")
    print(f"(-) Otros Gastos:          ${otros_gastos:,.2f}")
    print(f"= Utilidad Antes de Impuestos: ${utilidad_antes_impuestos:,.2f}")
    print(f"(-) Impuestos (30%):       ${impuestos:,.2f}")
    print(f"= Utilidad Neta:           ${utilidad_neta:,.2f}")

    # Cerrar la conexión
    conexion.close()

