#sumar dos numeros y mostrar dos resultados
#parametro es la variable que se define cuando se crea la  funcion
def getSum(number1,number2):
    return number1 + number2

def  showResult(message, result):
    return f"{message} {result}"
print("Dime un numero: ")
num1 = float(input())
print("Dime otro numero: ")
num2 = float(input())
#Argumentos son los valores que se envian a la funcaion cuando se llama.
sum = getSum(num1, num2)
print(showResult("La suma es: ", sum))
