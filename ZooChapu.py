#Queremos una lista donde se puedan ingresar animales
list = []
class Animal:
	def __init__(self):
		#Aqui irán los inputs
		cont =int(input("¿Cuántos animales entran?: "))
		for x in range (0,cont):
			self.name=input("¿Cuál es el nombre del animal?: ")
			list.append(self.name)
			self.tipo = input("¿Qué tipo de animal es?: ")
			print ("El animal "+self.name+" ha ingresado")
		print("La lista actual de animales es: " + list[:])
	def NewType(self):
		#Se registrará los nuevos tipos
new_animal = Animal()