from tkinter import *

fenetre = Tk()
xEcran = fenetre.winfo_screenwidth()
yEcran = fenetre.winfo_screenheight()
fenetre.attributes('-fullscreen', True)

ecran = 0

canvasBG = Canvas(fenetre, width = xEcran, height = yEcran)
canvasBG.pack()

tabImage = ["../.dist/Accueil.png", 
"../.dist/AccueilClick.png", 
"../.dist/test-design-bobone-de-cri-inserer-cubeai.png", 
"../.dist/AnalyseFin.png", 
"../.dist/AnalyseContinue.png", 
"../.dist/AnalyseStop.png", 
"../.dist/Resolution.png", 
"../.dist/ResolutionClick.png", 
"../.dist/loading.gif"]

"""
tabAnimationWait = ["../.dist/IMG_src/IMG_1.png", 
"../.dist/IMG_src/IMG_2.png", 
"../.dist/IMG_src/IMG_3.png", 
"../.dist/IMG_src/IMG_4.png", 
"../.dist/IMG_src/IMG_5.png", 
"../.dist/IMG_src/IMG_6.png", 
"../.dist/IMG_src/IMG_7.png", 
"../.dist/IMG_src/IMG_8.png", 
"../.dist/IMG_src/IMG_9.png", 
"../.dist/IMG_src/IMG_10.png", 
"../.dist/IMG_src/IMG_11.png", 
"../.dist/IMG_src/IMG_12.png", 
"../.dist/IMG_src/IMG_13.png", 
"../.dist/IMG_src/IMG_14.png", 
"../.dist/IMG_src/IMG_15.png", 
"../.dist/IMG_src/IMG_16.png", 
"../.dist/IMG_src/IMG_17.png", 
"../.dist/IMG_src/IMG_18.png", 
"../.dist/IMG_src/IMG_19.png", 
"../.dist/IMG_src/IMG_20.png", 
"../.dist/IMG_src/IMG_21.png"]

def Loading():
    canvasBG.delete(ALL)
    for i in range(0,20) :
        image = PhotoImage(file=tabAnimationWait[i])
        canvasBG.create_image(xEcran/2, yEcran/2, image=image)
        canvasBG.delete(ALL)
        
   #if validationAlgo == 1:
        #Ecran(3)
"""
validationAlgo = 0
frameCnt = 20
frames = [PhotoImage(file="../.dist/loading.gif",format = 'gif -index %i' %(i)) for i in range(frameCnt)]
def update(ind):

    while validationAlgo == 0:
        frame = frames[ind]
        ind += 1
        if ind == frameCnt:
            ind = 0
        label.configure(image=frame)
        fenetre.after(100, update, ind)
        label = Label(fenetre)
        label.pack()
        fenetre.after(0, update, 0)
    else:
        Ecran(3)




def EcranUnbind(param):
    global ecran
    canvasBG.delete(ALL)
    image = PhotoImage(file=tabImage[param])
    canvasBG.create_image(xEcran/2, yEcran/2, image=image)

    ecran = param

    canvasBG.bind("<ButtonRelease-1>", Event1)

    fenetre.mainloop()

def Event1 (event):
    global ecran
    x = event.x
    y = event.y
    print("Clic détecté en X =" + str(x) +\
                            ", Y =" + str(y))

    if 614<x<920 and 329<y<629 and ecran == 0:
        print("Ecran 0")
        EcranUnbind(1)

    if ecran == 1:
        if 614<x<920 and 329<y<629: 
            print("Ecran 1")
            Ecran(2)
        
        else:
            Ecran(0)

    if ecran == 2:
        if 103<x<304 and 336<y<554:
            print("Back")
            Ecran(0)

        if 1191<x<1410 and 336<y<554:
            print("Next") 
            update()
        
    if ecran == 3:
        if 790<x<920 and 420<y<550:
            print("annuler")
            EcranUnbind(5)

        elif 610<x<740 and 420<y<550:
            print("suivant")  
            EcranUnbind(4)
    
    if ecran == 4:
        print("Elle")
        if 610<x<740 and 420<y<550:
            Ecran(6)
        
        else:
            Ecran(3)

    if ecran == 5:
        if 790<x<920 and 420<y<550:
            Ecran(0)

        else:
            Ecran(3)
    
    if ecran == 6:
        if 1064<x<1204 and 350<y<500:
            EcranUnbind(7)

    if ecran == 7:
        if 1064<x<1204 and 350<y<500:
            Ecran(0)#à remplacer par 0 par la suite
    



def Ecran(param):
    global ecran
    canvasBG.delete(ALL)
    image = PhotoImage(file=tabImage[param])
    canvasBG.create_image(xEcran/2, yEcran/2, image=image)
    ecran = param
    canvasBG.bind("<Button-1>", Event1)
    

    fenetre.mainloop()



 

if __name__ == '__main__':
    Ecran(0) 