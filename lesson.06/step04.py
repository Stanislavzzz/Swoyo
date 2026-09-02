class Car:
    def __init__(self, color="white"):
        self.engine_on = False
        self.__color = color

    def start_engine(self):
        self.engine_on = True

    def drive_to(self, city):
        if self.engine_on:
            print(f"Едем на  {self.__color} авто в {city}")
        else:
            print(f"{self.__color} Машина не заведена")


car1 = Car()
car1.start_engine()
car1.__color = 'black'
car1.drive_to("Москву")

car2 = Car("Красный")
# car2.start_engine()
car2.drive_to("Сочи")