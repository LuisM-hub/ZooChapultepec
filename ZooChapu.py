#Queremos una lista donde se puedan ingresar animales
lista = []
list_type = []
class Animal:
	def __init__(self):
		#Aqui irán los inputs
		cont =int(input("¿Cuántos animales entran?: "))
		for x in range (0,cont):
			
			self.name=input("¿Cuál es el nombre del animal?: ")
			lista.append(self.name)
			
			self.type = input("¿Qué tipo de animal es?: ")
			list_type.append(self.type)	
			print ("El animal "+self.name+" ha ingresado y es del tipo: "+self.type)
		
		print("La lista actual de animales es: " + lista[:])
		bool validar = true; 
		while validar:
			id = int(input("Para cambiar el tipo de animal, escoge a un animal de la lista: "))
			if(id==0){
			print ("La lista empieza del 1 a n")
			print ("")
			}
			else
			{
			id--
			elegido = lista[id]
			elegido_t= list_type[id]
			print("El nombre del animal elegido es: "+ dato + " y es del tipo: " + elegido_t)
			self.NewType();
			}
			pass

	def NewType(self):
		#Se registrará los nuevos tipos
		self.type = input ("¿Cuál es el nuevo tipo de animal?")
new_animal = Animal()