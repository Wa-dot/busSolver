from tkinter import *

fenetre = Tk()
xEcran = fenetre.winfo_screenwidth()
yEcran = fenetre.winfo_screenheight()
fenetre.attributes('-fullscreen', True)

ecran = 0

canvasBG = Canvas(fenetre, width = xEcran, height = yEcran)
canvasBG.pack()

print ("begin")





def Event3(event):
    x = event.x
    y = event.y
    print("Clic détecté en X =" + str(x) +\
                            ", Y =" + str(y))
    print("X ecran = "+ str(xEcran) + ", Y ecran = " + str(yEcran))
    if 103<x<304 and 336<y<554:
        print("Annuler")
        Ecran1()

#ecran pour insérer le cube
def Ecran3():
    canvasBG.delete(ALL)
    image = PhotoImage(file="D:/Desktop/BOB/.dist/test-design-bobone-de-cri-inserer-cubeai.png")
    canvasBG.create_image(xEcran/2, yEcran/2, image=image)

    canvasBG.bind("<Button-1>", Event3)

    fenetre.mainloop()


def Event2(event):
    x = event.x
    y = event.y
    print("Clic détecté en X =" + str(x) +\
                            ", Y =" + str(y))
    print("X ecran = "+ str(xEcran) + ", Y ecran = " + str(yEcran))
    if 103<x<304 and 336<y<554:
        print("Annuler")
        Ecran1()

    if 1191<x<1410 and 336<y<554:
        print("Suivant")  
        Ecran3()
        

#ecran d'accueil appuie
def Ecran2():
    canvasBG.delete(ALL)
    image = PhotoImage(file="D:/Desktop/BOB/.dist/test-design-bobone-de-cri-inserer-cubeai.png")
    canvasBG.create_image(xEcran/2, yEcran/2, image=image)

    canvasBG.bind("<Button-1>", Event2)

    fenetre.mainloop()


def Event1_5 (event):
    x = event.x
    y = event.y
    if 614<x<920 and 329<y<629:
        print("Good")
        Ecran2()


#ecran d'accueil
def Ecran1_5():
    canvasBG.delete(ALL)
    image = PhotoImage(file="D:/Desktop/BOB/.dist/AccueilClick.png")
    canvasBG.create_image(xEcran/2, yEcran/2, image=image)

    canvasBG.bind("<ButtonRelease-1>", Event1_5)

    fenetre.mainloop()


def Event1 (event):
    x = event.x
    y = event.y
    print("Clic détecté en X =" + str(x) +\
                            ", Y =" + str(y))
    if 614<x<920 and 329<y<629:
        print("Good")
        Ecran1_5()



def Ecran1():
    canvasBG.delete(ALL)
    image = PhotoImage(file="D:/Desktop/BOB/.dist/Accueil.png")
    canvasBG.create_image(xEcran/2, yEcran/2, image=image)

    canvasBG.bind("<Button-1>", Event1)

    fenetre.mainloop()

 

if __name__ == '__main__':
    Ecran1() 