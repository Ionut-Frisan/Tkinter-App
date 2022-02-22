import tkinter as tk
from Repository.Clienti import *
from tkinter import messagebox
from tkinter import ttk

class GUI(tk.Tk):
    def __init__(self, servF, servC):
        super().__init__()
        self.geometry("500x600")
        self.title("New  H  I  T  2020")
        self.servF = servF
        self.servC = servC
        self.printoptions()
        self.printCl(self)
        self.rowconfigure(0,weight=2)
        self.columnconfigure(0,weight=2)
        self.resizable(width=False, height=False)
        self.remapclosebutton()

    #Client Functionalities
    def removeTextFromEntry(self,entry):
        string = tk.StringVar()
        string = str(entry.get())
        if string == "Introduceti id-ul/numele/Cnp-ul cautat" or string == "ex: 10234589213456" or string == "ex: Mirciulica Bambilica" or string == "ex: 1" :
            entry.delete(0,'end')

    def printoptions(self):
        #generates the page that contains the options for clients add/remove/modify/search
        self.LabelOptiuni = tk.LabelFrame(self)
        #self.LabelOptiuni.grid_rowconfigure(0, weight=1)
        #self.LabelOptiuni.grid_columnconfigure(0, weight=1)

        self.id = tk.ttk.Entry(self.LabelOptiuni, justify="center", width=40)
        self.nume = tk.ttk.Entry(self.LabelOptiuni, justify="center", width=40)
        self.cnp = tk.ttk.Entry(self.LabelOptiuni, justify="center", width=40)
        idlabel = tk.Label(self.LabelOptiuni,text=" Id ", justify="center")
        numelabel = tk.Label(self.LabelOptiuni, text=" Nume ", justify="center")
        cnplabel = tk.Label(self.LabelOptiuni, text=" Cnp ", justify="center")
        cautalabel = tk.Label(self.LabelOptiuni, text="Cauta Client",justify="center")

        self.id.insert(0, "ex: 1")
        self.nume.insert(0, "ex: Mirciulica Bambilica")
        self.cnp.insert(0, "ex: 10234589213456")
        self.id.bind('<Button-1>',lambda x :self.removeTextFromEntry(self.id))
        self.nume.bind('<Button-1>', lambda x: self.removeTextFromEntry(self.nume))
        self.cnp.bind('<Button-1>', lambda x: self.removeTextFromEntry(self.cnp))

        self.id.grid(row=0, column=1,columnspan=2, sticky="w",padx=10,pady=10)
        self.nume.grid(row=1, column=1,columnspan=2, sticky="w",padx=10,pady=10)
        self.cnp.grid(row=2, column=1,columnspan=2, sticky="w",padx=10,pady=10)
        idlabel.grid(row=0,column=0,padx=10,pady=10)
        numelabel.grid(row=1, column=0,padx=10,pady=10)
        cnplabel.grid(row=2, column=0,padx=10,pady=10)
        cautalabel.grid(row=4,column=0,padx=10,pady=10)

        self.valcauta = tk.ttk.Entry(self.LabelOptiuni,justify="center", width=40)
        self.valcauta.insert(0,"Introduceti id-ul/numele/Cnp-ul cautat")
        self.valcauta.bind('<Button-1>', lambda x: self.removeTextFromEntry(self.valcauta))
        self.valcauta.grid(row=4,columnspan=2,column=1,sticky="we",padx=10,pady=10)
        #Buttons
        self.buttonaddCl = tk.ttk.Button(self.LabelOptiuni, text="Adauga client", command=lambda : self.AdaugaCl(self,self.id.get(), self.nume.get().capitalize(),self.cnp.get()))
        self.buttoncautaCl = tk.ttk.Button(self.LabelOptiuni, text="Cauta client", command=lambda: self.cautaCl())
        self.buttonmodCl = tk.ttk.Button(self.LabelOptiuni, text="Modifica Client", command= lambda:self.ModificaCl(self.nume.get(), self.cnp.get()))
        self.buttonstergeCl = tk.ttk.Button(self.LabelOptiuni, text="Sterge Client", command= self.StergeCl)

        self.buttonstergeCl.grid(row=3, column=0,padx=10,pady=10)
        self.buttonmodCl.grid(row=3, column=2,padx=10,pady=10)
        self.buttoncautaCl.grid(column=3, row=4,padx=10,pady=1)
        self.buttonaddCl.grid(row=3, column=1,padx=10,pady=10)
        self.LabelOptiuni.grid(row=1,column=0,padx=10,pady=10)

    def AdaugaCl(self,frame,id,nume,cnp):
        try:
            idVal = tk.IntVar()
            cnpVal = tk.IntVar()
            idVal = id
            cnpVal= cnp
            idVal = int(idVal)
            cnpVal = int(cnpVal)
            newCl = Client(idVal, nume, cnpVal)
            self.servC.adaugaClient(newCl)
            self.printCl(frame)
        except ValueError as ve:
            tk.messagebox.showinfo("Date invalide !",ve)
       # except TypeError :
           # print("eroare")

    def StergeCl(self):
        try:
            id = 0
            for value in self.tree.selection():
                valoare = self.tree.item(value)['values']
                id = valoare[0]
                self.servC.stergeClient("id",int(id))
            self.printCl(self)
        except ValueError as ve:
            tk.messagebox.showinfo("!!! Eroare fraiere !!!",ve)

    def ModificaCl(self,nume,cnp):
        try:
            id = 0
            count = 0
            for value in self.tree.selection():
                valoare = self.tree.item(value)['values']
                id = valoare[0]
                count+=1
            if count == 1:
                self.modificaCl(int(id), nume, cnp)
            else:
                raise ValueError("Va rugam sa selectati cel putin un client si in acelasi timp maxim un client !")
        except ValueError as ve :
            tk.messagebox.showinfo("!!! Eroare fraiere !!!",ve)

    def checkInt(self,var):
        #return 1 if var is int or it is a string with a number value ,return 0 otherwise
        try:
            int(var)
        except:
            return 0
        return 1

    def modificaCl(self,id,newName,newCnp):
        try:
            if(len(str(newName)) == 0):
                raise ValueError("Numele nu poate sa fie nul!")
            if self.checkInt(newName) :
                raise ValueError("Numele nu poate fi un numar!")
            if self.checkInt(newCnp) == 0:
                raise ValueError("Cnp-ul trebuie sa fie un numar")
            self.servC.modificaClientGUI(id,str(newName).capitalize(),int(newCnp))
            self.printCl(self)
        except ValueError as ve:
            tk.messagebox.showinfo("Error",ve)


    def printCl(self,frame,*args):
        #afiseaza toti clientii memorati, optiunea de a-i sterge si de a-i modifica
        if args:
            lista = args[0]
            frameCl = tk.LabelFrame(frame, text="Clienti gasiti", padx=3, pady=3, width=400)
        else:
            lista = self.servC.returnClienti()
            frameCl = tk.LabelFrame(frame, text="Clienti", padx=3, pady=3, width=400)
        frameCl.grid(row=0, column=0, columnspan=5, sticky="NWSE",padx=10,pady=10)

        self.tree = ttk.Treeview(frameCl,displaycolumns='#all')
        self.tree["column"]=("id","nume","cnp")
        self.tree.column("#0", minwidth=40, width=50)
        self.tree.column("id", minwidth=80, width=133, anchor=tk.CENTER)
        self.tree.column("nume", minwidth=80, width=133, anchor=tk.CENTER)
        self.tree.column("cnp", minwidth=80, width=133, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading("#0", text="Nr crt")
        self.tree.heading("id", text="Id ")
        self.tree.heading("nume", text="Nume ")
        self.tree.heading("cnp", text="Cnp ")

        count = 0

        frameCl.columnconfigure(0,weight=1)
        frameCl.rowconfigure(0,weight=1)
        for cl in lista:
            id = cl.get_id()
            nume = cl.get_nume()
            cnp = cl.get_cnp()
            iid = self.tree.insert("", count, iid='Row %s'%count, text=str(count+1), values=(id,nume,cnp))
            count +=1

        self.tree.grid(row=0,column=0)


    def cautaCl(self):
        val = tk.StringVar()
        val = self.valcauta.get()
        try:
            clienti = self.servC.cautaClient(val)
        except ValueError:
            clienti = []
        self.printCl(self,clienti)

    def DontTellAnybodyButThisFunctionWillEncryptTheFileWhenClosingTheApp(self):
        self.servC.RepoC.encrypt()
        self.destroy()

    def remapclosebutton(self):
        #self.protocol('WM_DELETE_WINDOW',self.doSomething)
        pass




#TODO add all the film functionalities
#
