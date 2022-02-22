from Repository.Repo_filme import Repo_film
from Repository.Filme import Film
from cryptography.fernet import Fernet

class Repo_filme_file(Repo_film):
    def __init__(self,filename):
        Repo_film.__init__(self)
        self.filename = filename
        try:
            self.decrypt()
        except:
            pass
        self.loadfromfile()

    """def encrypt(self):
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
            file.close()"""

    def createFilmFromLine(self, line):
        """
        Generate a Film from a line and returns a film
        """
        fields = line.split(" ")
        titluL = fields[1].split("_")
        descriereL = fields[2].split("_")
        titlu = ""
        descriere = ""
        for t in titluL :
            titlu +=t
        for d in descriereL :
            descriere += d

        film = Film(int(fields[0]), titlu, descriere, fields[3])
        return film

    def loadfromfile(self):
        """
        Load films from file
        """
        try:
            ff = open(self.filename,"r")
        except:
            ff = open(self.filename,"x")
        for line in ff :
            if line.strip() == "":
                continue
            film = self.createFilmFromLine(line)
            self._listaFilme.append(cl)
        ff.close()

    def appendToFile(self,film):
        """
        Append a new line to the file, representing the Film film
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










