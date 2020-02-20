from exceptii.erori import ValidError,RepoError
class Console(object):
    
    
    def __init__(self, srvJucator):
        self.__srvJucator = srvJucator
        self.__comenzi = {
        'add':self.__ui_adaugare_jucator,
        'modify':self.__ui_modificare_inaltime,
        'filter':self.__ui_filtrare_jucatori,
        'import':self.__ui_import_jucatori
        }
    
    def __ui_adaugare_jucator(self,parametrii):
    #Functia comunica cu utilizatorul pentru a introduce un jucator
        if len(parametrii)!=4: #nume,prenume,inaltime,post
            raise ValueError("Numar incorect de date introduse")
        
        nume = parametrii[0]
        prenume = parametrii[1]
        inaltime = parametrii[2]
        post = parametrii[3]
        
        self.__srvJucator.adaugare_jucator(nume,prenume,inaltime,post)
     
    def __ui_modificare_inaltime(self,parametrii):
    #Functia comunica cu utilizatorul pentru a modifica inaltimea
        if len(parametrii)!=3: #nume,prenume,inaltime
            raise ValueError("Numar incorect de date introduse")
        
        nume = parametrii[0]
        prenume = parametrii[1]
        inaltime = parametrii[2]
        
        self.__srvJucator.modificare_jucator(nume,prenume,inaltime)
        
    def __ui_filtrare_jucatori(self,parametrii):
    #Functia comunica cu utilizatorul pentru a creea o echipa cu media de inaltime maxima
    
        if len(parametrii)!=0:
            raise ValueError("Numar incorect de date introduse")
        
        echipa = self.__srvJucator.filtrare_echipa()
        
        for jucator in echipa:
            print(jucator)
        
    def __ui_import_jucatori(self,parametrii):
    #Functia comunica cu utilizatorul pentru a importa dintr-un fisier jucatori
    
        if len(parametrii)!=1: #fisierul
            raise ValueError("Numar incorect de date introduse")
        
        nume_fisier = parametrii[0]
        print("Au fost introdusi " , self.__srvJucator.importa_jucatori(nume_fisier))
        
    def run(self):
        """
    Functia principala de rulare a interfetei cu utilizatorul
    Utilizatorul intrduce o comanda, comanda este verificata si daca exista se executa
        """
    
        while True:
            
            comanda = input('Introduceti comanda dorita! ')
            
            comanda = comanda.strip()#elimin spatiile libere
            
            if comanda is None:
                print('Comanda invalida!')
            
            if comanda=='exit':
                print('Aplicatia a fost inchisa cu succes')
                break
            
            comanda = comanda.split(' ')
            nume_comanda = comanda[0]
            parametrii = comanda[1:]
            
            if nume_comanda in self.__comenzi.keys(): #verific daca exita comanda
                try:
                    self.__comenzi[nume_comanda](parametrii) #execut
                except ValueError as ve:
                    print("UI error: \n " + str(ve))
                except ValidError as valide:
                    print("Valid error: \n" + str(valide))
                except RepoError as re:
                    print("Repo error: \n" + str(re))
                    
            else:
                print("Comanda invalida!")
    
    
    
    
    



