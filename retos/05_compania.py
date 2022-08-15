'''
Una compañía de software contable, paga a su personal de ventas un salario de 3500000 mensuales, 
mas una comisión de 1500000 por cada licencia de software vendida 
menos el (5% del salario total + comisiones de deducciones) por impuestos. 
Codifica un programa que calcule e imprima el salario mensual de un vendedor dado 
recibiendo el numero de ventas realizadas
'''
nombreVendedor=input("Ingrese el nombre del vendedor: ")
ventasRealizadas=input(f"Ingrese la cantidad de ventas realizadas por el vendedor {nombreVendedor}: ")
comisionPorVenta=1500000
salarioBasico=3500000
totalComisiones=int(ventasRealizadas)*comisionPorVenta
salarioBruto=salarioBasico+totalComisiones
deducciones=salarioBruto*0.05
salarioNeto=salarioBruto-deducciones

print(f'Salario Básico Mensual: {salarioBasico} ')
print(f'Comisión por ventas en el mes: {totalComisiones}')
print(f'Salario bruto: {salarioBruto} ')
print(f'Deducciones: {deducciones}')
print(f'Salario Neto: {salarioNeto}')
