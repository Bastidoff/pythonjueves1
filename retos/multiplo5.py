#Recibir un numero en teclado y determinar si este es múltiplo de 5

num=input("Ingrese un número para determinar si es múltiplo de 5: ")

if(int(num)%5==0):
    print(f'el número {num} es múltiplo de 5.')
else:
    print(f'el número {num} NO es múltiplo de 5.')
    
