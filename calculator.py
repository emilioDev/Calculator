#!/usr/bin/python

import os

#addizione
def add(x, y):
	return x+y
#sottrazione
def sub(x, y):
	return x-y
#moltiplicazione
def mul(x, y):
	return x*y
#divisione
def div(x, y):
	if y == 0:
		print("Errore, divisione per 0")
	else:
		return x/y

os.system("clear")
print("************************************************************************************************\n")
addendo1 = int(raw_input("Inserire il primo valore: "))

addendo2 = int(raw_input("Inserire il secondo valore: "))
print("\n1)Somma\n2)Dividi\n3)Moltiplica\n4)Dividi\n")

val = raw_input("Inserire opzione: ")

if val == '1':
	print(add(addendo1,addendo2))
elif val == '2':
	print(sub(addendo1,addendo2))
elif val == '3':
	print(mul(addendo1,addendo2))
elif val == '4':
	print(div(addendo1,addendo2))
else:
	print("Operazione non valida!")

