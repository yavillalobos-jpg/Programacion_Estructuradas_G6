#Registrar las edades de n cantidad de personas y mostrar la edad mas altas y mas baja y la cantidad de personas registrada.
ages = []

def addAge(age):
    ages.append(age)

    def getMaxAge():
        maxAge =  ages[0]
        for age in ages:
            if age > maxAge:
                maxAge =  age
        return maxAge

def getMinAge():
    MinAge = ages[0]
    for age in ages:
        if age < minAge:
            minAge = age
    return minAge

def showSize():
    return ages.count

def showAges():
    return ages

while True:
    try:
        age = int(input("Dime tu edad: "))
        if(age > 3):
            addAge(age)
        else:
            print("Debe ser un numero mayor a 3.")

        answer = input("ingresa otro [S - N]: ")
        if answer.upper() != "S":
           break
    except ValueError:
        print("Debe ingresar un entero.")



print("Mostrar edades")
print(f"Cantidad de edades registradas: {showSize()}")
print(showAges())
print(f"Edad más joven: {getMinAge()}")
print("Todas las edades:", showAges())