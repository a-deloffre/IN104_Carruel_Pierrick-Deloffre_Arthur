import geometric_figures
import unittest

class TestClass(unittest.TestCase):
    data=[geometric_figures.Shape(4,5),geometric_figures.Rectangle(2,2),geometric_figures.Ellipse(6,3)]

    def test_length(self):
        result=self.data[0].getLength()
        self.assertEqual(result, 4)
    
    def test_width(self):
        result=self.data[0].getWidth()
        self.assertEqual(result, 5)

    def test_is_square(self):
        result=self.data[1].is_square()
        self.assertTrue(result)

    def test_perimeter_rectangle(self):
        result = self.data[1].perimeter()
        self.assertEqual(result, 8)
    
    def test_area_rectangle(self):
        result = self.data[1].area()
        self.assertEqual(result, 4)

    def test_is_circle(self):
        result=self.data[2].is_circle()
        self.assertFalse(result)

    def test_area_ellipse(self):
        result = self.data[2].approxArea()
        self.assertEqual(result, (9, 18))

if __name__ == '__main__':
    unittest.main()