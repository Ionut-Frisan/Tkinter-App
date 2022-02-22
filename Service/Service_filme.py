

class Service_filme():
    def __init__(self,RepoF,ValidF):
        self.RepoF = RepoF
        self.ValidF  = ValidF

    def adaugaFilm(self,newFilm):
        self.ValidF.validareFilm(newFilm)
        self.RepoF.adaugaFilm(newFilm)

    def stergeFilm(self,criteriu,valoare):
        self.RepoF.stergeFilm(criteriu,valoare)

    def modificaFilm(self,id,criteriu,valoare):
        self.RepoF.modificaFilm(id,criteriu,valoare)

    def cautaFilm(self,valoare):
        return self.RepoF.cautaFilm(valoare)

    def printFilme(self):
        self.RepoF.printFilme()

