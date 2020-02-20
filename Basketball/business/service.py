from domain.entitati import Jucator
from business.random import generate_random_integer,generate_random_string
from exceptii.erori import RepoError
class ServiceJucator(object):
    
    
    def __init__(self, repoJucator, validJucator):
        self.__repoJucator = repoJucator
        self.__validJucator = validJucator
    
    

    def adaugare_jucator(self,nume,prenume,inaltime,post):
        
        jucator = Jucator(nume,prenume,inaltime,post)
        
      
        if(self.__validJucator.validare_jucator(jucator)):
            self.__repoJucator.adauga_entitate(jucator)
        
    def modificare_jucator(self,nume,prenume,inaltime):
        
        jucator = Jucator(nume,prenume,inaltime,'Pivot')
        
        if(self.__validJucator.validare_jucator(jucator)):
            self.__repoJucator.modifica_entitate(jucator)

    def filtrare_echipa(self):
    #preiau jucatorii
        jucatori = self.__repoJucator.get_all()
    
    #sortez in ordinea descrescatoare a inaltimii
        jucatori = sorted(jucatori, key = lambda x: x.get_inaltime(), reverse = True)
        
    #creez o echipa valida(2 fundasi, 2 extreme, 1 pivot)
        dict = {'Fundas': 2, 'Extrema': 2, 'Pivot': 1}
        
        echipa = []
        
        for jucator in jucatori:
            post_jucator = jucator.get_post()
            
            if dict[post_jucator]>0:
                echipa.append(jucator)
                dict[post_jucator]-=1
    
        return echipa
    
    def importa_jucatori(self,nume_fisier):
    #deschid fisierul
        fisier = open(nume_fisier,'r')
        
        content = fisier.read()
        content = content.split('\n')
        
        numar_jucatori_adaugati = 0
        
        for line in content:
            if line.strip()=='':
                continue
            
            line = line.split(' ')
            nume = line[0]
            prenume = line[1]
            inaltime = generate_random_integer(150,200)
            post = generate_random_string()
            
            try:
                self.__repoJucator.adauga_entitate(Jucator(nume,prenume,inaltime,post))
                numar_jucatori_adaugati += 1  
            except RepoError:
                continue
            
        fisier.close()
        return numar_jucatori_adaugati