from Clientes import Cliente


def menu_principal():
    print("Menú Principal\n")
    print("1. Ingresar")
    print("2. ¿Es cliente nuevo?")
    print("3. Salir\n\n")

    opcion = input("Ingrese la opción deseada: ")

    if opcion == "1":
        print("Ingresar\n\n\n")
        email_ingresado = input("Ingrese su nombre de email: ")
        contraseña_ingresada = input("Ingrese su contraseña: ")
        cliente = Cliente("", email_ingresado, contraseña_ingresada, "")
        cliente.login(email_ingresado, contraseña_ingresada)
        return email_ingresado, contraseña_ingresada

    elif opcion == "2":
        print("Registro de cliente\n\n\n")
        nombre = input("Ingrese su nombre: ")
        email = input("Ingrese su mail: ")
        contraseña = input("Ingrese su contraseña: ")
        direccion = input("Ingrese su dirección: ")
        cliente = Cliente(nombre, email, contraseña, direccion)
        cliente.guardar_en_archivo()

    elif opcion == "3":
        exit()

    else:
        print("Opción inválida...\n\n\n")


def menu_de_clientes(email, contraseña):
    print("Menú de clientes\n\n")
    print("1. Ver información de cliente")
    print("2. Volver al menú principal")
    print("3. Salir\n\n")

    opcion = input("Ingrese la opción deseada: ")

    if opcion == "1":
        print("\nInformación de cliente:\n")
        cliente = Cliente("", email, contraseña, "")
        cliente.ver_info(email, contraseña)

    elif opcion == "2":
        print("Volver al menú principal: ")
        menu_principal()

    elif opcion == "3":
        exit()

    else:
        print("Opción inválida")


if __name__ == "__main__":
    while True:
        email_ingresado, contraseña_ingresada = menu_principal()
        menu_de_clientes(email_ingresado, contraseña_ingresada)
