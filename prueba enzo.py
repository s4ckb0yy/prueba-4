compradores_concepcion = []
compradores_puente = []
compradores_valpo = []
compradores_vina = []

stock_concepcion = 500
stock_puente = 1300
stock_valpo = 100
stock_vina = 50

def validar_codigo(codigo):
    tiene_mayus = any(c.isupper() for c in codigo)
    tiene_numero = any(c.isdigit() for c in codigo)
    no_espacios = " " not in codigo
    largo_correcto = len(codigo) >= 6
    return tiene_mayus and tiene_numero and no_espacios and largo_correcto

def comprar_conce():
    global stock_concepcion
    if stock_concepcion == 0:
        print("No hay stock de entradas disponible en concepción")
        return
    nombre = input("Ingresa tu nombre: ")
    if nombre in compradores_concepcion:
        print("Este nombre ya fue registrado anteriormente")
        return
    codigo = input("Ingrese el código para validar: ")
    if not validar_codigo(codigo):
        print("Código inválido")
        return
    compradores_concepcion.append(nombre)
    stock_concepcion -= 1
    print("Entrada registrada en concepción.")

def comprar_puente():
    global stock_puente
    if stock_puente == 0:
        print("No hay stock de entradas disponible en puente alto")
        return
    nombre = input("Ingresa tu nombre: ")
    if nombre in compradores_puente:
        print("Este nombre ya fue registrado anteriormente")
        return
    cantidad = int(input("¿Cuántas entradas deseas? Máximo 3: "))
    if cantidad < 1 or cantidad > 3:
        print("Cantidad no permitida, máximo 3")
        return
    if cantidad > stock_puente:
        print("No hay stock disponible")
        return
    compradores_puente.append(nombre)
    stock_puente -= cantidad
    print(f"{cantidad} entradas registradas en Puente Alto.")

def comprar_valpo():
    global stock_valpo
    if stock_valpo == 0:
        print("No hay stock de entradas disponible en Valparaíso")
        return
    nombre = input("Ingresa tu nombre: ")
    if nombre in compradores_valpo:
        print("Este nombre ya fue registrado anteriormente")
        return
    codigo = input("Ingrese el código de confirmación: ")
    if not validar_codigo(codigo):
        print("Código inválido")
        return
    compradores_valpo.append(nombre)
    stock_valpo -= 1
    print("Entrada tipo 'G' registrada en Valparaíso.")

def comprar_vina():
    global stock_vina
    if stock_vina == 0:
        print("No hay entradas disponibles en Viña del Mar.")
        return
    nombre = input("Ingrese su nombre: ")
    if nombre in compradores_vina:
        print("Nombre repetido.")
        return
    tipo = input("Ingrese tipo de entrada (Sun o Ni): ")
    if tipo != "Sun" and tipo != "Ni":
        print("Tipo de entrada inválido.")
        return
    compradores_vina.append(nombre)
    stock_vina -= 1
    print("Entrada registrada en Viña del Mar.")

def menu():
    print()
    print("TOTEM AUTOSERVICIO GIRA ROCK AND CHILE IN CHILE")
    print("1.- Comprar entrada a “los Fortificados” en Concepción.")
    print("2.- Comprar entrada a “los Fortificados” en Puente Alto.")
    print("3.- Comprar entrada a “los Fortificados” en Muelle Barón en Valparaíso.")
    print("4.- Comprar entrada a “los Fortificados” en Muelle Vergara en Viña del Mar.")
    print("5.- Salir.")

def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            comprar_conce()
        elif opcion == "2":
            comprar_puente()
        elif opcion == "3":
            comprar_valpo()
        elif opcion == "4":
            comprar_vina()
        elif opcion == "5":
            print("Programa finalizado")
            break
        else:
            print("Opción inválida")

main()
