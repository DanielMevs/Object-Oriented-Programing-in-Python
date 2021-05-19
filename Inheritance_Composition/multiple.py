# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance


class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "Class A"


class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "Class B"


class C(A, B):
    def __init__(self):
        super().__init__()

    def showprops(self):
    	print(self.foo)
    	print(self.bar)
    	#will print the name of the first parent class inherited
    	#to print Class B change the order i.e. class C(B, A)
    	print(self.name)


c = C()
c.showprops()
#shows the method resolution order
print(C.__mro__)
