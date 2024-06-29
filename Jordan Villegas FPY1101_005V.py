
import json
from datetime import datetime   

pizzas = [
    ["ID pizza","Tipo de pizza", "Tamaño", "Precio"],
    [1, "Margarita", "Pequeña", 5500],
    [2, "Margarita", "Mediana", 8500],
    [3, "Margarita", "Familia", 11000],
    [4, "Mexicana", "Pequeña", 7000],
    [5, "Mexicana", "Mediana", 10000],
    [6, "Mexicana", "Familiar", 13000],
    [7, "Barbacoa", "Pequeña", 6500],
    [8, "Barbacoa", "Mediana", 9500],
    [9, "Barbacoa", "Familiar", 12500],
    [10, "Vegetariana", "Pequeña", 5000],
    [11, "Vegetariana", "Mediana", 8000],
    [12, "Vegetariana", "Familiar", 10500],
]

ventas_registradas = []

def menu():
    
    print("   Bienvenido a PIZZAS DUOC.")
    print("1. Registrar una venta.")
    print("2. Mostrar todas las ventas.")
    print("3. Buscar ventas por cliente.")
    print("4. Guardas las ventas en un archivo.")
    print("5. Cargar las ventas desde un archivo.")
    print("6. Generar boleta.")
    print("7. Anular venta.")
    print("8. Salir del programa")
    
    choice = int(input("    Ingrese una opcion: "))
    
    return choice

def datos_pizzas():
#esto es un bucle que recorre todo lo guardado en pizzas
    print("Seleccione una Pizza:    ")

    for row in pizzas:
        print(row,"     ")

    id_pizza = int(input("Ingrese el ID de la pizza que desea comprar: "))

    pizza_finded = None

    for pizza in pizzas[1:]:

        if pizza[0] == id_pizza:
            pizza_finded = pizza
            break
        
    if pizza_finded:

        tipo_pizza = pizza_finded[1]
        tamaño_pizza = pizza_finded[2]
        precio_pizza = pizza_finded[3]
         
        return tipo_pizza, tamaño_pizza, precio_pizza
    
    else:

        print("Pizza no encontrada.")
        return None, None, None, None


def registrar_venta():
    
    rut = input("Ingrese su RUT: ")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    tipo_cliente = ""

    print("   Ingrese el tipo de cliente.")
    print("1. diurno.")
    print("2. vespertino.")
    print("3. administrativo.")
    
    while True:

        try:

            opcion = int(input("    Ingrese una opción: "))

            if opcion == 1:

                tipo_cliente = "diurno"
                break
            elif opcion == 2:

                tipo_cliente = "vespertino"
                break
            elif opcion == 3:

                tipo_cliente = "administrativo"
                break

            else: print("Ingrese una opción válida.")

        except ValueError:
            print("Ingrese una opción válida.")

    tipo_pizza, tamaño_pizza, precio_pizza = datos_pizzas()

    if tipo_pizza:

        datos_venta = {
            "RUT": rut,
            "Nombre": nombre,
            "Apellido": apellido,
            "Tipo cliente": tipo_cliente,
            "Tipo Pizza": tipo_pizza,
            "Tamaño Pizza": tamaño_pizza,
            "Precio Pizza": precio_pizza
        }

        ventas_registradas.append(datos_venta)

        print("     Venta registrada correctamente:")
        for key, value in datos_venta.items():
            print(f"{key}: {value}")

        return datos_venta
    
    else:

        print("     Pizza no encontrada. Venta no registrada.")
        return None
    
#esto hace que se aplique un bucle en todas las ventas registradas

def visualizar_ventas():
    if not ventas_registradas:
        print("No hay pedidos registrados, ingrese uno.")
    else:
        for rows in ventas_registradas:
            print(rows)
        

def exportar_ventas(nombre_archivo):

    with open(nombre_archivo, 'w') as file:
        json.dump(ventas_registradas, file, indent=4)

def buscar_ventas_por_rut(rut):
    
    encontradas = False
    
    for venta in ventas_registradas:
        
        if venta["RUT"] == rut:
            
            encontradas = True
            print("     Venta encontrada:")
            
            for key, value in venta.items():
                print(f"{key}: {value}")
                
    if not encontradas:
        print("     No se encontraron ventas para el RUT proporcionado.")

