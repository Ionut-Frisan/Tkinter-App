
class Client():
    def __init__(self,id,nume,cnp):
        self._id = id
        self._nume = nume
        self._cnp = cnp

    #def __eq__(self, other):
     #   return self._id == other._id

    def __str__(self):
        return "Id: " + str(self._id) + " Cnp: " + str(self._cnp) + " Nume: " + str(self._nume)

    def get_id(self):
        return self._id

    def get_nume(self):
        return self._nume

    def get_cnp(self):
        return self._cnp

    def set_id(self,newid):
        self._id = newid

    def set_cnp(self,newcnp):
        self._cnp = newcnp

    def set_nume(self,newnume):
        self._nume = newnume
