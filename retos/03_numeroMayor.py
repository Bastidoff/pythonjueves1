#Recibir dos números y determinar cual es mayor
print("Este programa permite estabecer el número mayor de dos números ingresados.")
numero1=input("Ingrese el prímer número: ")
numero2=input("Ingrese el segundo número: ")


if(int(numero1)==int(numero2)):
    print(f'Los dos números son iguales.')
else:
    if(int(numero1)>int(numero2)):
        print(f'El número mayor es {numero1}')
    else:
        print(f'El número mayor es {numero2}')


