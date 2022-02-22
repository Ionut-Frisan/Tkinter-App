from Repository.Clienti import *

class Valid_client():
    def __init__(self):
        pass

    def checkint(self,var):
        try:
            int(var)
        except:
            return 0
        return 1

    def validareClient(self,newClient):
        error = ""
        if (type(newClient.get_id()) != int) or newClient.get_id() <= 0 :
            error +="Id invalid\n"
        if len(newClient.get_nume()) == 0 or self.checkint(newClient.get_nume()) == 1:
            error +="Nume invalid\n"
        if (type(newClient.get_cnp()) != int) or newClient.get_cnp() <= 0:
            error +="Cnp invalid\n"
        if len(error) > 0 :
            raise ValueError(error)

