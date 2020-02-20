from domain.entitati import Jucator
from exceptii.erori import ValidError


class ValidareJucator():
    
    def validare_jucator(self,jucator):
    #Functia valideaza un jucator transmis (nume,prenume nevide) inaltime pozitiva  
        
        erori_validare = ''
        #nume,prenume nevide  
        if jucator.get_nume() is None:
            erori_validare += "Nume invalid" + '\n'
        if jucator.get_prenume() is None:
            erori_validare += "Prenume invalid" + '\n'
        
        #inaltime pozitiva
        try:
            inaltime = int(jucator.get_inaltime())
            
            if inaltime <= 0:
                erori_validare += "Inaltime invalida" + '\n'
            
            jucator.set_inaltime(inaltime)
        
        except ValueError:
            erori_validare += "Inaltime invalida" + '\n'
            
        
        #verific postul
        post = jucator.get_post()
        
        if post!='Fundas' and post!='Pivot' and post!='Extrema':
            erori_validare += "Post invalid" +'\n'
        
        if erori_validare=='':
            return True
        else:
            raise ValidError(erori_validare)