def cargar_ventas(nombre_archivo):
    
    global ventas_registradas
    
    try:
        
        with open(nombre_archivo, 'r') as file:
            
            ventas_registradas = json.load(file)
            print(f"        Datos de ventas cargados correctamente desde {nombre_archivo}.")
            
    except FileNotFoundError:
        
        print(f"    El archivo {nombre_archivo} no existe.")

def generar_factura(datos_ventas):
    
    print("     ************* FACTURA GENERADA *************")
    print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("==================================")
    print(f"Nombre Cliente: {datos_ventas[0]['Nombre']} {datos_ventas[0]['Apellido']}")
    print(f"RUT Cliente: {datos_ventas[0]['RUT']}")
    print(f"Tipo Cliente: {datos_ventas[0]['Tipo cliente'].capitalize()}")
    print("----------- Detalles de Ventas -----------")
    
    total_sin_descuento = 0
    total_con_descuento = 0
    
    for datos_venta in datos_ventas:
        precio_pizza = datos_venta['Precio Pizza']
        
        tipo_cliente = datos_venta['Tipo cliente']
        if tipo_cliente == 'diurno':
            descuento = 0.15  
        elif tipo_cliente == 'vespertino':
            descuento = 0.18  
        elif tipo_cliente == 'administrativo':
            descuento = 0.11  
        else:
            descuento = 0  
        
        precio_con_descuento = precio_pizza * (1 - descuento)
        

        total_sin_descuento += precio_pizza
        total_con_descuento += precio_con_descuento

        print(f"Tipo pizza: {datos_venta['Tipo Pizza']}")
        print(f"Tamaño pizza: {datos_venta['Tamaño Pizza']}")
        print(f"Precio pizza: ${precio_pizza}")
        print(f"Descuento aplicado: {descuento * 100}%")
        print(f"Precio con descuento: ${precio_con_descuento:.2f}")
        print("----------------------------------")
    

    print("==================================")
    print(f"Total sin descuento: ${total_sin_descuento:.2f}")
    print(f"Total con descuento: ${total_con_descuento:.2f}")
    print("==================================")
    print("Gracias por preferirnos!")
    print("**********************************\n")

def anular_venta():
    rut_buscar = input("Ingrese el RUT del cliente para anular la venta: ")
    venta_encontrada = False

    for i, venta in enumerate(ventas_registradas):
        if venta["RUT"] == rut_buscar:
            print(f"Anulando venta para {venta['Nombre']} {venta['Apellido']}.")
            del ventas_registradas[i]
            venta_encontrada = True
            print("Venta anulada correctamente.")
            break
    
    if not venta_encontrada:
        print("No se encontraron ventas para el RUT proporcionado.")


while True:

    opcion = menu()

    if opcion == 1:
        registrar_venta()

    elif opcion == 2:
        visualizar_ventas()
    
    elif opcion == 3:

        rut_buscar = input("    Ingrese el RUT del cliente: ")
        buscar_ventas_por_rut(rut_buscar)

    elif opcion == 4:

        nombre_archivo = input("Indique nombre del archivo: ")

        exportar_ventas(nombre_archivo)

        print(f"    Datos de ventas exportados correctamente a {nombre_archivo}.")

    elif opcion == 5:
        nombre_archivo = input("Nombre del archivo que desea cargar: ")
        cargar_ventas(nombre_archivo)

    elif opcion == 6:
        rut_buscar = input("     Ingrese el RUT del cliente: ")
        ventas_cliente = []

        for venta in ventas_registradas:
            if venta["RUT"] == rut_buscar:
                ventas_cliente.append(venta)
        
        if ventas_cliente:
            generar_factura(ventas_cliente)
        else:
            print("     No se encontraron ventas para el RUT escrito.")
    elif opcion == 7:
        anular_venta()
         
        
    elif opcion == 8:

        print("Saliendo...")
        break

    else: print("Ingrese una opcion valida.")

    
    

