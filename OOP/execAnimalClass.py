from __future__ import print_function
import animal

animal1=animal.Animal(3,50)
bear=animal.Mammal(10,1,6,150)
duck=animal.Bird(2,1,3)

print(bear)
bear.eat(0.3)
bear.fly()
bear.lay_eggs()

print(duck)
duck.fly()
duck.lay_eggs()
