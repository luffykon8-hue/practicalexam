#Multiple Inheritance Example
class Flyer:
    def fly(self):
        return "I can fly!"

class Swimmer:
    def swim(self):
        return "I can swim!"

class Duck(Flyer, Swimmer): # Inherits from both Flyer and Swimmer
    def quack(self):
        return "Quack!"

# Usage
stupid = Duck()
print(stupid.fly())   # From Flyer
print(stupid.swim())  # From Swimmer
print(stupid.quack()) # From Duck

#Multilevel Inheritance Example
class Animal:
    def eat(self):
        return "Sleeping and Eating"

class Dog(Animal):
    def bark(self):
        return "Always Barking"
class Cat(Animal):
    def meow(self):
        return "Always Meowing"
# Usage
dog = Dog()
cat = Cat()
print(cat.eat())  # From Animal
print(cat.meow())  # From Cat
print(dog.eat())  # From Animal
print(dog.bark()) # From Dog