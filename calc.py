X = int(input("Ingresa un entero, por favor: "))

if X < 0:
	X = 0
	print('Negativo cambiado a cero')
elif X == 0:
	print ('Cero')
elif X == 1:
	print ('Simple')
else:
	print ('Más')
	