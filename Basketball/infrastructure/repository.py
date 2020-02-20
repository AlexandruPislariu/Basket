from exceptii.erori import RepoError
class RepositoryFile(object):


    def __init__(self, filename, entity):
        self.__filename = filename
        self.__entity = entity
        self.__lista_entitati = []
        self.__read_all_from_file()

    def __read_all_from_file(self):
        """
    Functia citeste de pe liniile fisierului entitatile si le adauga in lista din memorie
        """
        fisier = open(self.__filename,'r')

        content = fisier.read()
        content = content.split('\n')

        for line in content:
            if line.strip()=='':
                continue

            entitate = self.__entity.read_entity(line)#transform linia in entitate
            self.adauga_entitate(entitate)#adaug in memorie

        fisier.close()

    def __write_all_in_file(self):
        """
    Functia adauga in fisier lista de entitati din memorie
        """
        fisier = open(self.__filename,'w')

    #Golesc fisierul
        fisier.seek(0)
        fisier.truncate()

    #Preiau entitatile
        entitati = self.get_all()

    #Rescriu continutul fisierului
        for element in entitati:
            fisier.write(self.__entity.write_entity(element))#transform un element intr-un string pentru a putea fi scris pe o linie a fisierului
            fisier.write('\n')

        fisier.close()

    def get_entitate(self,index):
        """
    Functia returneaza o entitate de pe un anumit index
        """
        return self.__lista_entitati[index]

    def get_all(self):
        """
    Functia returneaza lista entitatilor(privata)
        """
        return self.__lista_entitati

    def cauta_entitate(self,entitate):
        """
    Functia returneaza indicele entitatii daca se afla in lista, -1 in caz contrar
        """
        entitati = self.get_all()

        for element in entitati:
            if element.get_nume()==entitate.get_nume() and element.get_prenume()==entitate.get_prenume():
                return entitati.index(element)

        return -1

    def adauga_entitate(self,entitate):
        """
    Functia adauga o entitate atat in lista din memorie cat si in fisier
    Daca se afla deja, se produce o eroare
        """
        if self.cauta_entitate(entitate)!=-1: #se afla in lista, nu se poate adauga
            raise RepoError("Se afla deja in lista")

        self.__lista_entitati.append(entitate)#stochez in memorie
        self.__write_all_in_file()#adaug in fisier

    def modifica_entitate(self,entitate):
        """
    Functia modifica un atribut al unei entitati
    Daca entitatea nu se afla in lista, se produce o eroare
        """
        index = self.cauta_entitate(entitate)

        if index==-1: #Nu se afla
            raise RepoError("Nu se afla in lista")

        element = self.get_entitate(index)
        element.set_inaltime(entitate.get_inaltime())#modific in memorie
        self.__write_all_in_file()#modific si in fisier

    def sterge_entitate(self,entitate):
        """
    Functia sterge o entitate atat din memorie cat si din fisier
    Daca entitatea nu se afla in lista, se produce o eroare
        """
        index = self.cauta_entitate(entitate)

        if index == -1: #nu se afla o entitate
            raise RepoError("Nu se afla in lista")

        del self.__lista_entitati[index]#modific in memorie
        self.__write_all_in_file()#modific in fisier

