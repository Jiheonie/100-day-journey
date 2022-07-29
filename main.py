class Animal:
    def __init__(self) -> None:
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Dog(Animal):
    def __init__(self) -> None:
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Doing in the water.")

yenmach = Dog()
print(yenmach.num_eyes) 
yenmach.breathe()