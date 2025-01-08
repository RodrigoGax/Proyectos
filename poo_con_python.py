class Personaje:
    #Atributos de la clase 
    nombre = 'Default'
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0
    #Indicar que no se haga nada en este momento
    pass
#Variable del constructor vacío de la clase
mi_personaje = Personaje()
mi_personaje.nombre = "ChemaFighter"
mi_personaje.fuerza = 30
mi_personaje.inteligencia = 12
mi_personaje.defensa = 28
mi_personaje.vida = 3
print("El nombre del personaje es ",mi_personaje.nombre)
print("La fuerza del personaje es ",mi_personaje.fuerza)
print("La inteligencia del personaje es ",mi_personaje.inteligencia)
print("La defensa del personaje es ",mi_personaje.defensa)
print("La vida del personaje es ",mi_personaje.vida)