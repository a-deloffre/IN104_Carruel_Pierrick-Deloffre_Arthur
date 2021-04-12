class Animal:

    def __init__(self, age, weight):
        
        self.weight = weight
        self.age = age

    def getWeight(self):

        return self.weight

    def eat(self, kgm):

        self.weight+=kgm
        print("The animal weights",self.weight,"kg after eating.")

    def getAge(self):
        return self.age

class Bird(Animal):
    def __init__ (self, color_of_feather, size_of_beak,weight):
        self.color_of_feather=color_of_feather
        self.size_of_beak=size_of_beak
        self.weight=weight

    def __str__(self):
        return "I am a bird of "+str(self.getWeight())+" kg"

    def lay_eggs(self):
        print("I lay eggs, as I'm a bird !")

    def fly(self):
        print("I fly as a bird")

class Mammal(Animal):
    def __init__(self,hair_color,fur_width,age,weight):
        self.hair_color=hair_color
        self.fur_width=fur_width
        self.weight=weight
        self.age=age
    def __str__(self):
        return "I am a "+str(self.getAge())+" year-old mammal"

    def lay_eggs(self):
        print("I don't lay eggs : I'm a mammal")

    def fly(self):
        print("I don't fly : I'm a mammal")