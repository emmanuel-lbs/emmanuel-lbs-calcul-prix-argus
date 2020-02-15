
from tkinter  import *


def buttonEssence():
    main.destroy() #detruit main
    Essence() # et puis lance fct essence
def Essence():
    #creation des fenetre graphique
    Essence= Tk()

    # I personalisations:
    Essence.title("modele essence ")# titre
    Essence.geometry("2000x1000")#taille
    Essence.config(background="#41B77F")

    mega=Frame(Essence,bg="#41B77F")#Frame=boite ou on met tout dedans

    fratexte=Frame(mega,bg="#41B77F",pady=50)
    boite=Frame(mega,bg="#41B77F")
    boite2=Frame(mega,bg="#41B77F")
    boite3=Frame(mega,bg="#41B77F")




    Q1=Label(fratexte,text="Quel est le modele de votre voiture a essence ?",font=("Courrier",40),bg=("#41B77F"),fg=("black")) #text question basique
    Q1.pack(expand=YES,side=TOP)


    #ajouter des Buttons partout

    #colone 1 dans frame boite
    modele= Button(boite,text="Renault Clio 4",font=("Courrier",20),bg=("white"),fg=("black"),width=20,command=a) #button qui lance fct
    modele.pack(pady=10,padx=10)
    modele= Button(boite,text="Renault Captur",font=("Courrier",20),bg=("white"),fg=("black"),width=20,command=b)
    modele.pack(pady=10,padx=10)
    modele= Button(boite,text="Citroen C3 (3ème gen)",font=("Courrier",20),bg=("white"),fg=("black"),width=20,command=c)
    modele.pack(pady=10,padx=10)


    #colone 2 dans frame boite2
    modele= Button(boite2,text="Citroen C1 (2ème gen)",font=("Courrier",20),bg=("white"),fg=("black"),width=20,command=d)
    modele.pack(pady=10,padx=10)
    modele= Button(boite2,text="Peugeot 3008",font=("Courrier",20),bg=("white"),fg=("black"),width=20,command=e)
    modele.pack(pady=10,padx=10)
    modele= Button(boite2,text="BMW série 3 coupée",font=("Courrier",20),bg=("white"),fg=("black"),width=20,command=f)
    modele.pack(pady=10,padx=10)


    #colone 3 dans frame boite3
    modele= Button(boite3,text="Opel Corsa 5",font=("Courrier",20),bg=("white"),fg=("black"),width=20,command=g)
    modele.pack(pady=10,padx=10)
    modele= Button(boite3,text="Golf 7 GTI cabriolet",font=("Courrier",20),bg=("white"),fg=("black"),width=20,command=h)
    modele.pack(pady=10,padx=10)
    modele= Button(boite3,text="Toyota Yaris 3",font=("Courrier",20),bg=("white"),fg=("black"),width=20,command=i)
    modele.pack(pady=10,padx=10)






    #afficher les boites
    fratexte.pack(expand=YES,side=TOP)

    boite.pack(expand=YES , side=LEFT)
    boite2.pack(expand=YES,side=LEFT)
    boite3.pack(expand=YES, side=LEFT)
    mega.pack(expand=YES ,)

    Essence.mainloop()

def a(x=16200):
    findPriceEssence(x,date,Km)
def b(x=21450):
    findPriceEssence(x,date,Km)
def c(x=17900):
    findPriceEssence(x,date,Km)
def d(x=12700):
    findPriceEssence(x,date,Km)
def e(x=30100):
    findPriceEssence(x,date,Km)
def f(x=39200):
    findPriceEssence(x,date,Km)
def g(x=13800):
    findPriceEssence(x,date,Km)
def h(x=40390):
    findPriceEssence(x,date,Km)
def i(x=15300):
    findPriceEssence(x,date,Km)

def findPriceEssence(prix,date,Km):
    A=2020-date


    b=5

    if A==1:
        print("a sa sortie votre voiture couter",prix )
        prix=prix*0.80
        print("apres 1 an votre voiture couta " ,prix)
    if A==2:
        print("a sa sortie votre voiture couter",prix )
        prix=prix*0.80
        print("apres 1 an votre voiture couta " ,prix)
        prix=prix*0.82
        print("apres 2 an votre voiture couta " ,prix)
    if A==3:
        print("a sa sortie votre voiture couter",prix )
        prix=prix*0.80
        print("apres 1 an votre voiture couta " ,prix)
        prix=prix*0.82
        print("apres 2 an votre voiture couta " ,prix)
        prix=prix*0.85
        print("apres 3 an votre voiture couta ", prix)
    if A==4:
        print("a sa sortie votre voiture couter",prix )
        prix=prix*0.80
        print("apres 1 an votre voiture couta " ,prix)
        prix=prix*0.82
        print("apres 2 an votre voiture couta " ,prix)
        prix=prix*0.85
        print("apres 3 an votre voiture couta ", prix)
        prix=prix*0.88
        print("apres 4 an votre voiture couta " ,prix)
    if A>=5:
        print("a sa sortie votre voiture couter",prix )
        prix=prix*0.80
        print("apres 1 an votre voiture couta " ,prix)
        prix=prix*0.82
        print("apres 2 an votre voiture couta " ,prix)
        prix=prix*0.85
        print("apres 3 an votre voiture couta ", prix)
        prix=prix*0.88
        print("apres 4 an votre voiture couta " ,prix)
        while A!=4:
            prix=prix*0.90

            A=A-1
            print("apres",b,"ans votre voiture couter",prix )
            b=b+1
        print("aujhourd'hui votre voiture coute ",prix)


    A=2020-date
    maxkm=A*15000



    if Km<maxkm :
        while Km<maxkm  :
            Km= Km+1000
            prix=prix*1.25

    if Km>maxkm :
        while Km>maxkm:
            Km= Km-1000
            prix=prix*0.5

    prix=int(prix)
    Prix(prix)









