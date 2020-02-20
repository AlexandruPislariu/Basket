import unittest
from infrastructure.repository import RepositoryFile
from exceptii.erori import RepoError
from domain.entitati import Jucator



class TestRepository(unittest.TestCase):
#Functia testeaza repository

    def setUp(self):
    #repo
        self.repo = RepositoryFile('./fisier_test.txt',Jucator)
        
    #creez jucatori valizi
        self.p1 = Jucator("Radu",'Ilie',180,'Extrema')
        self.p2 = Jucator("Alex",'Ilie',180,'Fundas')
        self.p3 = Jucator("Gheorghe",'Ilie',180,'Pivot')
        self.p4 = Jucator("Angel",'Ilie',180,'Pivot')
        self.p5 = Jucator("Simon",'Ilie',180,'Extrema')
        self.p6 = Jucator("Radu",'Ilie',180,'Fundas')
        self.p7 = Jucator("Ana","Maria",160,'Extrema')
        
    #adaug jucatorii
        self.repo.adauga_entitate(self.p1)
        self.repo.adauga_entitate(self.p2)
        self.repo.adauga_entitate(self.p3)
        self.repo.adauga_entitate(self.p4)
        self.repo.adauga_entitate(self.p5)
        
       
    def tearDown(self):
        
        fh = open('./fisier_test.txt','w')
        fh.seek(0)
        fh.truncate()
        fh.close()
        
    def test_get_all(self):
        
        self.assertEqual(self.repo.get_all(), [self.p1,self.p2,self.p3,self.p4,self.p5])
       
    def test_get_entitate(self):
        
        entitati = self.repo.get_all()
        self.assertEqual(entitati[0], self.p1)
        
    def test_adauga_entitate(self):
        
        with self.assertRaises(RepoError):
            self.repo.adauga_entitate(self.p6) 
            
        self.repo.adauga_entitate(self.p7)
        self.assertEqual(self.repo.get_all(), [self.p1,self.p2,self.p3,self.p4,self.p5,self.p7])
        
    def test_cauta_entitate(self):
        self.assertEqual(self.repo.cauta_entitate(self.p1), 0)
        self.assertEqual(self.repo.cauta_entitate(self.p5), 4)
        self.assertEqual(self.repo.cauta_entitate(self.p3), 2)
    
    def test_modifica_entitate(self):
        
        with self.assertRaises(RepoError):
            self.repo.modifica_entitate(self.p7)
            
        new = Jucator("Radu",'Ilie',200,'Extrema')
        index = self.repo.cauta_entitate(new)
        self.repo.modifica_entitate(new)
        
        self.assertEqual(self.repo.get_entitate(index).get_inaltime(), new.get_inaltime())
if __name__=='__main__':
    unittest.main()
            
        


