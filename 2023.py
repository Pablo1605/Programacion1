#Vamos a llenar un tanquecito de agua jaja
print("Hola Usuario!")
print("Vamos a llenar un tanque con agua!")
print("Que capacidad quiere que el tanque tenga?")
#Aca se asigna la capacidad del tanque
tankcapacity=float(input())
print("El tanque de agua tiene una capacidad de", tankcapacity ,"ml")
choice="si"
waterintank=0
if choice=="si":
    while choice.lower()=="si":
        print("Ingrese la cantidad de ml que quiere vertir en el tanque")
        waterdeposit=float(input())
        print("Llenando...")
        for z in range(int(waterintank), int((waterintank+waterdeposit+10)), 10):
            print(z)
        print("Agua vertida con exito!")
        waterintank=waterdeposit+waterintank
        if waterintank==tankcapacity:
            print("Ha llenado la capacidad del tanque!")
            break
        elif waterintank>tankcapacity:
            print("El tanque se lleno y se rebalzo, hay", (waterintank-tankcapacity), "ml sobrantes!")
            break
        print("Quiere seguir?")
        choice=input()
        if choice.lower()!="no" and choice.lower()!="si":
            while choice.lower()!="no" and choice.lower()!="si":
                print("Respuesta invalida, solo se acepta si, o no\n"
                    "Ingrese nuevamente su eleccion")
                choice=input()
    if waterintank>=tankcapacity:
        print("El tanque tiene", waterintank, "ml de agua!")
    else:
        print("El tanque de agua tiene", waterintank, "ml")
elif choice.lower()!="no" and choice.lower()!="si":
        print("Respuesta invalida, ingrese nuevamente los ml")
        while choice.lower()=="si":
            print("Ingrese la cantidad de ml que quiere vertir en el tanque")
            waterdeposit=float(input())
            print("Llenando...")
            for z in range(int(waterintank), int((waterintank+waterdeposit+10)), 10):
                print(z)
            print("Agua vertida con exito!")
            waterintank=waterdeposit+waterintank
            if waterintank==tankcapacity:
                print("Ha llenado la capacidad del tanque!")
                break
            elif waterintank>tankcapacity:
                print("El tanque se lleno y se rebalzo, hay", (waterintank-tankcapacity), "ml sobrantes!")
                break
        print("Quiere seguir?")
        choice=input()
        if choice.lower()!="no" and choice.lower()!="si":
            while choice.lower()!="no" and choice.lower()!="si":
                print("Respuesta invalida, solo se acepta si, o no\n"
                    "Ingrese nuevamente su eleccion")
                choice=input()
        if waterintank>=tankcapacity:
            print("El tanque tiene", waterintank, "ml de agua!")
        else:
            print("El tanque de agua tiene", waterintank, "ml")