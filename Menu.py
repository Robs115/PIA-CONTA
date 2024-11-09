from Metodos import Admin

met = Admin()

def ejecutar_menu():
    opciones_menu_principal = {
        '1': ('Agregar Inventario', met.agregar_producto),
        '2': ('Agregar gastos operativos', met.registrar_gasto_operativo),
        '3': ('Agregar ingreso', met.registrar_ingreso),
        '4': ('Agregar otros gastos', met.registrar_otro_gasto),
        '5': ('Estado de Resultados General', met.estado_resultado_general),
        '6': ('Estado de Resultados por Periodo', met.estado_resultado_por_periodo),
        '7': ('Punto de Equilibrio General', met.punto_equilibrio_todos_productos),
        '8': ('Punto de Equilibrio por Periodo', met.punto_equilibrio_producto_especifico),
        '9': ('Salida', confirmar_salida)
    }
    while True:
        print("\n--- Menú Principal ---")
        for key, value in opciones_menu_principal.items():
            print(f"{key}. {value[0]}")
        
        opcion_menu = input("Seleccione una opción: ").strip()
        accion_principal = opciones_menu_principal.get(opcion_menu, (None, lambda: print("Opción no válida")))[1]
        accion_principal()


def confirmar_salida():
    while True:
        salida = input("\n¿Está seguro de que desea salir? (Escribe S para salir, N para volver al menu principal)): ").strip().lower()
        if salida == 's':
            print("\n...Saliendo del sistema...")
            exit()
        elif salida == 'n':
            return
        else:
            print("Opcion no valida.")
        
        print("\n--------------------------------------------------------")

ejecutar_menu()