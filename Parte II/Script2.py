"""
Script 2: Funciones, importacion de librerias y concepto de clases
Autor: kevinrojas
"""

"""
Este archivo fue presentado mientrás se impartía el curso de python.
"""
# Una librería en programacion es un conjunto de elementos como datos,
# funciones, documentacion, archivos de ayuda, clases, entre otros.

# Algunas de estas librerias son desarrolladas por terceras partes, por
# lo que no hacen parte del programa original, sin embargo, la razon 
# mas importante es que consumirian mas memoria.

# Una de las librerias mas utilizadas en python es Numpy, una libreria
# diseniada pensando en la mejora y optimizacion de vectores y matrices

# Primero llamo la libreria

import numpy as np #por convencion se utiliza np

# Algunos ejemplos:

A1 = np.zeros(3)
A2 = np.zeros( (2,3) )
A3 = np.arange(0,10,1)
A4 = np.linspace(1000,1030,5)


print(A1)
print(A2)
print(A3)
print(A4)

#Numeros aleatorios con Numpy

A = np.random.randint(11, size=(3,3))
print(A)

# Una funcion es un grupo de codigo que recibe un numero de inputs (puede
# ser igual a 0) y ejecuta procesos especificos con esos datos para luego
# proveer un retorno (o output).

# Se las define por medio de la palabra clave def

def mi_funcion():
    print("Hola mundo, estoy en una funcion :)")
    
# Los inputs tambien se definen por medio de nombres genericos

def mi_funcion_saludo(nombre):
    print("Hola", nombre, "que gusto saludarte!")
    
# Obviamente, los inputs pueden ser numeros:
    
def mi_funcion_suma1(numero):
    print(numero + 1)  


# Mezclamos los dos conceptos y poder obtener funciones mas complejas


#Funcion para calcular ingresos y gastos generados

def IngresosyGastos(data):

    income = np.sum(data[data>0]) 
    expenses = np.sum(data[data<0])
    return (income, expenses) 

# Aca defino los datos de forma aleatoria

test = np.random.randint(10, size=(1,5)) - 5
print("Los numeros generados son:", test )

# Uso de la funcion

(misIngresos, misGastos) = IngresosyGastos(test)

print("Mis ingresos fueron:", misIngresos)
print("Mis gastos fueron:", misGastos)

def Vector3(data):
    restado = data - 3
    return restado

prueba = Vector3(test)



# Las clases son el nucleo de la programacion orientada a objetos
# Python es un lenguaje de programacion orientado a objetos

# Una clase es una generalización. Es un concepto, el cual podemos
# nutrir de caracteristicas. En el caso de la programacion, entendemos
# como objeto algo que tiene valores numericos o de texto y que 
# ademas puede ejecutar una accion especifica

class MiClase:
  x = 5
  edad = 30
  
p1 = MiClase()
print(p1.edad)
p2 = MiClase()

# Sin embargo, el aspecto mas importante de las clases es el de
# su construccion:

class MiembrodelClub:
  def __init__(self, nombre, edad, apellido):
    self.nombre = nombre
    self.edad = edad
    self.apellido = apellido

p1 = MiembrodelClub("Pedro", 40, "Romero")

print(p1.nombre)
print(p1.edad)

p2 = MiembrodelClub("Juan", 25)


class Panchonomist:
    def __init__(self, nombre, apellido, area, semestre):
        self.nombre = nombre
        self.apellido = apellido
        self.area = area
        self.semestre = semestre

Daniel = Panchonomist("Daniel", "Carrera", "Eventos Academicos", 6)



