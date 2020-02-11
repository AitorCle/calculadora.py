import sys
import decimal

def suma(A,B):
	return A + B
	
def resta(A,B):
	return A - B

def multiplicacion(A,B):
	return A*B

def division(A,B):
	return A/B
	
#Arguments control	
if len(sys.argv) != 4:
	sys.exit("Error in arguments(OPERATION ARG1 ARG2)")

try:
	op1 = decimal.Decimal(sys.argv[2])
	op2 = decimal.Decimal(sys.argv[3])
except decimal.InvalidOperation:							#PRUEBA Y SI SALE EL ERROR INVALIDOPERATION ESCRIBE TAL
	sys.exit("Operands must be numbers")	
		
operacion = sys.argv[1]
#main
if operacion == "suma":
	res = suma(op1,op2)
elif operacion == "resta":
	res = resta(op1,op2)
print(res)

