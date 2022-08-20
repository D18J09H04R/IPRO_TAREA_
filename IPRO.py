# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	print("hola esta es una calculadora")
	print("dime el primer numero a sumar")
	numeroa = float(input())
	print("hola esta es una calculadora")
	print("dime el segundo numero a sumar")
	numerob = float(input())
	resultado_suma = numeroa+numerob
	print("resultado=",resultado_suma)
	print("hola esta es una calculadora")
	print("dime el tercer numero")
	numeroc = float(input())
	resultado_resta = numeroa-numerob-numeroc
	print("resultado=",resultado_resta)
	print("hola esta es una calculadora")
	print("dime el cuarto numero")
	numerod = float(input())
	resultado_multiplicar = numeroa*numerod
	print("resultado=",resultado_multiplicar)
	print("cual es tu nombre")
	nom = input()
	print("ingresa el numero de notas a calcular")
	x = float(input())
	day = -0
	for i in range(1,x+1):
		print("ingresar la nota",i,":")
		nota = float(input())
		day = day+nota
	final = day/x
	print("el promedio de",nom,"es de:",final)

