# Inheritance in OOP

"""
            Animal
      Vert            Invert
Mammal
"""

class Animal:    # "Base Class"

    def __init__(self, name):
        self.name = name
    
    def call(self):
        print(f" {self.name}: Generic animal sound")

class Vertibrate(Animal):    # Vertibrate is an Animal, "is-a" relationship

    def call(self):    # Override the parent class' call method
        print("Generic vertibrate sound")

class Mammal(Vertibrate):
    pass

class Cat(Mammal):

    def __init__(self, name, evil):
        super().__init__(name)
        self.evil = evil

    def call(self): 
        print(f'{self.name} ({"evil" if self.evil else "not evil"}): Meow')

class Invertibrate(Animal):    # Intertibrate is an Animal, "is-a" relationship
    pass

animals = [
    Animal("animal 1"),
    Vertibrate("vert 1"),
    Invertibrate("invert 1"),
    Cat("cat 1", False),
]

a = Animal("animal 1")
a.call()

v = Vertibrate("vert 1")
v.call()

iv = Invertibrate("invert 1")
iv.call()

c = Cat("cat 1", False)
c.call()

