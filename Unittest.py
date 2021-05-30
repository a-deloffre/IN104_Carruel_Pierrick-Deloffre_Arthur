import unittest
from preprocess_data import PreprocessData
#from preprocess_data import remove_all, convert_lowercase, lemmatization_text


class Test(unittest.TestCase):
    
    texte= ('dollar')
    
    def test_remove_all(self, texte):
        new_text1=PreprocessData.remove_all(texte)
        self.assertEqual(new_text1, ('dollar'))
    
    def test_convert_lowercase(self):
        texte2=('My name is BOND, James BOND')
        new_text2=PreprocessData.convert_lowercase(texte2)
        self.assertEqual(new_text2, 'my name is bond, james bond')
        
    def test_lemmatization(self, texte):
        new_text3=PreprocessData.lemmatization_text(texte)
        self.assertEqual(new_text3,'dollar')
    
    
    
if __name__ == "__main__":
    unittest.main()