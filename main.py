# Función que suma todos los elementos de una lista.
# Si la lista está vacía, devuelve 0.
def addmultiplenumbers(lista):
    if not lista:
        return 0
    return sum(lista)


# Función que multiplica todos los elementos de una lista.
# Si la lista está vacía, devuelve 1 (identidad multiplicativa).
def multiplymultiplenumbers(lista):
    if not lista:
        return 1
    result = 1
    for num in lista:
        result *= num
    return result


# Función que verifica si un número es par.
# Utiliza la fucnción isitaninteger para validar primero si el número es entero, y luego verificar si es par
def isiteven(numero):
    return isitaninteger(numero) and numero % 2 == 0


# Función que verifica si un número es entero.
# Acepta tanto enteros como flotantes sin decimales (ej. 3.0).
def isitaninteger(numero):
    return isinstance(numero, int) or (
        isinstance(numero, float) and numero.is_integer()
    )


# Función principal que interactúa con el usuario.
# Permite elegir entre suma, multiplicación, verificacion de paridad o entero.
def main():
    print("Bienvenido a la Calculadora Mejorada ")
    print(
        "Opciones: \n"
        "1- Suma lista de números\n"
        "2- Multiplicación lista de números\n"
        "3- Verificar si el número es par \n"
        "4- Verificar si el número es entero\n"
    )

    # Solicita al usuario la operación deseada
    opcion = input("¿Qué operación deseas realizar? ")

    # Si la opción es suma o multiplicación, pide una lista de números
    if opcion in ["1", "2"]:
        entrada = input("Introduce los números separados por coma: ")
        lista = [float(x) for x in entrada.split(",") if x.strip()]
        if opcion == "1":
            print("Resultado:", addmultiplenumbers(lista))
        else:
            print("Resultado:", multiplymultiplenumbers(lista))

    # Si la opción es paridad, pide un número y verifica si es par
    elif opcion == "3":
        numero = float(input("Introduce un número: "))
        print("¿Es par?", isiteven(numero))

    # Si la opción es entero, verifica si el número ingresado es entero
    elif opcion == "4":
        numero = float(input("Introduce un número: "))
        print("¿Es entero?", isitaninteger(numero))

    # Si la opción no es válida, muestra un mensaje de error
    else:
        print("Opción no válida.")


if __name__ == "__main__":
    main()
