"""Hola esta es mi  KATA 8
   Ejercicio 1
   Creacion de diccionarios"""

# Crear y modificar un diccionario 

planet = {
    'name': 'Mars', # Las claves antes de los ':' son cadenas
    'moons': 2      # Los valores despues de ':' pueden ser cualquier tipos de datos
}

# Muestra el nombre del planeta y el numero de lunas

print(f'{planet["name"]} has {planet["moons"]} moons')

# Agrega la clave circunferencia con los datos proporcionados previamente

planet['circumference'] = { # La clave de circunferencia se agrega como una tercera clave
    'polar': 6752,          # La clave polar es 
    'equatorial': 6792      # La clave equatorial es 
}

print(planet)
print(f'{planet["name"]} has a polar circumference of {planet["circumference"]["polar"]}')

print(planet['circumference'])

"""Ejercicio 2
   Programación dinámica con diccionarios"""

# Planets and moons

planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

# Almacenar el número de lunas

moons = planet_moons.values()           #  Moon contendra los siguientes valores = 0, 0, 1, 2, 79, 82, 27, 14, 5, 2, 1, 1
print('Las lunas son: ', moons)          # Imprime solo el numero de lunas

# Almacenar el número de planetas

planets = len(planet_moons.keys())
print('Los planetas son : ', planets)  

# Sumar las lunas

TotalMoons = 0

for moon in moons:
    TotalMoons = TotalMoons + moon
print(f'El total de lunas son: {TotalMoons}')

# Calcula el promedio de lunas
Prom = TotalMoons / planets

# Muestra el promedio
print(f'El promedio de lunas es: {Prom}')