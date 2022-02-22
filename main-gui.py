from Valid.Valid_film import *
from Valid.Valid_client import *
from GUI.GUI import *
from Repository.Repo_clienti import *
from Repository.Repo_filme import *
from Service.Service_filme import *
from Service.Service_clienti import *
from Repository.Repo_clienti_file import Repo_clienti_file

repoC = Repo_clienti_file("Repository/Clienti.txt")
repoF = Repo_film()
validC = Valid_client()
validF = Valid_film()
servC = Service_clienti(repoC,validC)
servF = Service_filme(repoF,validF)


if __name__ == '__main__' :
    GUI(servF,servC).mainloop()
