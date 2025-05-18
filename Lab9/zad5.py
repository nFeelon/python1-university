class Engine():
    def start(self):
        print("Двигатель запущен.")

class Car():
    def __init__(self):
        self.engine = Engine()

    def start_engine(self):
        self.engine.start()

car = Car()
car.start_engine()