from Repository.Clienti import *

class Repo_clienti():
    def __init__(self):
        self._listaClienti = []

    def adaugaClient(self,newClient):
        duplicat = False
        for client in self._listaClienti:
            if client.get_id() == newClient.get_id():
                duplicat = True
        if duplicat == False :
            self._listaClienti.append(newClient)
        else:
            raise ValueError("id existent")


    def stergeClient(self,criteriu,valoare):
        removed = False
        if criteriu == "id" :
            for client in self._listaClienti :
                if str(client.get_id()) == str(valoare) :
                    self._listaClienti.remove(client)
                    removed = True
        elif criteriu == "nume" :
            for client in self._listaClienti :
                if client.get_nume() == valoare :
                    self._listaClienti.remove(client)
                    removed = True
        elif criteriu == "cnp" :
            for client in self._listaClienti :
                if str(client.get_cnp()) == str(valoare) :
                    self._listaClienti.remove(client)
                    removed = True

        if removed == False :
            raise ValueError("Date incorecte!")

    def modificaClient(self,id,criteriu,valoare):
        modificare = False
        if criteriu == "nume" :
            for client in self._listaClienti :
                if client.get_id() == id :
                    client.set_nume(valoare)
                    modificare = True
        if criteriu == "cnp" :
            for client in self._listaClienti :
                if client.get_id() == id :
                    client.set_cnp(valoare)
                    modificare = True
        if criteriu != "cnp" and criteriu != "nume" :
            raise ValueError("Criteriu invalid !")

        if modificare == False :
            raise ValueError("Id-ul introdus nu corespunde unui client !")

    def modificaClientGUI(self,id,newName,newCnp):
        modificare = False
        for i in range(0,len(self._listaClienti)):
            if self._listaClienti[i].get_id() == id :
                self._listaClienti[i].set_nume(newName)
                self._listaClienti[i].set_cnp(newCnp)
                modificare = True
        if modificare == False :
            raise ValueError("Ceva a facut BooM !")

    def cautaClient(self,valoare):
        clientiGasiti = []
        for client in self._listaClienti :
            #print(type(client.get_id()))
            if str(client.get_cnp()) == valoare:
                clientiGasiti.append(client)
            elif str(client.get_id()) == valoare :
                clientiGasiti.append(client)
            elif client.get_nume() == valoare :
                clientiGasiti.append(client)
        if len(clientiGasiti) == 0 :
            raise ValueError("Datele introduse nu corespund nici unui client!")
        else:
            return clientiGasiti

    def printClienti(self):
        for client in self._listaClienti :
            print(client)

    def returnClienti(self):
        lista = []
        for client in self._listaClienti :
            lista.append(client)
        return lista
