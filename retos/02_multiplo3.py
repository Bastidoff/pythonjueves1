#Recibir un múmero en teclado y determinar si este es múltiplo de 3

numero=input("Ingrese un número para saber si es múltiplo de 3: ")

if(int(numero)%3==0):
    print(f'El número {numero} es múltiplo de 3.')
else:
    print(f'El número {numero} NO es múltiplo de 3.')

