import animal
import unittest

class TestClass(unittest.TestCase):
    data=(animal.Animal(10,2))

    def test_age(self):
        result=self.data.age
        self.assertEqual(result, 10)
    
    def test_poids(self):
        result=self.data.getWeight()
        self.assertEqual(result, 2)

    def test_eat_mammal(self):
        data=animal.Mammal('brown',15,1,2)
        data.eat(12)
        result=data.getWeight()
        self.assertEqual(result, 14)
    
    def test_hair_color(self):
        data=animal.Mammal('red',15,1,2)
        result=data.hair_color
        self.assertEqual(result, 'red')

    def test_size_of_beak_bird(self):
    	data=animal.Bird('blue',2,3)
    	result=data.size_of_beak
    	self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
