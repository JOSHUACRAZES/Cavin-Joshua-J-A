#Single inheritance
class employee:
    def __init__(self,name):
        self.name = name
class manager(employee):
    def __init__(self,name,dept):
        super().__init__(name)
        self.dept = dept
    def show(self):
        print(f"{self.name} - {self.dept}")
m = manager("alice","Cybersecurity")
m.show()



#multiplevel inheritance
class livingBeing:
    alive = True
class Animal(livingBeing):
    can_move = True
class Dog(Animal):
    species = "canis lupus familiaries"
    def print_all(self):
        print(f"alive: {self.alive}")
        print(f"can move: {self.can_move}")
        print(f"species:{self.species}")
Dog = Dog()
Dog.print_all()

#Hierarchical inheritance
class vehicle:
    def type(self):
        print("this is vehicle")
class car (vehicle):
    def wheels(self):
        print("car has 4 wheels")
class bike(vehicle):
    def wheels(self):
        print("bike haS 2 wheels")
class truck(vehicle):
    def wheels(self):
        print("truck has 6 wheels")
car = car()
bike = bike()
truck = truck()

car.type()
car.wheels()

bike.type()
bike.wheels()

truck.type()
truck.wheels()


#multiple inheritance
class camera:
    def click(self):
        print("clicked a photo")
class phone:
    def call(self):
        print("making a call")
class smartphone(camera, phone):
    pass
sp = smartphone()
sp.click()
sp.call()


#Ploymorphism and Overriding
class Animal:
    def sound(self):
        print("some generic animal sound")
class dog(Animal):
    def sound(self):
        print("woof")
class cat (Animal):
    def sound(self):
        print ("meow")
a = Animal()
d = dog()
c = cat()

a.sound()
d.sound()
c.sound()


#Ploymorphism and Overloading
class calculator:
    def add(self,*args):
        print(sum(args))
calc = calculator()
calc.add(2, 3)
calc.add(2, 3, 4)