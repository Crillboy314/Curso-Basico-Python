"""
Script 1: Tipo de datos, ejecución de códigos y consola
Autor: kevinrojas
"""

"""
Este archivo fue presentado mientrás se impartía el curso de python.
"""

# PRINT es nuestra expresión con el exterior

print("Hola Mundo")
print("Hola", "Mundo")
print("Hola" + "Mundo")

# ademas permite resolver calculos simples (una gran calculadora)

print(5)
print(50+100)
print(123456789 * 987654321)
print(123456789 / 987654321)

# INPUT por su parte, nos permite incorporar informacion a un programa
# Recordar que INPUT considera como datos de tipo de string lo ingresado

#Programa "amistoso" para el calculo del IVA

Nombre = input("Como te llamas")

print("Hola " + Nombre)

Pago = input("Ingresa el valor a pagar")

PagoNum = int(Pago)

print("El valor total con IVA sería ", PagoNum + (0.12*PagoNum) )

# Python, como lenguaje de programación, ofrece una variedad de tipos de
# datos posibles con los cuales se puede trabajar de forma independiente
# desde la consola o por medio de un IDE

# Siempre podemos identificar el tipo de datos por medio de TYPE:

#Con datos numericos (float e integer):

a = 3
print(type(a))
b = 3.25
print(type(b))

#Con datos de tipo string (para represantacion de texto)

c = "USFQ"
print(type(c))

#Finalmente, los otros tipos de datos mas frecuentes en python son:

#Booleanos

d = 3 < 2
print(type(d))

#Listas LIST

Colegios = ["CADE", "POLI", "CHAT", "COM"]
print(type(Colegios))

#Diccionarios DICT

diccionario = {
  "marca": "Toyota",
  "modelo": "Camry",
  "anio": 1998
}
print(type(diccionario))

#NOTA: Proceso de casting de puede hacer con int(), float(), str()

# Los controladores de flujo son los llamados de elementos mas usados
# en general en programacion, un ejemplo de esto puede ser:

# UTILIZANDO IF 

a = float(input("Ingresa el primer numero"))
b = float(input("Ingresa el segundo numero"))
if b > a:
    print("El segundo numero", b, "es mas grande que el primer numero ", a )
elif a == b:
    print("los dos numeros son iguales")
else:
    print("El primer numero", a, "es mas grande que el segundo numero ", a )


# UTILIZANDO FOR

x = range(3, 6)
for n in x:
  print(n)
  
x = range(3, 20, 2)
for n in x:
  print(n)
  
Colegios = ["CADE", "POLI", "CHAT", "COM"]

for name in Colegios:
    print("Un colegio academico de la USFQ es", name)

        
# UTILIZANDO WHILE
        
i = 1
print("Voy a empezar a contar")
while i < 10:
    print(i)
    i = i + 1

# A continuacion, un ejemplo de loop infinito

#while True:
#    print("Al infinito y mas alla, estoy en ", i)
#    i = i + 1
 


