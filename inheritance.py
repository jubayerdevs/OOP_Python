class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("")


class Lion(Animal):
    def make_sound(self):
        print("RoooooARRRRR!!!")



class Dog(Animal):
    def make_sound(self):
        print("BAAAARKkkkk!!!")

    
lion1 = Lion("BDLion", 5)
dog1 = Dog("BDDog", 10)
print(lion1.name)
print(dog1.name)

lion1.make_sound()
dog1.make_sound()