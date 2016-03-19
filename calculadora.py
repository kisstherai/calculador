import os
import sys
import time

def suma():
	A = input("ingrese valor de A ") 
	B = input("ingrese valor de B ")
	print A + B  

def resta():
	A = input("ingrese valor de A ")
	B = input("ingrese valor de B ")
	print A - B

def multiplicacion():
	A = input("ingrese valor de A ")
	B = input("ingrese valor de B ")
	print A * B

def dividir():
	A = input("ingrese valor de A ")
	B = input("ingrese valor de B ")
	print A / B

def potencia():
	A = input("ingrese valor de A ")
	print A * A
def menu():
	print "                                                                     calculadora"
	print "     1 suma"
	print "     2 resta"
	print "     3 multiplicacion"
	print "     4 dividir"
	print "     5 potencia"
	Numero = raw_input("ingrese el numero ")

	if Numero.isalpha() == True:
		print "no se permiten letras"
		time.sleep(2)
		os.system(["clear","cls"])
		menu()
	else:
		if Numero =="1":
			print "PUEDE EMPESARA A SUMA"
			suma()
		elif Numero =="2":
			print "PUEDE EMPESAR A RESTAR"
			resta()
		elif Numero =="3":
			print "PUEDE EMPESAR A MULTIPLICAR"
			multiplicacion()
		elif Numero =="4":
			print "PUEDE EMPESAR A DIVIDIR"
			dividir()
		elif Numero =="5":
			print "PUEDE EMPESAR A POTENCIAR"
			potencia()
		else:
			print "Erroneo"

menu()