
catalogo_jugadores = {
    "Messi": {"equipo": "Inter Miami", "posicion": "delantero", "goles": 894},
    "Cristiano Ronaldo": {"equipo": "Al-Nassr", "posicion": "delantero", "goles": 950},
}



def agregar_jugador():
    nombre = input("Nombre del jugador: ")
    equipo = input("Equipo: ")
    posicion = input("Posicion: ")
    goles = int(input("Goles: "))
   
    catalogo_jugadores[nombre] = {"equipo": equipo, "posicion": posicion, "goles": goles}
    print("Se agrego a", nombre, "al catalogo!")


# Funcion para ver todos los jugadores con sus atributos
def ver_jugadores():
    print("\n--- TODOS LOS JUGADORES ---")
    if len(catalogo_jugadores) == 0:
        print("El catalogo esta vacio")
    # recorremos el diccionario con .items() para tener la llave y el valor
    for nombre, datos in catalogo_jugadores.items():
        print(nombre)
        print("   Equipo:", datos["equipo"])
        print("   Posicion:", datos["posicion"])
        print("   Goles:", datos["goles"])


# Funcion para modificar un atributo de un jugador que ya existe
def modificar_jugador():
    nombre = input("Nombre del jugador a modificar: ")
    # primero revisamos que el jugador si exista en el catalogo
    if nombre in catalogo_jugadores:
        atributo = input("Que atributo quiere cambiar? (equipo / posicion / goles): ")
        if atributo in catalogo_jugadores[nombre]:
            nuevo_valor = input("Nuevo valor: ")
            # los goles son un numero, entonces hay que convertirlo
            if atributo == "goles":
                nuevo_valor = int(nuevo_valor)
            catalogo_jugadores[nombre][atributo] = nuevo_valor
            print("Se cambio el atributo", atributo, "de", nombre)
        else:
            print("Ese atributo no existe")
    else:
        print("Ese jugador no esta en el catalogo")



opcion = ""
while opcion != "4":
    print("\n===== CATALOGO DE JUGADORES DE FUTBOL =====")
    print("1. Ver todos los jugadores")
    print("2. Agregar un jugador")
    print("3. Modificar un jugador")
    print("4. Salir")
    opcion = input("Elija una opcion: ")

    if opcion == "1":
        ver_jugadores()
    elif opcion == "2":
        agregar_jugador()
    elif opcion == "3":
        modificar_jugador()
    elif opcion == "4":
        print("Adios!")
    else:
        print("Opcion no valida, intente de nuevo")
 