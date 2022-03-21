import pyfirmata
import time

board = pyfirmata.Arduino('COM3')
print("Conectado")

print("Ingrese la letra de su teclado en mayuscula")
encender = input().upper()

def luz():

    if encender == 'AY':
        board.digital[12].write(1)
        board.digital[8].write(1)
        time.sleep(.5)
        board.digital[12].write(0)
        board.digital[8].write(0)
        time.sleep(.5)

while True:
    luz()


        
    
       


