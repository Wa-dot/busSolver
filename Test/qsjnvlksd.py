import tkinter as tk


       
def command(order):
    if order == 1:
        print("<bouton push")


class FullscreenMenu:
    def __init__(self):
        self.window = tk.Tk()
        self.window.attributes('-fullscreen', True)  
        self.fullScreenState = False
        self.window.bind("<F11>", self.toggleFullScreen)
        self.window.bind("<Escape>", self.quitFullScreen)

        self.window.mainloop()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)
        
        
    def buttonStart(self):
        ButtonBonus = Button(self, text ="Lancer", command = command(1))
        ButtonBonus.grid(row=1,column=0, padx = 5, pady = 5)
        
        
 
        
        
        

if __name__ == '__main__':
    app = FullscreenMenu() 




"""
        X_validate = True

    if (300 < Height < 550):
        print("Valide y")
        Y_validate = True

    if (X_validate == Y_validate == True):
        print("Valide both")
        

#CanvasFondu = Button(window, height=210, width=210, bg="blue")
#CanvasFondu.place(relx=0.85, rely=0.5, anchor=CENTER)
"""