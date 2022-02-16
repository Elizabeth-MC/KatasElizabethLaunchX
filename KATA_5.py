# Hola esta es mi KATA 5
# Ejercicio1 
# Utilizar operadores aritméticos
# Programa para calcular la distancia entre dos planetas

#Definir variables

Tierra = 149597870 #Km
Jupiter= 778547200 #Km

#Calcular la diferencia

Distancia= Jupiter-Tierra
print('Distancia= ',Distancia)
print('Distancia en millas=', round(Distancia*0.621))

# Ejercicio 2 
# Convierte cadenas en números y usa valores absolutos
# Aplicación para trabajar con números y entrada de usuario

print('\nDIME EL NOMBRE DE LOS PLANETAS')
Planeta1=int(input('Introduce la distancia al sol del Planeta1: '))
Planeta2=int(input('Introduce la distancia al sol del Planeta2: '))

DistanciaPlanetas=Planeta2-Planeta1

print('La distancia entre los planetas es de ',abs(DistanciaPlanetas),'Km')
print('La distancia entre los planetas es de ',round(DistanciaPlanetas*0.621),'millas')