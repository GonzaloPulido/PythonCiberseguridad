while True:
    try:
        horas = int(input("Introduce tus horas de trabajo: "))
        coste = int(input("Introduce el coste por hora: "))
        print("Tu pago es de:", horas * coste)
        break
    except ValueError:
        print("Error: Debes introducir un número válido.")