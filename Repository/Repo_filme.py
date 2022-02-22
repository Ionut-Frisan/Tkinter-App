from Repository.Filme import *

class Repo_film():
    def __init__(self):
        self._listaFilme = []

    def adaugaFilm(self,newFilm):
        duplicat = False
        for film in self._listaFilme:
            if film.get_id() == newFilm.get_id():
                duplicat = True

        if duplicat == False :
            self._listaFilme.append(newFilm)
        else:
            raise ValueError("id existent")

    def stergeFilm(self,criteriu,valoare):
        removed = False
        if criteriu == "id" :
            for film in self._listaFilme :
                if film.get_id() == int(valoare) :
                    self._listaFilme.remove(film)
                    removed = True

        if criteriu == "titlu" :
            for film in self._listaFilme :
                if film.get_titlu() == valoare :
                    self._listaFilme.remove(film)
                    removed = True

        if removed == False :
            raise ValueError("Filmul nu este inregistrat !")

    def modificaFilm(self,id,criteriu,valoare):
        if criteriu == "titlu" :
            for i in range(0,len(self._listaFilme)) :
                if self._listaFilme[i].get_id() == id :
                    self._listaFilme[i].set_titlu(valoare)

        if criteriu == "descriere" :
            for i in range(0,len(self._listaFilme)) :
                if self._listaFilme[i].get_id() == id :
                    self._listaFilme[i].set_descriere(valoare)

        if criteriu == "gen" :
            for i in range(0,len(self._listaFilme)) :
                if self._listaFilme[i].get_id() == id :
                    self._listaFilme[i].set_gen(valoare)

    def printFilme(self):
        for film in self._listaFilme:
            print(film)

    def cautaFilm(self,valoare):
        filmeGasite = []
        for film in self._listaFilme :
            if film.get_id() == valoare :
                filmeGasite.append(film)
            if film.get_titlu() == valoare :
                filmeGasite.append(film)
            if film.get_descriere() == valoare :
                filmeGasite.append(film)
            if len(filmeGasite) == 0 :
                raise ValueError("Date invalide !")
            else :
                return filmeGasite


    def printFilme(self):
         for film in self._listaFilme :
             print(film)

    def lenght(self):
        return len(self._listaFilme)

    def get_film(self,index):
        return self._listaFilme[index]



def test_adauga() :
    repotest = Repo_film()
    film1 = Film(1,"Ion","None","Crima")
    repotest.adaugaFilm(film1)
    assert(repotest.lenght() == 1)

def test_sterge() :
    repotest = Repo_film()
    film1 = Film(1, "Ion", "None", "Crima")
    repotest.adaugaFilm(film1)
    repotest.stergeFilm("id",1)
    assert(repotest.lenght() == 0)
    repotest = Repo_film()
    film1 = Film(1, "Ion", "None", "Crima")
    repotest.adaugaFilm(film1)
    repotest.stergeFilm("titlu", "Ion")
    assert (repotest.lenght() == 0)

def test_modifica() :
    repotest = Repo_film()
    film1 = Film(1, "Ion", "None", "Crima")
    repotest.adaugaFilm(film1)
    repotest.modificaFilm(1,"titlu","Mara")
    assert(repotest.get_film(0).get_titlu() == "Mara")
    repotest.modificaFilm(1,"descriere","Mirobolant")
    assert(repotest.get_film(0).get_descriere() == "Mirobolant")
    repotest.modificaFilm(1, "gen", "Comedie")
    assert (repotest.get_film(0).get_gen() == "Comedie")

def run_all_film_tests() :
    test_modifica()
    test_adauga()
    test_sterge()

run_all_film_tests()
