""""
    Hola
    Esta es mi KATA 7 
    Ejercicio 1
    Creacion de un bucle WHILE
"""

# Definir variables

new_planet=''
planets=[]

print('Escribe lo planetas a añadir, cuando los tendas escribe *done* para terminar ')

while new_planet != 'done':

    if new_planet: # solo gusarda el valor mientra la sentencia se siga cumpliendo
        planets.append(new_planet)
        
    new_planet= input('Planeta: ') # pregunta por los planetas en un ciclo y estos se asignan a la variable new_planet

print('Los planetas son: \n', planets)

"""Ejercicio 1
    Creacion de un bucle WHILE"""

for planet in planets:
    print( ' Los planetas son:' , planet) 