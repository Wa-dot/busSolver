import tkinter as tk

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
        ButtonBonus = Button(self.window, text = "Lancer la résolution", command = communication(1))
        
        
        
def command(order):
    if order == 1:
        print("<bouton push")
        
        
        

if __name__ == '__main__':
    app = FullscreenMenu() 