class Dog:
	#class attribute
	species = "Canis familiaris"

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __str__(self):
		return f"{self.name} is {self.age} years old"
