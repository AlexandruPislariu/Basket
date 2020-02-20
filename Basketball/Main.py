'''
Created on 30 ian. 2020

@author: Alex
'''
#teste
from teste.testeValidare import TestValid
from teste.testeRepo import TestRepository
from teste.testeService import TestService

#validari
from validari.validation import ValidareJucator
validJucator = ValidareJucator()

#repository
from infrastructure.repository import RepositoryFile
from domain.entitati import Jucator
repoJucator = RepositoryFile('./echipa.txt',Jucator)

#service
from business.service import ServiceJucator
srvJucator = ServiceJucator(repoJucator,validJucator)

#UI
from prezentare.console import Console
ui = Console(srvJucator)
ui.run()
