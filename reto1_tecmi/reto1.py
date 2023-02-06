import os
import time

print("Bienvenido al sistema de Toppings Heladeando")
time.sleep(3)
os.system('cls')
while True:
    
    print("BIENVENIDO AL MENÚ PRINCIPAL: \n\n 1. Inventario HELADEANDO \n 2. Agrega un nuevo topping \n 3. VER ALERTAS DE GRAMAJE \n 4. CERRAR PROGRAMA")
    menu = int(input("Selecciona algún submenú: "))

    match menu:
        case 1: 
                while True:
                    print("Bienvenido al Inventario HELADEANDO")
                    print("1. Chocolates")
                    print("2. Frutos Secos")
                    print("3. Líquidos o mermeladas")
                    print("4. A granel")
                    print("5. Salir")
                    num = int(input("Elija el tipo de topping que desea seleccionar: "))
                    match num:
                        case 1: 
                                print("Chocolates: ")
                                print("Chocolate Cobertura")
                                print("M&Ms")
                                print("Carlos V")
                                print("Krankys")
                                print("Ferrero Rocher")
                                time.sleep(3)
                        case 2: 
                                print("Frutos Secos: ")
                                print("Avellanas")
                                print("Nueces")
                                print("Pistachos")
                                print("Piñones")
                                print("Cacahuates")
                                time.sleep(3)
                        case 3: 
                                print("Líquidos o mermeladas: ")
                                print("Mermelada de fresa")
                                print("Mermelada de piña")
                                print("Mermelada de mango")
                                print("Chocolate Hershey's")
                                time.sleep(3)
                        case 4: 
                                print("A granel: ")
                                print("Amaranto")
                                print("Nuez molida")
                                print("Chocomilk en polvo")
                                time.sleep(3)
                        case 5: 
                                print("Espere un momento")
                                time.sleep(3)
                                break
                        case _:
                                print("Error, inténtelo de nuevo...")
                                time.sleep(3)
        case 2: 
                new_toppings_quantity = int(input("Ingresa la cantidad de toppings por agregar: "))
                lista_de_toppings = []
                for i in range(new_toppings_quantity):
                        topping = input(f"Dame el topping {i}: ")
                        lista_de_toppings.append(topping)

                print("Estos son los toppings que agregaste: ", lista_de_toppings)
                time.sleep(3)

        case 3: 
                print("Bienvenido al submenú \"Listas de gramaje\"")
                while True:
                        print("1. Chocolate \n 2. Fresa \n 3. Vainilla V \n 4. Carlos V \n 5. Salir")
                        num = int(input("Ingresa el código de topping que quieres verificar gramaje: "))
                        match num:
                                case 1:
                                        gram = int(input("Ingresa la cantidad de grmaos que tienes: "))
                                        if gram <= 200:
                                                print("Alerta: RELLENA EL TOPPING CHOCOLATE")
                                        else:
                                                print("Tienes suficientes gramos.")
                                        time.sleep(3)
                                case 2:
                                        gram = int(input("Ingresa la cantidad de grmaos que tienes: "))
                                        if gram <=200:
                                                print("Alerta: RELLENA EL TOPPING FRESA")
                                        else:
                                                print("Tienes suficientes gramos")
                                        time.sleep(3)
                                case 3:
                                        gram = int(input("Ingresa la cantidad de grmaos que tienes: "))
                                        if gram <= 200:
                                                print("Alerta: RELLENA EL TOPPING VAINILLA")
                                        else:
                                                print("Tienes suficientes gramos")
                                        time.sleep(3)
                                case 4:
                                        gram = int(input("Ingresa la cantidad de grmaos que tienes: "))
                                        if gram <= 200:
                                                print("Alerta: RELLENA EL TOPPING CARLOS V")
                                        else:
                                                print("Tienes suficientes gramos")
                                        time.sleep(3)
                                case 5:
                                        print("Espere un momento...")
                                        time.sleep(3)
                                        break
                                case _:
                                        print("Error, inténtelo de nuevo")
                                
        case 4: 
                print("HASTA LUEGO!")
                time.sleep(3)
                break