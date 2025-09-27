import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()


    print("Fuentes disponibles (ejemplo):")
    print(", ".join(figlet.getFonts()[:10]), "...")  

    fuente = input("Ingrese el nombre de una fuente (o presione Enter para aleatoria): ").strip()

    if not fuente:
        fuente = random.choice(figlet.getFonts())

    if fuente not in figlet.getFonts():
        print("Fuente no encontrada. Se usará aleatoria.")
        fuente = random.choice(figlet.getFonts())

    figlet.setFont(font=fuente)

    # Pedir al usuario el texto
    texto = input("Ingrese el texto a imprimir: ")

    print("\n--- Resultado FIGlet ---\n")
    print(figlet.renderText(texto))

if __name__ == "__main__":
    main()
