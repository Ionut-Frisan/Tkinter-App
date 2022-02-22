
class Service_clienti():
    def __init__(self,RepoC,ValidC):
        self.RepoC = RepoC
        self.ValidC = ValidC

    def adaugaClient(self,newClient):
        self.ValidC.validareClient(newClient)
        self.RepoC.adaugaClient(newClient)

    def stergeClient(self,criteriu,valoare):
        self.RepoC.stergeClient(criteriu,valoare)

    def modificaClient(self,id,criteriu,valoare):
        self.RepoC.modificaClient(id,criteriu,valoare)

    def modificaClientGUI(self,id,newname,newcnp):
        self.RepoC.modificaClientGUI(id,newname,newcnp)

    def cautaClient(self,valoare):
        return self.RepoC.cautaClient(valoare)

    def printClienti(self):
        self.RepoC.printClienti()

    def returnClienti(self):
        return self.RepoC.returnClienti()