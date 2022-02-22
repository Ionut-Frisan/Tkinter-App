from Valid.Valid_film import *
from Valid.Valid_client import *
from UI.UI import *


repoC = Repo_clienti()
repoF = Repo_film()
validC = Valid_client()
validF = Valid_film()
servC = Service_clienti(repoC,validC)
servF = Service_filme(repoF,validF)
ui = UI(servF,servC)

ui.run()





"""Scrieți o aplicație pentru o firmă de închiriere de filme.
    Aplicația stochează:
        filme: <id>,<titlu>,<descriere>,<gen>,etc
        clienți: <id>, <nume>, <CNP>,etc
    Creați o aplicație care permite:
        gestiunea listei de filme și clienți.+

        adaugă,șterge, modifică, lista de filme, lista declienți
        căutare film, căutare clienți.
        Închiriere/returnare filme
        Rapoarte:
            Clienți cu filme închiriate ordonat dupa:nume,  după numărul de filme închiriate
            Cele mai inchiriate filme.
            Primi 30% clienti cu cele mai multe filme (nume client și numărul de filme închiriate """
