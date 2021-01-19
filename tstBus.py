#library
import sys
import smbus2 as smbus    # bibliothèque pour la communication
import time

#adresse des modules
I2C_SLAVE_ADRESS = 11   #adresse de l'arduino esclave, en rajouer autant qu'il y a d'esclaves

print("begin")

def ConvertStringToByte(src):
    """converted = []
    for b in src:
        converted.append(ord(b))
    return converted"""
    


def main():
    I2Cbus = smbus.SMBus(1)   #création du bus I2C
    with smbus.SMBus(1) as I2Cbus:
        cmd = input("Entrer une commande : ")
    
    BytesToSend = ConvertStringToByte(cmd)
    print("Send " + str(I2C_SLAVE_ADRESS) + " the " + str(cmd) + " command.")
    print(BytesToSend)
    I2Cbus.write_i2c_block_data(I2C_SLAVE_ADRESS, 0x00, BytesToSend)   #Envoi de l'information avec adresse du récepteur, adresse de l'émetteur et message
    
    
    
    while True:
        try:
            data = I2Cbus.read_i2c_block_data(slaveAdress, 0x00, 16)  #Récupération de l'information sur un nombre de byte défini
            print("Message receive : " + str(data))
            
        except:
            print("Reception error")
            input()
    return 0       
    
        
    

if __name__ == '__main__':
    print("Main")
    try:
        main()
        
    except KeyboardInterupt:
        print ("ERROR")
        
    input()