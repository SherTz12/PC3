
# PROBLEMA 3: Cargar alumnos


def cargar_alumnos():
    alumnos = []
    try:
        n = int(input("¿Cuántos alumnos desea cargar?: "))
    except ValueError:
        print("Error: debe ingresar un número entero.")
        return alumnos

    for i in range(n):
        print(f"\nAlumno {i+1}:")
        nombre = input("Ingrese el nombre completo: ")

        notas = []
        for j in range(3):
            while True:
                try:
                    nota = float(input(f"Ingrese la nota {j+1} (0-10): "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("La nota debe estar entre 0 y 10.")
                except ValueError:
                    print("Error: ingrese un número válido.")
        
        promedio = sum(notas) / len(notas)
        alumnos.append({
            "nombre": nombre,
            "notas": notas,
            "promedio": promedio
        })
    return alumnos

# PROBLEMA 4: Clases Rectangulo y Cuadrado

class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def area(self):
        return self.largo * self.ancho

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

# 
# PROBLEMA 5: Contar aprobados y desaprobados
# 

def contar_aprobados(alumnos):
    aprobados = sum(1 for a in alumnos if a["promedio"] >= 4)
    desaprobados = len(alumnos) - aprobados
    return aprobados, desaprobados

# 
# PROBLEMA 6: Promedio del curso

def promedio_curso(alumnos):
    if not alumnos:
        return 0
    return sum(a["promedio"] for a in alumnos) / len(alumnos)


# PROBLEMA 7: Mejor y peor promedio

def extremos_promedio(alumnos):
    if not alumnos:
        return None, None
    mejor = max(alumnos, key=lambda a: a["promedio"])
    peor = min(alumnos, key=lambda a: a["promedio"])
    return mejor, peor

# PROBLEMA 7 

def buscar_alumno(alumnos, texto):
    resultados = [a for a in alumnos if texto.lower() in a["nombre"].lower()]
    return resultados




def menu():
    alumnos = []
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Cargar alumnos")
        print("2. Crear Rectángulo y Cuadrado")
        print("3. Contar aprobados y desaprobados")
        print("4. Promedio del curso")
        print("5. Mostrar mejor y peor promedio")
        print("6. Buscar alumno por nombre")
        print("0. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            alumnos = cargar_alumnos()
        elif opcion == "2":
            try:
                largo = float(input("Ingrese el largo del rectángulo: "))
                ancho = float(input("Ingrese el ancho del rectángulo: "))
                r = Rectangulo(largo, ancho)
                print(f"Área del rectángulo: {r.area()}")

                lado = float(input("Ingrese el lado del cuadrado: "))
                c = Cuadrado(lado)
                print(f"Área del cuadrado: {c.area()}")
            except ValueError:
                print("Error: ingrese un número válido.")
        elif opcion == "3":
            if alumnos:
                ap, des = contar_aprobados(alumnos)
                print(f"Aprobados: {ap}, Desaprobados: {des}")
            else:
                print("Primero debe cargar alumnos (opción 1).")
        elif opcion == "4":
            if alumnos:
                print(f"Promedio del curso: {promedio_curso(alumnos):.2f}")
            else:
                print("Primero debe cargar alumnos (opción 1).")
        elif opcion == "5":
            if alumnos:
                mejor, peor = extremos_promedio(alumnos)
                print(f"Mejor promedio: {mejor['nombre']} con {mejor['promedio']:.2f}")
                print(f"Peor promedio: {peor['nombre']} con {peor['promedio']:.2f}")
            else:
                print("Primero debe cargar alumnos (opción 1).")
        elif opcion == "6":
            if alumnos:
                texto = input("Ingrese el nombre (completo o parcial) a buscar: ")
                resultados = buscar_alumno(alumnos, texto)
                if resultados:
                    for r in resultados:
                        print(f"- {r['nombre']}, Notas: {r['notas']}, Promedio: {r['promedio']:.2f}")
                else:
                    print("No se encontraron alumnos con ese nombre.")
            else:
                print("Primero debe cargar alumnos (opción 1).")
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente nuevamente.")


if __name__ == "__main__":
    menu()
