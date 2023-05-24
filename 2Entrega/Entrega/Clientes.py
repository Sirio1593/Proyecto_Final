import json
import os

class Cliente:
    # Diccionario para almacenar todos los clientes
    datos_clientes = {}

    def __init__(self, nombre, email, contraseña, direccion):
        self.nombre = nombre
        self.email = email
        self.contraseña = contraseña
        self.direccion = direccion
        
        # Agrega la instancia actual al diccionario de clientes
        Cliente.datos_clientes[self.email] = self

    def guardar_en_archivo(self):
        ruta = "datos_clientes.json"
        datos_clientes = {
            self.email: {
                "nombre": self.nombre,
                "email": self.email,
                "contraseña": self.contraseña,
                "direccion": self.direccion,
            }
        }

        try:
            with open(ruta, "r") as archivo:
                existing_data = json.load(archivo)
        except FileNotFoundError:
            existing_data = {}

        existing_data.update(datos_clientes)

        with open(ruta, "w") as archivo:
            json.dump(existing_data, archivo, indent=4)
        
        print("\n---------------------------------------------------\n")
        print(f"El cliente {self.nombre} ha sido guardado en el archivo {ruta} con éxito.")
        print("\n---------------------------------------------------\n")

    @staticmethod
    def login(email, contraseña):
        from menu import menu_de_clientes
        ruta = "datos_clientes.json"
        with open(ruta, "r") as archivo:
            datos_clientes = json.load(archivo)

        if email in datos_clientes:
            if datos_clientes[email]["contraseña"] == contraseña:
                print("Inicio de sesión exitoso.")
                # Realiza las acciones necesarias después de iniciar sesión
                menu_de_clientes(email, contraseña)  # Llamada a la función menu_de_clientes del menú de clientes
            else:
                print("Contraseña incorrecta.")
        else:
            print("No se pudo iniciar sesión. El usuario no existe en el registro.")
            
    @staticmethod
    def ver_info(email, contraseña):
        from menu import menu_de_clientes
        ruta = "datos_clientes.json"
        with open(ruta, "r") as archivo:
            datos_clientes = json.load(archivo)

        if email in datos_clientes:
            if datos_clientes[email]["contraseña"] == contraseña:
                print("Inicio de sesión exitoso.")
                # Muestra la información del cliente
                cliente = datos_clientes[email]
                print("Información del cliente:")
                print(f"Nombre: {cliente['nombre']}")
                print(f"Email: {cliente['email']}")
                print(f"Dirección: {cliente['direccion']}")
                
                # Ofrece la opción de volver al menú de clientes
                opcion = input("Presione 'v' para volver al menú de clientes o cualquier otra tecla para salir: ")
                if opcion.lower() == "v":
                    menu_de_clientes(email, contraseña)
            else:
                print("Contraseña incorrecta.")
        else:
            print("No se pudo iniciar sesión. El usuario no existe en el registro.")