######################                          Bloc 2






def buttonGasoil():
    main.destroy()
    gasoil()
def gasoil():
    #creation des fenetre graphique
    Gasoil= Tk()

    # I personalisations:

    Gasoil.title("modele gasoil")# titre
    Gasoil.geometry("2000x1000")
    Gasoil.config(background="#41B77F")

    mega=Frame(Gasoil,bg="#41B77F")

    fratexte=Frame(mega,bg="#41B77F",pady=50)
    boite=Frame(mega,bg="#41B77F")
    boite2=Frame(mega,bg="#41B77F")




    Question=Label(fratexte,text="Quel est le modele de votre voiture Gasoil ?",font=("Courrier",40),bg=("#41B77F"),fg=("black"))
    Question.pack(expand=YES,side=TOP)

    #ajouter un bouton
    modele= Button(boite,text="Renault Clio 4",font=("Courrier",20),bg=("white"),fg=("black"),width=20,command=j)
    modele.pack(pady=10,padx=10)
    modele= Button(boite,text="Renault Captur",font=("Courrier",20),bg=("white"),fg=("black"),width=20,command=k)
    modele.pack(pady=10,padx=10)
    modele= Button(boite,text="Citroen C3 (3ème gen)",font=("Courrier",20),bg=("white"),fg=("black"),width=20,command=l)
    modele.pack(pady=10,padx=10)

    modele= Button(boite2,text="Peugeot 3008",font=("Courrier",20),bg=("white"),fg=("black"),width=20,command=m)
    modele.pack(pady=10,padx=10)
    modele= Button(boite2,text="BMW série 3 coupée",font=("Courrier",20),bg=("white"),fg=("black"),width=20,command=n)
    modele.pack(pady=10,padx=10)
    modele= Button(boite2,text="Opel Corsa 5",font=("Courrier",20),bg=("white"),fg=("black"),width=20,command=o)
    modele.pack(pady=10,padx=10)





    #afficher les boites
    fratexte.pack(expand=YES,side=TOP)
    mega.pack(expand=YES ,)
    boite.pack(expand=YES , side=LEFT)
    boite2.pack(expand=YES,side=LEFT)


    #ouvrir fenetre
    Gasoil.mainloop()

def j(x=18100):
    findPriceAutres(x,date,Km)
def k(x=25850):
     findPriceAutres(x,date,Km)
def l(x=21050):
     findPriceAutres(x,date,Km)
def m(x=35800):
     findPriceAutres(x,date,Km)
def n(x=39700):
     findPriceAutres(x,date,Km)
def o(x=16850):
     findPriceAutres(x,date,Km)

def findPriceAutres(prix,date,Km):
    A=2020-date
    print(A)

    b=5

    if A==1:
        print("a sa sortie votre voiture couter",prix )
        prix=prix*0.80
        print("apres 1 an votre voiture couta " ,prix)
    if A==2:
        print("a sa sortie votre voiture couter",prix )
        prix=prix*0.80
        print("apres 1 an votre voiture couta " ,prix)
        prix=prix*0.82
        print("apres 2 an votre voiture couta " ,prix)
    if A==3:
        print("a sa sortie votre voiture couter",prix )
        prix=prix*0.80
        print("apres 1 an votre voiture couta " ,prix)
        prix=prix*0.82
        print("apres 2 an votre voiture couta " ,prix)
        prix=prix*0.85
        print("apres 3 an votre voiture couta ", prix)
    if A==4:
        print("a sa sortie votre voiture couter",prix )
        prix=prix*0.80
        print("apres 1 an votre voiture couta " ,prix)
        prix=prix*0.82
        print("apres 2 an votre voiture couta " ,prix)
        prix=prix*0.85
        print("apres 3 an votre voiture couta ", prix)
        prix=prix*0.88
        print("apres 4 an votre voiture couta " ,prix)
    if A>=5:
        print("a sa sortie votre voiture couter",prix )
        prix=prix*0.80
        print("apres 1 an votre voiture couta " ,prix)
        prix=prix*0.82
        print("apres 2 an votre voiture couta " ,prix)
        prix=prix*0.85
        print("apres 3 an votre voiture couta ", prix)
        prix=prix*0.88
        print("apres 4 an votre voiture couta " ,prix)
        while A!=4:
            prix=prix*0.90

            A=A-1
            print("apres",b,"ans votre voiture couter",prix )
            b=b+1
        print("aujhourd'hui votre voiture coute ",prix)


    A=2020-date
    maxkm=A*25000


    if Km<maxkm :
        while Km<maxkm  :
            Km= Km+1000
            prix=prix*1.25


    if Km>maxkm :
        while Km>maxkm:
            print(prix)
            Km= Km-1000
            prix=prix*0.5



    prix=int(prix)
    Prix(prix)






