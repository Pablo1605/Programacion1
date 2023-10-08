'''Ejercicios en clase - Variables dimensionadas'''

#Ejercicio 1
def add_passenger():
    name = input("Ingrese el nombre del pasajero: ")
    dni = int(input("Ingrese el DNI del pasajero: "))
    destiny = input("Ingrese el destino del pasajero: ")
    travelers.append((name, dni, destiny))

def add_city():
    city = input("Ingrese el nombre de la ciudad: ")
    country = input("Ingrese el nombre del país: ")
    cities.append((city, country))

def city_by_dni():
    dni = int(input("Ingrese el DNI del pasajero: "))
    for name, num_dni, destiny in travelers:
        if num_dni == dni:
            for city, country in cities:
                if destiny == city:
                    print(f"El pasajero {name} viaja a {city}, {country}")
                    return
    print("No se encontró un pasajero con ese DNI o no se encontró la ciudad de destino.")

def count_passengers_by_city():
    city = input("Ingrese el nombre de la ciudad: ")
    counter = 0
    for _, _, destiny in travelers:
        if destiny == city:
            counter += 1
    print(f"La cantidad de pasajeros que viajan a {city} es: {counter}")

def country_by_dni():
    dni = int(input("Ingrese el DNI del pasajero: "))
    for name, num_dni, destiny in travelers:
        if num_dni == dni:
            for _, country in cities:
                if destiny == _:
                    print(f"El pasajero {name} viaja a {country}")
                    return
    print("No se encontró un pasajero con ese DNI o no se encontró la ciudad de destino.")

def count_passengers_by_country():
    country = input("Ingrese el nombre del país: ")
    counter = 0
    for _, p in cities:
        if p == country:
            for _, _, destiny in travelers:
                if destiny == _:
                    counter += 1
    print(f"La cantidad de pasajeros que viajan a {country} es: {counter}")

travelers = []
cities = []
while True:
    print("\n1. Agregar pasajeros a la lista de viajeros")
    print("2. Agregar ciudades a la lista de ciudades")
    print("3. Ver el DNI de un pasajero,ver a qué ciudad viaja")
    print("4. Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad")
    print("5. Dado el DNI de un pasajero, ver a que ciudad viaja")
    print("6. Dado un país, mostra cuántos pasajeros viajan a ese país")
    print("7. Salir del programa")
    
    option = int(input("\nElija una opción: "))
    
    if option == 1:
        add_passenger()
    elif option == 2:
        add_city()
    elif option == 3:
        city_by_dni()
    elif option == 4:
        count_passengers_by_city()
    elif option == 5:
        country_by_dni()
    elif option == 6:
        count_passengers_by_country()
    elif option == 7:
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")

#Ejercicio 2
def obtain_unique_addresses(shopping):
    addresses = set()
    for buys in shopping:
        _, _, _, domicilie = buys
        addresses.add(domicilie)
    return list(addresses)

shopping = []
while True:
    customer = input("Ingrese el nombre del cliente, o deje vacio para terminar: ")
    if not customer:
        break

    day = int(input("Ingrese el día del mes: "))
    amount = float(input("Ingrese el monto de la compra: "))
    domicile = input("Ingrese el domicilio del cliente: ")

    shopping.append((customer, day, amount, domicile))

unique_addresses = obtain_unique_addresses(shopping)

print("Domicilios únicos a los que se debe enviar factura:")
for domicile in unique_addresses:
    print(domicile)

#Ejercicio 3
def load_partner():
    num = int(input("Ingrese el número de socio: "))
    name = input("Ingrese el nombre del socio: ")
    last_name = input("Ingrese el apellido del socio: ")
    income = input("Ingrese la fecha de ingreso (ddmmaaaa): ")
    quota_per_day = input("¿Cuota al día? (s/n): ").lower() == 's'
    partners[num] = {"nombre": name + " " + last_name, "ingreso": income, "cuota_al_dia": quota_per_day}

def number_of_partners():
    print(f"La cantidad de socios es: {len(partners)}")

def pay_dues():
    num = int(input("Ingrese el número de socio que ha pagado las cuotas adeudadas: "))
    if num in partners:
        partners[num]["cuota_al_dia"] = True
        print(f"Se han registrado las cuotas pagadas para el socio n°{num}.")
    else:
        print(f"No se encontró un socio con el número {num}.")

def modify_date():
    for partners in partners.values():
        partners["ingreso"] = "14/03/2018"
    print("Se ha modificado la fecha de ingreso para todos los socios.")

def unsubscribe():
    name_lastName = input("Ingrese el nombre y apellido del socio a dar de baja (en el formato 'Nombre Apellido'): ")
    partner_to_delete = None
    for num, data in partners.items():
        if data["nombre"].lower() == name_lastName.lower():
            partner_to_delete = num
            break
    if partner_to_delete is not None:
        del partners[partner_to_delete]
        print(f"Se ha dado de baja al socio {name_lastName}.")
    else:
        print(f"No se encontró un socio con el nombre {name_lastName}.")

def print_partners():
    print("Listado de socios:")
    for num, data in partners.items():
        print(f"Socio n°{num}, {data['nombre']}, ingresó: {data['ingreso']}, {'cuota al día' if data['cuota_al_dia'] else 'cuota pendiente'}.")

partners = {
    1: {"nombre": "Amanda Núñez", "ingreso": "17/03/2009", "cuota_al_dia": True},
    2: {"nombre": "Bárbara Molina", "ingreso": "17/03/2009", "cuota_al_dia": True},
    3: {"nombre": "Lautaro Campos", "ingreso": "17/03/2009", "cuota_al_dia": True}
}
while True:
    print("\nMenu:")
    print("1. Cargar información de socios")
    print("2. Informar cantidad de socios")
    print("3. Registrar pago de cuotas")
    print("4. Modificar fecha de ingreso")
    print("5. Dar de baja a un socio")
    print("6. Imprimir listado de socios")
    print("7. Salir")
    
    option = input("Seleccione una opción (1-7): ")
    
    if option == '1':
        load_partner()
    elif option == '2':
        number_of_partners()
    elif option == '3':
        pay_dues()
    elif option == '4':
        modify_date()
    elif option == '5':
        unsubscribe()
    elif option == '6':
        print_partners()
    elif option == '7':
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción del 1 al 7")