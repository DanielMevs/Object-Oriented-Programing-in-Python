class Dog:
	species = "Canis familiaris"

	def __init__(self, name, age, breed):
		self.name = name
		self.age = age
		self.breed = breed

	def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

 miles = JackRussellTerrier("Miles", 4)
 buddy = Dachshund("Buddy", 9)
 jack = Bulldog("Jack", 3)
 jim = Bulldog("Jim", 5)


 miles.species
#'Canis familiaris'

buddy.name
#'Buddy'

print(jack)
#Jack is 3 years old

jim.speak("Woof")
#'Jim says Woof'

type(miles)

isinstance(miles, Dog)

isinstance(miles, Bulldog)