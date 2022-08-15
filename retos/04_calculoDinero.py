'''
Juan tiene N cantidad de pesos, 
Camila tiene la mitad de lo que posee Juan 
y Ricardo tiene la mitad de lo que poseen Camila y Juan Juntos. 
¿Puede PYTHON ayudarme a calcular la cantidad de dinero de los 3?
'''
pesosJuan=input("Ingrese la cantidad de dinero que tiene Juan: ")

pesosCamila=float(pesosJuan)/2
pesosRicardo=(float(pesosJuan)+float(pesosCamila))/2

print(f'Juan tiene: {pesosJuan} pesos \n Camila tiene {pesosCamila} pesos \n Ricardo tiene {pesosRicardo} pesos')