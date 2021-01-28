from tkinter import *

fenetre = Tk()
xEcran = fenetre.winfo_screenwidth()
yEcran = fenetre.winfo_screenheight()
fenetre.attributes('-fullscreen', True)

ecran = 0

canvasBG = Canvas(fenetre, width = xEcran, height = yEcran)
canvasBG.pack()

tabImage = ["D:/Desktop/BOB/.dist/Accueil.png", 
"D:/Desktop/BOB/.dist/AccueilClick.png", 
"D:/Desktop/BOB/.dist/test-design-bobone-de-cri-inserer-cubeai.png", 
"D:/Desktop/BOB/.dist/AnalyseFin.png", 
"D:/Desktop/BOB/.dist/AnalyseContinue.png", 
"D:/Desktop/BOB/.dist/AnalyseStop.png", 
"D:/Desktop/BOB/.dist/Resolution.png", 
"D:/Desktop/BOB/.dist/ResolutionClick.png"]

def Event1 (event):
    global ecran
    x = event.x
    y = event.y
    print("Clic détecté en X =" + str(x) +\
                            ", Y =" + str(y))


def Ecran(param):
    global ecran
    canvasBG.delete(ALL)
    image = PhotoImage(file=tabImage[6])
    canvasBG.create_image(xEcran/2, yEcran/2, image=image)
    ecran = param
    canvasBG.bind("<Button-1>", Event1)
    

    fenetre.mainloop()



 

if __name__ == '__main__':
    Ecran(0) 