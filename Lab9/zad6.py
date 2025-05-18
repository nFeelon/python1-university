from abc import ABC

class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Zoo():
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def print_animals(self):
        for animal in self.animals:
            print(animal.name, animal.age)

zoo = Zoo()

dog = Animal("Собака", 2)
cat = Animal("Кот", 3)
elephant = Animal("Реальный слон", 5)

zoo.add_animal(dog)
zoo.add_animal(cat)
zoo.add_animal(elephant)

zoo.remove_animal(cat)

zoo.print_animals()