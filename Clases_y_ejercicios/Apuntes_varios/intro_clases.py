# Clase padre Mascota
class Pets:
    #atributos
    mascota = []
    #Constructor de la clase
    def __init__(self, mascota):
        self.mascota = mascota
    #Método Walk
    def mover(self):
        for mascota in self.mascota:
            print(mascota.mover())
    def run(self, speed=0):
        for mascota in self.mascota:
            print(mascota.run(speed))
# Clase Padre Perro
class Dog:
    # Atributos
    species = 'mammal'
    is_hungry = True
    # Constructor de la clase
    def __init__(self, name, age, fur):
        self.name = name
        self.age = age
        self.fur = fur
    def __str__():
        return "este animal es de la especie: ",self.species
    # Método description
    def description(self):
        return self.name, self.age
    # Método Speak
    def speak(self, sound):
        return "%s says %s" % (self.name, sound)
    # Método eat
    def eat(self):
        self.is_hungry = False
    #Método walk
    def mover(self):
        return "%s is walking!" % (self.name)
    def run(self, speed=0):
        return "%s es perro perro" % (self.name)
#Clase padre Pez
class Fish:
 # Atributos
    species = 'vertebrados'
    is_hungry = True
    # Constructor de la clase
    def __init__(self, name, age, fins):
        self.name = name
        self.age = age
        self.fins = fins
    # Método description
    def description(self):
        return self.name, self.age
    def mover(self):
         return "%s is swimming!" % (self.name)
    def run(self, speed=0):
        return "%s no corre!!" % (self.name)
class Shark(Fish):
    #atributos
    color = 'gris'
    def __init__(self, name, age, fins, color):
        self.name = name
        self.age = age
        self.fins = fins
        self.color = color
    def mover(self):
        return "%s su edad es %s" % (self.name,self.age)
# Clase Hijo (hereda de la clase Perro Dog)
class RussellTerrier(Dog):
    def run(self, speed=0):
        return "%s runs %s" % (self.name,speed)
# Clase Hijo (Hereda de la clase Perro )
class Bulldog(Dog):
    peso = 10
    def __init__(self,name,age,fur,size):
        Dog.name = name
        Dog.age = age
        Dog.fur = fur
        self.size = size
    def run(self, speed):
        return "La mascota %s corre %s, y tiene un tamaño %s " % (self.name,speed,self.size)

# Creamos una instancia de Perro
"""
lista_objetos_mascotas = [
    Bulldog("Pancho", 6,"corto","grande"), 
    RussellTerrier("Puppy", 7,"largo"), 
    Dog("Huesos", 9,"corto"),
    Fish("Nemo",2,2)
]"""
objetobulldog = Bulldog("pepe",5,"corto","grande")
objetorussellterrier = RussellTerrier("puppy",5,"largo")
objetoPez = Fish("Tiburón",2,3)
objetoShark = Shark("Tibu",10,3,"rojo")
lista_objetos_mascotas = [objetobulldog,objetorussellterrier,objetoPez,objetoShark]
# Creamos una instacia de Mascota
mis_mascotas = Pets(lista_objetos_mascotas)
# Salida
#mis_mascotas.mover()
mis_mascotas.run(100)
print(lista_objetos_mascotas[3].run(10))
print(f'el perro pesa: {lista_objetos_mascotas[0].peso} kg')
