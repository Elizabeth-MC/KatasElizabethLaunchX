"""    Hola esta es mi KATA 6
        Ejercicio 1
        Crear y usar listas de Python"""

# Crear lista 

Planetas = ['Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno', 'Uranuno', 'Neptuno']
print(Planetas)

#Agregar un planeta a la lista

Planetas.append('Pluton')
print(Planetas)

# Mostrar el ultimo elemento

print('El ultimo planeta es: ',Planetas[-1])

""" Ejercicio 2
    Trabajando con datos de una lista"""
# Solicitamos al usuario el nombre de un planeta

AgregarPlaneta=input('Ingresa un planeta con la primer letra en mayuscula: ')
BuscarPlaneta=Planetas.index(AgregarPlaneta)
print('El planeta '+ AgregarPlaneta +' es el numero ', BuscarPlaneta +1,' del sistema solar')

# Mostrar los Planetas más cercanos

print('Los planetas más cercanos al sol que'+ AgregarPlaneta +'son: ')
print(Planetas[0:BuscarPlaneta])

# Mostrar los Planetas más lejanos

print('Los planetas más lejanos del sol que'+ AgregarPlaneta +'son: ')
# Mostar uno despues del planeta hasta el final
print(Planetas[BuscarPlaneta+1:])