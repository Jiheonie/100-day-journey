from webbrowser import get


class Car:
    def __init__(self, **kw) -> None:
        self.make = kw.get('make')
        self.model = kw.get('model')

my_car = Car(make='Nissan', model='GT-R')
print(my_car.make)
