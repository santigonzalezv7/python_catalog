
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



opcion = ""
while opcion != "4":
    print("\n===== CATALOGO DE JUGADORES DE FUTBOL =====")
    print("1. Ver todos los jugadores")
    print("2. Agregar un jugador")
    print("3. Modificar un jugador")
    print("4. Salir")
    opcion = input("Elija una opcion: ")

    if opcion == "1":
        print("Esta opcion todavia no esta lista")
    elif opcion == "2":
        agregar_jugador()
    elif opcion == "3":
        print("Esta opcion todavia no esta lista")
    elif opcion == "4":
        print("Adios!")
    else:
        print("Opcion no valida, intente de nuevo")
 