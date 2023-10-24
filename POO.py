'''EJERCICIOS CLASES Y OBJETOS'''

class motorcycle:
    new = True
    motor = False
    def __init__(self,color=" ",tuition=0,fuel_liters=0,
    number_of_wheels=0,brand="",model="",fabricatcion_date=0,top_speed=0,
    weight=0,motor = False) -> None:
        self.color = color
        self.tuition = tuition
        self.number_of_wheels = number_of_wheels
        self.brand = brand
        self.model = model
        self.fabrication_date = fabricatcion_date
        self.top_speed = top_speed
        self.weight = weight
    
    def start_up(self):
        if not self.motor:
            self.motor = True
            print("El motor ha arrancado")
        else:
            print("El motor ya estaba en marcha")
    
    def stop(self):
        if self.motor:
            self.motor = False
            print("El motor se ha detenido")
        else:
            print("El motor ya estaba detenido")
    
    def check_price(cls):
        return cls.price

moto1 = motorcycle(color="Rojo",tuition="htn123",fuel_liters=15,
    number_of_wheels=2,brand="Honda",model="TRK 251",fabricatcion_date=16032020,
    top_speed=300,weight=175)

moto1.start_up()
moto1.stop()

motorcycle.price = 800000

print(f"El precio de la motocicleta {moto1.brand} {moto1.model} es  de {motorcycle.price}$")

price_moto1 = moto1.check_price()

moto2 = motorcycle(color="Blanco",tuition="abc160",fuel_liters=10,
    number_of_wheels=2,brand="Honda",model="CBR",fabricatcion_date=24102023,
    top_speed=250,weight=200)

moto2.start_up()
moto2.stop()

motorcycle.price = 500000

print(f"El precio de la motocicleta {moto2.brand} {moto2.model} es  de {motorcycle.price}$")

price_moto2 = moto2.check_price()