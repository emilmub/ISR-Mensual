import numpy as np
import matplotlib.pyplot as plt

def ISR(Tabla,Salario):
	'''
	Calcula el Impuesto Sobre la Renta para un salario mensual

	Tabla: Matriz con los datos relevantes para el calculo
	Salario: Salario mensual para el que deseamos calcular
	'''
	
	for fila in Tabla:
		if Salario <= fila[1] and Salario >= fila[0]:
			cargoFijo = fila[2]
			diferencia = Salario - fila[0]
			porcentaje = fila[3]
			ISR = cargoFijo + diferencia*porcentaje
			return ISR

def grafISR(Tabla):
	'''
	Calcula el ISR para un vector de valores con tal de generar una grafica
	'''
	Salarios = np.arange(1,100000,1)
	Impuestos = []
	SalNeto = []

	for Salario in Salarios:
		Imp = ISR(Tabla,Salario)
		print(Salario)
		Impuestos.append(Imp)
		SalNeto.append(Salario - Imp)

	Impuestos = np.array(Impuestos)
	SalNeto = np.array(SalNeto)

	#plt.plot(Salarios,Impuestos)
	#plt.show()

	plt.plot(Salarios,SalNeto,'m.-',markevery = 5000,ms = 10,lw = 3)
	plt.xlabel('Salario Bruto')
	plt.ylabel('Salario Libre')
	plt.show()


Tabla = np.loadtxt('TablaMensual.csv',skiprows=1,delimiter = ',')

grafISR(Tabla)