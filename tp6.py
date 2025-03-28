def cargar_datos():
    alumnos = []
    try:
        with open('alumnos.txt', 'r') as archivo:
            for linea in archivo:
                datos = linea.strip().split(',')
                alumno = {
                    "nombre": datos[0],
                    "apellido": datos[1],
                    "fecha_nacimiento": datos[2],
                    "dni": datos[3],
                    "tutor": datos[4],
                    "notas": list(map(int, datos[5].split(';'))),
                    "faltas": int(datos[6]),
                    "amonestaciones": int(datos[7])
                }
                alumnos.append(alumno)
    except FileNotFoundError:
        pass
    return alumnos

def guardar_datos(alumnos):
    with open('alumnos.txt', 'w') as archivo:
        for alumno in alumnos:
            notas = ';'.join(map(str, alumno['notas']))
            archivo.write(f"{alumno['nombre']},{alumno['apellido']},{alumno['fecha_nacimiento']},{alumno['dni']},{alumno['tutor']},{notas},{alumno['faltas']},{alumno['amonestaciones']}\n")

def agregar_alumno(alumnos):
    alumno = {
        "nombre": input("Nombre: "),
        "apellido": input("Apellido: "),
        "fecha_nacimiento": input("Fecha de nacimiento (DD/MM/AAAA): "),
        "dni": input("DNI: "),
        "tutor": input("Nombre del tutor: "),
        "notas": [int(nota) for nota in input("Notas (separadas por comas): ").split(',')],
        "faltas": int(input("Cantidad de faltas: ")),
        "amonestaciones": int(input("Cantidad de amonestaciones: "))
    }
    alumnos.append(alumno)
    guardar_datos(alumnos)

def mostrar_alumnos(alumnos):
    if not alumnos:
        print("No hay alumnos en el registro.")
        return
    for alumno in alumnos:
        print(f"\nNombre: {alumno['nombre']} {alumno['apellido']}")
        print(f"Fecha de Nacimiento: {alumno['fecha_nacimiento']}")
        print(f"DNI: {alumno['dni']}")
        print(f"Tutor: {alumno['tutor']}")
        print(f"Notas: {alumno['notas']}")
        print(f"Faltas: {alumno['faltas']}")
        print(f"Amonestaciones: {alumno['amonestaciones']}")

def modificar_datos(alumnos):
    dni = input("Introduce el DNI del alumno a modificar: ")
    alumno = next((alumno for alumno in alumnos if alumno['dni'] == dni), None)
    
    if alumno:
        print("Modificar datos del alumno:")
        alumno['nombre'] = input(f"Nuevo nombre ({alumno['nombre']}): ") or alumno['nombre']
        alumno['apellido'] = input(f"Nuevo apellido ({alumno['apellido']}): ") or alumno['apellido']
        alumno['fecha_nacimiento'] = input(f"Nueva fecha de nacimiento ({alumno['fecha_nacimiento']}): ") or alumno['fecha_nacimiento']
        alumno['tutor'] = input(f"Nuevo nombre del tutor ({alumno['tutor']}): ") or alumno['tutor']
        notas = input(f"Nuevas notas ({', '.join(map(str, alumno['notas']))}): ")
        if notas:
            alumno['notas'] = [int(nota) for nota in notas.split(',')]
        faltas = input(f"Nuevas faltas ({alumno['faltas']}): ")
        if faltas:
            alumno['faltas'] = int(faltas)
        amonestaciones = input(f"Nuevas amonestaciones ({alumno['amonestaciones']}): ")
        if amonestaciones:
            alumno['amonestaciones'] = int(amonestaciones)

        guardar_datos(alumnos)
        print("Datos modificados correctamente.")
    else:
        print("Alumno no encontrado.")

def expulsar_alumno(alumnos):
    dni = input("Introduce el DNI del alumno a expulsar: ")
    alumno = next((alumno for alumno in alumnos if alumno['dni'] == dni), None)
    
    if alumno:
        alumnos.remove(alumno)
        guardar_datos(alumnos)
        print(f"Alumno con DNI {dni} expulsado.")
    else:
        print(f"Alumno con DNI {dni} no encontrado.")

def menu():
    alumnos = cargar_datos()
    
    while True:
        print("\n--- Menú ---")
        print("1. Agregar alumno")
        print("2. Mostrar datos de los alumnos")
        print("3. Modificar datos de un alumno")
        print("4. Expulsar alumno")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            agregar_alumno(alumnos)
        elif opcion == '2':
            mostrar_alumnos(alumnos)
        elif opcion == '3':
            modificar_datos(alumnos)
        elif opcion == '4':
            expulsar_alumno(alumnos)
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción del menú.")

if __name__ == "__main__":
    menu()
