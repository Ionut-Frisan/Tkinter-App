from Service.Service_clienti import *
from Service.Service_filme import *
from Repository.Repo_filme import *
from Repository.Repo_clienti import *

class UI():
    def __init__(self,servF,servC):
        self.servF = servF
        self.servC = servC

    def readinput(self,inp,message,type):
        inp = input(message)
        inp = type(inp)
        return inp

    def adaugaClient(self):
        id = int
        cnp = int
        id = self.readinput(id,"Id: ",int)
        nume = input("Nume: ")
        cnp = self.readinput(cnp,"Cnp: ",int)
        newCl = Client(id,nume,cnp)
        try:
            self.servC.adaugaClient(newCl)
        except ValueError as ve :
            print(ve)

    def stergeClient(self):
        criteriu = input("Criteriu: ")
        valoare = input("Valoare: ")
        try :
            self.servC.stergeClient(criteriu,valoare)
        except ValueError as ve :
            print(ve)

    def modificaClient(self):
        id = int
        id = self.readinput(id, "Id: ", int)
        criteriu = input("Criteriu: ")
        valoare = input("Valoare: ")
        try :
            self.servC.modificaClient(id,criteriu,valoare)
        except ValueError as ve :
            print(ve)

    def cautaClient(self):
        valoare = input("Keyword: ")
        try:
            clientiGasiti = self.servC.cautaClient(valoare)
            if len(clientiGasiti) != 0:
                print("Clienti gasiti :")
                for client in clientiGasiti :
                    print(client)
        except ValueError as ve :
            print(ve)

    def printClienti(self):
        print("**Clienti: ")
        self.servC.printClienti()

    def printFilme(self):
        print("**Filme: ")
        self.servF.printFilme()

    def adaugaFilm(self):
        id = int
        id = self.readinput(id,"Id: ",int)
        titlu = input("Titlu: ")
        descriere = input("Descriere :")
        gen = input("Gen: ")
        newFilm = Film(id,titlu,descriere,gen)
        try :
            self.servF.adaugaFilm(newFilm)
        except ValueError as ve :
            print(ve)

    def stergeFilm(self):
        criteriu = input("Criteriu: ")
        valoare = input("Valoare: ")
        try:
            self.servF.stergeFilm(criteriu, valoare)
        except ValueError as ve:
            print(ve)

    def modificaFilm(self):
        id = int
        id = self.readinput(id,"Id: ",int)
        criteriu = input("Criteriu: ")
        valoare = input("Valoare noua: ")
        try :
            self.servF.modificaFilm(id,criteriu,valoare)
        except ValueError as ve :
            print(ve)

    def cautaFilm(self):
        valoare = input("Keyword: ")
        try :
            filmeGasite = self.servF.cautaFilm(valoare)
            if (len(filmeGasite)) > 0 :
                for film in filmeGasite :
                    print(film)
        except ValueError as ve :
            print(be)

    def print_menu(self):
        print("\n Menu : ")
        print("1.Adauga client")
        print("2.Sterge client")
        print("3.Modifica client")
        print("4.Cauta client")
        print("5.Adauga film")
        print("6.Sterge film")
        print("7.Modifica film")
        print("8.Cauta film")
        print("9.Exit()")

    def run(self):

        while(True):
            self.print_menu()
            self.printClienti()
            self.printFilme()
            optiune = input("Optiune: ")
            if optiune == "1" :
                self.adaugaClient()
            elif optiune == "2" :
                self.stergeClient()
            elif optiune == "3" :
                self.modificaClient()
            elif optiune == "4" :
                self.cautaClient()
            elif optiune == "5" :
                self.adaugaFilm()
            elif optiune == "6" :
                self.stergeFilm()
            elif optiune == "7" :
                self.modificaFilm()
            elif optiune == "8" :
                self.cautaFilm()
            elif optiune == "9" :
                print("O zi buna !")
                return
            else :
                print(" !!! Optiune invalida !!! ")

