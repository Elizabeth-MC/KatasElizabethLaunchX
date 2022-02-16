"""
Hola esta es mi KATA 9
Uso de funciones en Python
Ejercicio 1
Trabajar con argumentos
"""
# Función que necesite tres lecturas de combustible
# Función para leer 3 tanques de combustible y muestre el promedio

def report (tanque1, tanque2, tanque3):
    prom = (tanque1+tanque2+tanque3)/3
    return f"""
    El tanque uno esta al {tanque1} %  de nivel
    El tanque dos esta al {tanque2} %  de nivel
    El tanque tres esta al {tanque3} %  de nivel
    Por lo que el promedio de los tanques es {prom}%
    """

# Llamamos a la función que genera el reporte print(funcion(tanque1, tanque2, tanque3))
print('El promedio de los tanques es:', report(80,80,80))

# Función promedio para que el promedio se pueda hacer de forma independiente

def CalculoPromedio(Tanques):
    suma=sum(Tanques)
    NumTanques=len(Tanques)
    return suma/NumTanques

# Actualizarr la función de informes para llamar a la nueva función del promedio


def report (tanque1, tanque2, tanque3):  # Ncesita llevar corchetes para poder almacenar en tanques los valores asigandos
    return f"""
    El tanque uno esta al {tanque1} %  de nivel
    El tanque dos esta al {tanque2} %  de nivel
    El tanque tres esta al {tanque3} %  de nivel
    Por lo que el promedio de los tanques es {CalculoPromedio([tanque1,tanque2,tanque3])} 
    """

print(report(50,50,50))

# Ejercicio 2
# Trabajo con argumentos de palabra clave

"""Función con un informe preciso de la misión
   Considera hora de prelanzamiento, tiempo de vuelo, destino, tanque externo y tanque interno"""

def Mision (Prelanzamiento, Vuelo, Destino, ExTanq, InTanq):
    return f"""
    La mision estara dirigida a {Destino}
    Con un tiempo de vuelo de {Vuelo} hrs, con un pre lanzamiento de {Prelanzamiento} minutos
    Los tanques estan a una capacidad de : {ExTanq + InTanq} Lts
    """
print(Mision(10, 50, "Mars", 100, 800))

# Hazlo más flexible permitiendo cualquier número de pasos en el tiempo y cualquier número de tanques 
def Mision (Prelanzamiento, Vuelo, Destino, ExTanq, InTanq):
    return f"""
    La mision estara dirigida a {Destino}
    Con un tiempo de vuelo de {Vuelo} hrs, con un pre lanzamiento de {Prelanzamiento} minutos
    Los tanques estan a una capacidad de : {ExTanq + InTanq} Lts
    """
print(Mision(10, 50, "Mars", 100, 800)) 


def Mision(Destino, *Tiempo, **Tanques):
    Reporte = f"""
    La mision estara dirigida a {Destino}
    Con un tiempo de vuelo de: {sum(Tiempo)} minutos
    Los tanques estan a una capacidad de {sum(Tanques.values())}
    """
    return Reporte

print(Mision("Moon", 8, 11, 55, main=300000, external=200000))