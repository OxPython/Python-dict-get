'''
Created on Jul 2, 2014

@author: viejoemer

HowTo get a specific value from a dict in python?

¿Cómo obtener un valor específico de un diccionario en Python?

'''

#Creating a dict with data
d = {
     "red":100,
     "yellow":200,
     "blue" : 300
     }
print(d)

#Get a value from a dict
value = d.get("red")
print(value)