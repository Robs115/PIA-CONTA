#prueba muy basica 
#no creo que lo dejemos asi

def estado_de_resultados():
    print("Generador de Estado de Resultados")
    print("----------------------------------")

    # Solicitar ingresos y costos
    ventas = float(input("Ingrese las ventas netas ($): "))
    costo_ventas = float(input("Ingrese el costo de ventas ($): "))
    gastos_operativos = float(input("Ingrese los gastos operativos ($): "))
    gastos_generales = float(input("Ingrese los gastos generales y administrativos ($): "))
    otros_ingresos = float(input("Ingrese otros ingresos ($): "))
    otros_gastos = float(input("Ingrese otros gastos ($): "))

    # Calcular resultados
    utilidad_bruta = ventas - costo_ventas
    utilidad_operativa = utilidad_bruta - gastos_operativos - gastos_generales
    utilidad_antes_impuestos = utilidad_operativa + otros_ingresos - otros_gastos
    impuestos = utilidad_antes_impuestos * 0.30  # Supongamos una tasa de impuestos del 30%
    utilidad_neta = utilidad_antes_impuestos - impuestos

    # Mostrar el estado de resultados
    print("\nEstado de Resultados")
    print("---------------------")
    print(f"Ventas Netas:                           ${ventas:,.2f}")
    print(f"(-) Costo de Ventas:                    ${costo_ventas:,.2f}")
    print(f"= Utilidad Bruta:                       ${utilidad_bruta:,.2f}")
    print(f"(-) Gastos Operativos:                  ${gastos_operativos:,.2f}")
    print(f"(-) Gastos Generales y Administrativos: ${gastos_generales:,.2f}")
    print(f"= Utilidad Operativa:                   ${utilidad_operativa:,.2f}")
    print(f"(+) Otros Ingresos:                     ${otros_ingresos:,.2f}")
    print(f"(-) Otros Gastos:                       ${otros_gastos:,.2f}")
    print(f"= Utilidad Antes de Impuestos:          ${utilidad_antes_impuestos:,.2f}")
    print(f"(-) Impuestos (30%):                    ${impuestos:,.2f}")
    print(f"= Utilidad Neta:                        ${utilidad_neta:,.2f}")

