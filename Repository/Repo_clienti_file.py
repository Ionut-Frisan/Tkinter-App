#from cryptography.fernet import Fernet
from Repository.Repo_clienti import Repo_clienti
from Repository.Clienti import Client

class Repo_clienti_file(Repo_clienti):
    def __init__(self,filename):
        Repo_clienti.__init__(self)
        self.filename = filename
        try:
            self.decrypt()
        except:
            pass
        self.loadfromfile()

    def encrypt(self):
        key = Fernet.generate_key()
        with open('Repository\key.key', 'wb') as f:
            f.write(key)

        with open(self.filename, "rb") as f:
            data = f.read()

        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)

        with open('Repository\Clienti.txt', "wb") as f:
            f.write(encrypted)

    def decrypt(self):
        with open('Repository\key.key','rb') as f:
            key = f.read()
            f.close()

        with open(self.filename, "rb+") as f:
            data = f.read()


        fernet = Fernet(key)
        decrypted = fernet.decrypt(data)

        decrypted = decrypted.decode()
        decrypted = str(decrypted)
        with open("Repository\Clienti.txt","w") as file:
            file.write(decrypted)
            file.flush()
            file.close()



    def createClientFromLine(self, line):
        """
        Generates a Client from a line and returns a Client Object
        """
        fields = line.split(" ")
        nume = fields[1].split("_")
        numeCl = ""
        for i in range(len(nume)):
            if i == len(nume)-1 :
                numeCl +=nume[i]
            else:
                numeCl += nume[i] +" "
        Cl = Client(int(fields[0]), numeCl, int(fields[2]))
        return Cl

    def loadfromfile(self):
        """
        Load clients from file
        """
        try:
            fc = open(self.filename,"r")
        except:
            fc = open(self.filename,"x")
        for line in fc :
            if line.strip() == "":
                continue
            cl = self.createClientFromLine(line)
            self._listaClienti.append(cl)
        fc.close()

    def appendToFile(self,cl):
        """
        Append a new line to the file, representing the Client cl
        """
        fc = open(self.filename,"a")
        numeL = cl.get_nume()
        numeL = numeL.split(" ")
        print(numeL)
        nume = ""
        for i in range(len(numeL)):
            if i != len(numeL)-1:
                nume+=numeL[i]+"_"
            else:
                nume+=numeL[i]

        line = str(cl.get_id())+" "+nume+" "+str(cl.get_cnp())
        fc.write("\n")
        fc.write(line)
        fc.close()

    def updatefile(self):
        """
        Rewrites the file with the current Clients
        """
        fc = open(self.filename, "w")

        for cl in self._listaClienti :
            numeL = cl.get_nume()
            numeL = numeL.split(" ")
            print(numeL)
            nume = ""
            print(len(numeL))
            for i in range(len(numeL)):
                if i != len(numeL) - 1:
                    nume += numeL[i] + "_"
                else:
                    nume += numeL[i]

            line = str(cl.get_id()) + " " + nume + " " + str(cl.get_cnp())
            fc.write("\n")
            fc.write(line)
        fc.close()

    def adaugaClient(self,newClient):
        Repo_clienti.adaugaClient(self,newClient)
        self.appendToFile(newClient)

    def stergeClient(self,criteriu, valoare):
        Repo_clienti.stergeClient(self,criteriu, valoare)
        self.updatefile()

    def modificaClientGUI(self,id,criteriu,valoare):
        Repo_clienti.modificaClientGUI(self,id, criteriu, valoare)
        self.updatefile()