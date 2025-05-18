class Person():
    _count = 0

    def __init__(self, name, age) -> None:
        self._name = name
        self._age = age
        Person._count += 1

    @classmethod
    def get_count(cls):
        return cls._count
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, newname):
        self._name = newname

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, newage):
        self._age = newage

person1 = Person("Некит", 19)
person2 = Person("Никита", 20)

print(Person.get_count())

print(person1._name)
print(person1.name)

person1.name = "Никитос"
print(person1.name)

print(person1.age)
person1.age = 21
print(person1.age)