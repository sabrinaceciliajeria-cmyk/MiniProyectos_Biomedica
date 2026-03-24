# Mini proyecto 1: Calculadora de IMC de pacientes

# Lista para guardar pacientes
pacientes = []

# Función para calcular IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Función para determinar categoría
def categoria_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

# Ciclo para agregar pacientes
while True:
    nombre = input("Nombre del paciente (o 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break

    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))

    imc = calcular_imc(peso, altura)
    categoria = categoria_imc(imc)

    pacientes.append({
        "nombre": nombre,
        "peso": peso,
        "altura": altura,
        "imc": round(imc,2),
        "categoria": categoria
    })

    print(f"{nombre} agregado correctamente.\n")

# Al terminar, preguntar si quieres ver la lista completa
ver_resumen = input("¿Quieres ver la lista completa de pacientes? (si/no): ")
if ver_resumen.lower() == "si":
    print("\n--- Resumen completo de pacientes ---")
    for p in pacientes:
        print(f"Nombre: {p['nombre']}, Peso: {p['peso']} kg, Altura: {p['altura']} m, IMC: {p['imc']}, Categoría: {p['categoria']}")
else:
    print("Resumen no mostrado. Programa finalizado.")

# Mostrar resumen como tabla
if ver_resumen.lower() == "si":
    print("\n--- Resumen completo de pacientes ---")
    # Encabezados
    print(f"{'Nombre':<15} {'Peso(kg)':<10} {'Altura(m)':<10} {'IMC':<10} {'Categoría':<12}")
    print("-"*60)
    
    # Filas de pacientes
    for p in pacientes:
        print(f"{p['nombre']:<15} {p['peso']:<10} {p['altura']:<10} {p['imc']:<10} {p['categoria']:<12}")