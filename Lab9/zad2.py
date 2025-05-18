from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self):
        self.sound = "Гав"
    
    def make_sound(self):
        print(self.sound)

class Cat(Animal):
    def __init__(self):
        self.sound = "Мяяу"
    
    def make_sound(self):
        print(self.sound)


class Cow(Animal):
    def __init__(self):
        self.sound = "Мууу"
    
    def make_sound(self):
        print(self.sound)


animals = [Dog(), Cat(), Cow()]
for animal in animals:
    animal.make_sound()
