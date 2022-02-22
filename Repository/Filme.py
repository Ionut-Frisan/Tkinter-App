
class Film():
    def __init__(self,id,titlu,descriere,gen):
        self._id = id
        self._titlu = titlu
        self._descriere = descriere
        self._gen = gen

    def __eq__(self,other):
        return self._id == other._id

    def __str__(self):
        return "Id: " + str(self._id) + " Titlu: " + self._titlu + " Descriere: " + self._descriere + " Gen: " + self._gen

    def get_id(self):
        return self._id

    def get_titlu(self):
        return self._titlu

    def get_descriere(self):
        return self._descriere

    def get_gen(self):
        return self._gen

    def set_id(self,newId):
        self._id = newId

    def set_titlu(self,newTitlu):
        self._titlu = newTitlu

    def set_descriere(self,newDescriere):
        self._descriere = newDescriere

    def set_gen(self,newGen):
        self._gen = newGen
