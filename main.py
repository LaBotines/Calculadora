# metodos de operacion
def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def multiplicacion(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


# metodo seleccion operación
def calculadora():
    print("Seleccione una operación:")
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplicación")
    print("4.División")

# metodo main - llama la calculadora
def start():

    calculadora()

    opcion = input("Digite la opción deseada: ")

    # opciones disponibles de operación: 1-suma / 2-resta / 3-multiplicación / 4-división, y verificacion en caso de no seleccionar una opción válida
    if (opcion == "1" or
            opcion == "2" or
            opcion == "3" or
            opcion == "4"):
        num1 = float(input("Digite el primer número: "))
        num2 = float(input("Digite el segundo número: "))
    else:
        retry = input("Selección no válida, volver a intentar? S N: ")
        if (retry == "S" or
                retry == "s"):
            start()
        else:
            print("Hasta luego!")
            exit()

    #ciclo para seleccionar opciones disponibles
    if opcion == "1":
        print(num1, "+", num2, " = ", suma(num1, num2))
    elif opcion == "2":
        print(num1, "-", num2, " = ", resta(num1, num2))
    elif opcion == "3":
        print(num1, "*", num2, " = ", multiplicacion(num1, num2))
    elif opcion == "4":
        try:
            num2 == 0
            print(num1, "/", num2, " = ", division(num1, num2))
        except ZeroDivisionError:
            print("!!Error, no se puede dividir entre 0!!")
        else:
            pass

    #verificación para correr una operación nueva en la calculadora, si selecciona no termina la calculadora
    otra = input("Desea realizar otra operación? S/N: ")

    if (otra == "S" or
            otra == "s"):
        start()
    else:
        print("Gracias por usar la Calculadora de LaBotines, hasta luego!!")
        exit()


start()
