import unittest
from infrastructure.repository import RepositoryFile
from validari.validation import ValidareJucator
from domain.entitati import Jucator
from business.service import ServiceJucator

class TestService(unittest.TestCase):
   
    def setUp(self):
    #repo
        self.repo = RepositoryFile('./fisier_test.txt',Jucator)
    #validare
        self.valid = ValidareJucator()    
    #service
        self.service = ServiceJucator(self.repo,self.valid)
    #creez jucatori valizi
        self.p1 = Jucator("Radu",'Ilie',130,'Extrema')
        self.p2 = Jucator("Alex",'Ilie',120,'Fundas')
        self.p3 = Jucator("Gheorghe",'Ilie',200,'Pivot')
        self.p4 = Jucator("Angel",'Ilie',180,'Pivot')
        self.p5 = Jucator("Simon",'Ilie',150,'Extrema')
        self.p6 = Jucator("Raducu",'Ilie',180,'Fundas')
        self.p7 = Jucator("Ana","Maria",140,'Extrema')
        
    #adaug jucatorii
        self.repo.adauga_entitate(self.p1)
        self.repo.adauga_entitate(self.p2)
        self.repo.adauga_entitate(self.p3)
        self.repo.adauga_entitate(self.p4)
        self.repo.adauga_entitate(self.p5)
        self.repo.adauga_entitate(self.p6)
        self.repo.adauga_entitate(self.p7)
    

    def tearDown(self):
        
        fh = open('./fisier_test.txt','w')
        fh.seek(0)
        fh.truncate()
        fh.close()
        
    def test_filtrare_echipa(self):
        
        echipa = self.service.filtrare_echipa()
        self.assertEqual(echipa[0].get_nume(), self.p3.get_nume())
        self.assertEqual(echipa[0].get_prenume(), self.p3.get_prenume())
        self.assertEqual(echipa[1].get_nume(), self.p6.get_nume())
        self.assertEqual(echipa[1].get_prenume(), self.p6.get_prenume())
        self.assertEqual(echipa[2].get_nume(), self.p5.get_nume())
        self.assertEqual(echipa[2].get_prenume(), self.p5.get_prenume())
        self.assertEqual(echipa[3].get_nume(), self.p7.get_nume())
        self.assertEqual(echipa[3].get_prenume(), self.p7.get_prenume())
        self.assertEqual(echipa[4].get_nume(), self.p2.get_nume())
        self.assertEqual(echipa[4].get_prenume(), self.p2.get_prenume())
    
      
    def test_import_jucatori(self):
        
        numar_importuri = self.service.importa_jucatori('import_test.txt')
        jucatori = self.repo.get_all()
        
        self.assertEqual(jucatori[7].get_nume(), 'Mitrofan')
        self.assertEqual(jucatori[7].get_prenume(), 'Catalin')
        self.assertEqual(jucatori[8].get_nume(), 'Flutur')
        self.assertEqual(jucatori[8].get_prenume(), 'Vasile')
        self.assertEqual(numar_importuri, 3)
        
if __name__=='__main__':
    unittest.main()