#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Raspberry Pi to Arduino I2C Communication
#i2cdetect -y 1
#library
import sys
import smbus2 as smbus#,smbus2
import time
# Slave Addresses
I2C_SLAVE_ADDRESS = 11 #0x0b ou 11
I2C_SLAVE2_ADDRESS = 12
I2C_SLAVE3_ADDRESS = 13
# This function converts a string to an array of bytes.
def ConvertStringsToBytes(src):
  converted = []
  for b in src:
    converted.append(ord(b))
  return converted
def main(args):
    # Create the I2C bus
    I2Cbus = smbus.SMBus(1)
    with smbus.SMBus(1) as I2Cbus:
        slaveSelect = input("Which Arduino (1-3): ")
        cmd = input("Enter command: ")
        if slaveSelect == "1":
            slaveAddress = I2C_SLAVE_ADDRESS
        elif slaveSelect == "2":
            slaveAddress = I2C_SLAVE2_ADDRESS
        elif slaveSelect == "3":
            slaveAddress = I2C_SLAVE3_ADDRESS
        else:
            # quit if you messed up
            print(slaveSelect== "1")
            print(type(slaveSelect))
            print("no slave selected")
            quit()
        BytesToSend = ConvertStringsToBytes(cmd)
        print("Sent " + str(slaveAddress) + " the " + str(cmd) + " command.")
        print(BytesToSend )
        I2Cbus.write_i2c_block_data(slaveAddress, 0x00, BytesToSend)
        time.sleep(0.5)
        while True:
            try:
                data=I2Cbus.read_i2c_block_data(slaveAddress,0x00,16)
                print("recieve from slave:")
                print(data)
            except:
                print("remote i/o error")
                time.sleep(0.5)
    return 0
if __name__ == '__main__':
     try:
        main(sys.argv)
     except KeyboardInterrupt:
        print("program was stopped manually")
     input()


"""
from tkinter import *

Page = 0


window = Tk()
#window.attributes('-fullscreen', True) 


def key(event):
    print ("pressed", repr(event.char))

def callback(event):
    global Page
    Width = event.x
    Height = event.y
    print ("clicked at x : ", Width, "y : ", Height)

    if (640 < Width < 900 and 690 < Height < 730):
        print ("Crédits")



    if (630 < Width < 930 and 300 < Height < 640):
        print ("OK ici")
        Page = 1
        CanvasFond1.pack_forget() 
        CanvasFond2.pack()



def ValiderCube(event):
    Width = event.x
    Height = event.y
    print ("clicked at x : ", Width, "y : ", Height)

    if (1200 < Width < 1430 and 300 < Height < 550):
        print ("Valide both")



    if (110 < Width < 438 and 300 < Height < 550):
        print ("Dismiss both")
        CanvasFond2.pack_forget()



#tabImage = ['D:/Desktop/BOB/.dist/BomboneEntrée.png', 'D:/Desktop/BOB/.dist/test-design-bobone-de-cri-inserer-cubeai.png', 'D:/.Photo/3431885-hollow-knight-review-thumb-nologo.jpg']

print("Canvas 1")
#Canvas page 1
CanvasFond1 = Canvas(window, height=1000, width=1600)
CanvasFond1.pack()
#chemin_Fond = "D:/Desktop/BOB/.dist/BomboneEntrée.png" # Fichier dans le dossier de ce script
Fond = PhotoImage(file="D:/Desktop/BOB/.dist/BomboneEntrée.png") # Création d'une image Tkinter
CanvasFond1.create_image(780,420, image=Fond) # Coordonnées = centre de l'image 

CanvasFond1.bind("<Key>", key)
CanvasFond1.bind("<Button-1>", ValiderCube)
CanvasFond1.pack()



if __name__ == '__main__':
     try:
        print("Outside main")
        main()
     except KeyboardInterrupt:
        print("program was stopped manually")
     input()

     """