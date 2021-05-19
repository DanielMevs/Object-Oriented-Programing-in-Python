class Dog:
	#Class attribue
	species = "Canis familiaris"

	def __init__(self, name, age):
		self.name = name #instance attribute
		self.age = age #instance attribute

buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)

#access instance attributes with dot operator
print(buddy.name)
print(mile.age)

#access class attributes in the same way
print(buddy.species)