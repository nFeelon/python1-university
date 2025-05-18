from abc import ABC

class Place(ABC):
    def __init__(self, area, address):
        self.area = area
        self.address = address
    
    def to_sell(self):
        print(f"Продается помещение по адресу {self.address} и с площадью {self.area:.2f} метров квадратных")
    
class Apartment(Place):
    def __init__(self, area, address, rooms):
        super().__init__(area, address)
        self.rooms = rooms

    def to_sell(self):
        super().to_sell()
        print(f"С {self.rooms} комнатами!")

class House(Place):
    def __init__(self, area, address, floors):
        super().__init__(area, address)
        self.floors = floors

    def to_sell(self):
        super().to_sell()
        print(f"С {self.floors} этажами!")

apartment = Apartment(100, "улица Свердлова, 13", 3)
house = House(200, "улица Уличная, -1", 2)

apartment.to_sell()
house.to_sell()