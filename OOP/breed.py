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

miles = Dog("Miles", 4, "Jack Russell Terrier")
buddy = Dog("Buddy", 9, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")

buddy.speak("Yap")
jim.speak("Woof")
jack.speak("Woof")