def obtener_fraccion():
    """
    Pide al usuario una fracción X/Y hasta que sea válida.
    Devuelve el valor como fracción decimal (entre 0 y 1).
    """
    while True:
        try:
            fraccion = input("Ingrese una fracción en formato X/Y: ")
            x, y = fraccion.split("/")

            # Convertir a enteros
            x = int(x)
            y = int(y)

            # Validar que Y no sea cero
            if y == 0:
                raise ZeroDivisionError("El denominador no puede ser cero.")

            # Validar que X <= Y
            if x > y:
                raise ValueError("El numerador no puede ser mayor que el denominador.")

            return x / y

        except ValueError:
            print("Error: Solo se permiten enteros y X debe ser menor o igual a Y.")
        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero.")


def mostrar_combustible():
    """
    Convierte la fracción a porcentaje y muestra E, F o %.
    """
    fraccion = obtener_fraccion()
    porcentaje = round(fraccion * 100)

    if porcentaje <= 1:   # menor o igual al 1%
        print("E")
    elif porcentaje >= 99:  # mayor o igual al 99%
        print("F")
    else:
        print(f"{porcentaje}%")


# Ejecutar programa
if __name__ == "__main__":
    mostrar_combustible()
