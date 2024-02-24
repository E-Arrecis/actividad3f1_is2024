class Persona:
    def __init__(self):
        """
        Constructor de la clase Persona

        Solicita al usuario los datos de la persona
        """
        self._nombre = input("Ingrese su nombre: ")
        self._apellidos = input("Ingrese sus apellidos: ")
        self._direccion = input("Ingrese su dirección: ")
        self._telefono = input("Ingrese su teléfono: ")
        self._fecha_nacimiento = input("Ingrese su fecha de nacimiento (YYYY-MM-DD): ")

    # Propiedades (getters y setters)

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def apellidos(self):
        return self._apellidos

    @apellidos.setter
    def apellidos(self, value):
        self._apellidos = value

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, value):
        self._direccion = value

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, value):
        self._telefono = value

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, value):
        self._fecha_nacimiento = value

    # Métodos

    def __str__(self):
        """
        Representación en cadena de la clase Persona

        Returns:
            str: Cadena con la información de la persona
        """
        return f"Persona: {self.nombre} {self.apellidos}\n" \
               f"Dirección: {self.direccion}\n" \
               f"Teléfono: {self.telefono}\n" \
               f"Fecha de nacimiento: {self.fecha_nacimiento}"

    def ver_informacion(self):
        """
        Muestra la información de la persona
        """
        print(self)

    def modificar_informacion(self):
        """
        Solicita al usuario la modificación de los datos de la persona
        """
        while True:
            opcion = input("¿Qué desea modificar?\n"
                           "1. Nombre\n"
                           "2. Apellidos\n"
                           "3. Dirección\n"
                           "4. Teléfono\n"
                           "5. Fecha de nacimiento\n"
                           "0. Salir\n"
                           "Ingrese su opción: ")
            if opcion == "0":
                break
            elif opcion == "1":
                self.nombre = input("Ingrese su nuevo nombre: ")
            elif opcion == "2":
                self.apellidos = input("Ingrese sus nuevos apellidos: ")
            elif opcion == "3":
                self.direccion = input("Ingrese su nueva dirección: ")
            elif opcion == "4":
                self.telefono = input("Ingrese su nuevo teléfono: ")
            elif opcion == "5":
                self.fecha_nacimiento = input("Ingrese su nueva fecha de nacimiento (YYYY-MM-DD): ")
            else:
                print("Opción inválida.")


# Ejemplo de uso

persona1 = Persona()

while True:
    opcion = input("¿Qué desea hacer?\n"
                   "1. Ver información\n"
                   "2. Modificar información\n"
                   "0. Salir\n"
                   "Ingrese su opción: ")
    if opcion == "0":
        break
    elif opcion == "1":
        persona1.ver_informacion()
    elif opcion == "2":
        persona1.modificar_informacion()
    else:
        print("Opción inválida.")