from Metodos import Admin

met = Admin()

def ejecutar_menu():
    opciones_menu_principal = {
        '1': ('Agregar Inventario', met.agregar_inventario),
        '2': ('Agregar gastos operativo', met.registrar_gasto_operativo),
        '3': ('Agregar ingreso', met.registrar_ingreso),
        '4': ('Agregar otros gastos', met.registrar_otro_gasto),
        '0': ('Salida', confirmar_salida)
    }
    while True:
        
        opcion_menu = input("\n--- Menú Principal ---\n1. Agregar Inventario\n2. Agregar Inventario\n3. Agregar ingreso\n4. Agregar otros gastos\n5. Salida\nSeleccione una opción: ").strip()
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