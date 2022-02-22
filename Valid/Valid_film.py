from Repository.Filme import *

class Valid_film():
    def __init__(self):
        pass

    def validareFilm(self,newFilm):
        error = ""
        if (type(newFilm.get_id()) != int) or newFilm.get_id() <= 0 :
            error += "Id invalid\n"
        if len(newFilm.get_titlu()) == 0 :
            error += "Nume invalid\n"
        if len(newFilm.get_descriere()) == 0 :
            error += "Descriere invalida\n"
        if len(newFilm.get_gen()) == 0 :
            error += "Gen invalid\n"
        if len(error) > 0 :
            raise ValueError(error)