def buttonHybride():
    main.destroy() #detruit main
    findPriceAutres(21150,date,Km) # et puis lance fct Prix direct car 1 seule modele possible






def etat ():
    prix =16200
    date=int(input("en quel annee avez vous acheter votre voiture ?"))
    Km=int(input("combien de kilometres avez vous parcouru avec  ?"))
    #2 input pou connaitre le km et l'annee d'achat


    #creation des fenetre graphique
    etat= Tk()

    # I personalisations:

    etat.title("etat")# titre
    etat.geometry("2000x1000") #taile de base
    etat.config(background="#41B77F")

    frame=Frame(etat,bg="#41B77F") #frame=boite ou on met tout ce qu'on veux afficher dedans


    Q=Label(frame,text="quel est l'etat de votre voiture ?",font=("Courrier",40),bg=("#41B77F"),fg=("black"),pady=50) #text
    Q.pack(expand=YES,side=TOP)



    Bo= Button(frame,text="Essence",font=("Courrier",20),bg=("white"),fg=("black"),width=20,command=Prix(prix)) #button
    Bo.pack(pady=20,padx=10)  #affecter a frame
    Mo= Button(frame,text="Gasoil",font=("Courrier",20),bg=("white"),fg=("black"),width=20,command=Prix(prix))  #button
    Mo.pack(pady=20,padx=10)  #affecter a frame
    Ma= Button(frame,text="Hybride",font=("Courrier",20),bg=("white"),fg=("black"),width=20,command=Prix(prix))  #button
    Ma.pack(pady=20,padx=10)   #affecter a frame



    #afficher la boites
    frame.pack(expand=YES ) #affceter frame au etat

    #ouvrir fenetre
    etat.mainloop() # ouvrir etat
def Bon (prix) :
    prix= prix*1
    Prix(prix)
def Moyen (prix) :
    prix= prix*0.95
    Prix(prix)
def Mauvais (prix) :
    prix= prix*0.90
    Prix(prix)


def Prix(prix):



    #creation des fenetre graphique
    FIN= Tk()

    # I personalisations:

    FIN.title("modele essence ")# titre
    FIN.geometry("2000x1000")
    FIN.config(background="#41B77F")


    print(prix)


    frame=Frame(FIN,bg="#41B77F")
    fini=( "le prix d'occasion votre Argus est de ",prix,"€")

    modele=Label(frame,text=fini,font=("Courrier",40),bg=("#41B77F"),fg=("black"),pady=50)
    modele.pack(expand=YES,side=TOP)




    #afficher les boites
    frame.pack(expand=YES )

    #ouvrir fenetre
    FIN.mainloop()



date=int(input("en quel annee avez vous acheter votre voiture ?"))
Km=int(input("combien de kilometres avez vous parcouru avec  ?"))
#2 input pou connaitre le km et l'annee d'achat


#creation des fenetre graphique
main= Tk()

# I personalisations:

main.title("main")# titre
main.geometry("2000x1000") #taile de base
main.config(background="#41B77F")

frame=Frame(main,bg="#41B77F") #frame=boite ou on met tout ce qu'on veux afficher dedans


modele=Label(frame,text="A quoi fonctione votre voiture ?",font=("Courrier",40),bg=("#41B77F"),fg=("black"),pady=50) #text
modele.pack(expand=YES,side=TOP)



E= Button(frame,text="Essence",font=("Courrier",20),bg=("white"),fg=("black"),width=20,command=buttonEssence) #button
E.pack(pady=20,padx=10)  #affecter a frame
G= Button(frame,text="Gasoil",font=("Courrier",20),bg=("white"),fg=("black"),width=20,command=buttonGasoil)  #button
G.pack(pady=20,padx=10)  #affecter a frame
H= Button(frame,text="Hybride",font=("Courrier",20),bg=("white"),fg=("black"),width=20,command=buttonHybride)  #button
H.pack(pady=20,padx=10)   #affecter a frame



#afficher la boites
frame.pack(expand=YES ) #affecter frame au main

#ouvrir fenetre
main.mainloop() # ouvrir main
