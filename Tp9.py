'''Trabajo práctico nro. 9'''

#Ejercicio 1
class Person:
    def __init__(self, name=None, age=None, dni=None):
        self.__name = name
        self.__age = age
        self.__dni = dni

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("La edad no puede ser negativa.")

    def get_age(self):
        return self.__age

    def set_dni(self, dni):
        self.__dni = dni

    def get_dni(self):
        return self.__dni

    def show(self):
        print(f"Nombre: {self.__name}, Edad: {self.__age}, DNI: {self.__dni}")

    def hesOlder(self):
        return self.__age >= 18

person1 = Person("Pablo", 18, "46325466")

person1.show()

print(person1.hesOlder())

person1.set_age(17)  

person1.set_name("Pedro")

person1.show()

#Ejercicio 2
class Count:
    def __init__(self, headline=None, amount=0):
        self.__headline = headline
        self.__amount = amount

    def set_titular(self, headline):
        self.__headline = headline

    def get_headline(self):
        return self.__headline

    def set_amount(self, amount):
        self.__amount = amount

    def get_amount(self):
        return self.__amount

    def show(self):
        print(f"Titular: {self.__headline.get_name()}, Cantidad: {self.__amount}")

    def getInto(self, amount):
        if amount > 0:
            self.__amount += amount

    def withdraw(self, amount):
        self.__amount -= amount

person = Person("Pablo", 18, "46325466")

count = Count(person, 1000)

count.show()

count.getInto(500)

count.show()

count.withdraw(200)

count.show()

#Ejercicio 3
class Triangle:
    def __init__(self, side1,side2,side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def long_side(self):
        return max(self.side1, self.side2, self.side3)

    def triangle_type(self):
        if self.side1 == self.side2 == self.side3:
            return "Equilátero"
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return "Isósceles"
        else:
            return "Escaleno"

side1 = float(input("Ingrese el primer lado del triángulo: "))
side2 = float(input("Ingrese el segundo lado del triángulo: "))
side3 = float(input("Ingrese el tercer lado del triángulo: "))

triangle = Triangle(side1, side2, side3)

print(f"El lado con tamaño mayor es: {triangle.long_side()}")

print(f"El triángulo es de tipo: {triangle.triangle_type()}")

#Ejercicio 4
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class Diary:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def show_contacts(self):
        for contact in self.contacts:
            print(f"Nombre: {contact.name}, Teléfono: {contact.phone}, Email: {contact.email}")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print(f"Nombre: {contact.name}, Teléfono: {contact.phone}, Email: {contact.email}")
                return
        print(f"No se encontró ningún contacto con el nombre {name}")

    def edit_contact(self, name, new_phone, new_email):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone = new_phone
                contact.email = new_email
                print("Contacto editado correctamente.")
                return
        print(f"No se encontró ningún contacto con el nombre {name}")

    def menu(self):
        while True:
            print("\n--- Menú de Agenda ---")
            print("1. Añadir contacto")
            print("2. Lista de contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")

            option = input("Ingrese el número de la opción que desea ejecutar: ")

            if option == '1':
                name = input("Ingrese el nombre del contacto: ")
                phone = input("Ingrese el teléfono del contacto: ")
                email = input("Ingrese el email del contacto: ")
                new_contact = Contact(name, phone, email)
                self.add_contact(new_contact)

            elif option == '2':
                self.show_contacts()

            elif option == '3':
                name = input("Ingrese el nombre del contacto que desea buscar: ")
                self.search_contact(name)

            elif option == '4':
                name = input("Ingrese el nombre del contacto que desea editar: ")
                new_phone = input("Ingrese el nuevo teléfono del contacto: ")
                new_email = input("Ingrese el nuevo email del contacto: ")
                self.edit_contact(name, new_phone, new_email)

            elif option == '5':
                print("Agenda cerrada. ¡Hasta luego!")
                break

            else:
                print("Opción no válida. Por favor, ingrese un número del 1 al 5.")

diary = Diary()
diary.menu()