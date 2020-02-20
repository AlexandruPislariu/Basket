import unittest
from domain.entitati import Jucator
from validari.validation import ValidareJucator
from exceptii.erori import ValidError

class TestValid(unittest.TestCase):
#Functia testeaza validarea unui jucator

    def setUp(self):
        
        self.p1 = Jucator('','ada',20,'Extrema')
        self.p2 = Jucator('ada','',-1,'Fundas')
        self.p3 = Jucator('Dumitru','Costel',190,'adsa')
        self.p4 = Jucator('Dumitru','Costelino',180,'Extrema')
        
        self.valid = ValidareJucator()
        
    def tearDown(self):
        pass
    
    def test_validare_jucator(self):
        
        with self.assertRaises(ValidError):
            self.valid.validare_jucator(self.p1)
            self.valid.validare_jucator(self.p2)
            self.valid.validare_jucator(self.p3)
        
        self.assertEqual(self.valid.validare_jucator(self.p4),True)
      
if __name__=='__main__':
    unittest.main()  
        


