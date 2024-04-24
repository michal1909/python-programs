firstNum = 0
reset = True
result = None
calcOperations = ["+", "-", "*", "/", "**"]

while True:
    if reset:
        firstNum = float(input("Podaj pierwszą liczbę: "))
        reset = False

    operation = input("Podaj operację arytmetyczną " + str(calcOperations) + " lub reset bądź exit: ")
    if operation == "exit": break
    if operation == "reset":
        reset = True
        continue
    if not operation in calcOperations:
        print("Wprowadziłeś błędną operacje!")
        continue

    secondNum = float(input("Podaj drugą liczbę: "))

    try:
        if operation == "+":
            result = firstNum + secondNum

        if operation == "-":
            result = firstNum - secondNum

        if operation == "*":
            result = firstNum * secondNum

        if operation == "/":
            if secondNum == 0:
                raise ZeroDivisionError("Nie można dzielić przez zero!")
            result = firstNum / secondNum

        if operation == "**":
            result = firstNum ** secondNum

        print(str(firstNum), operation, str(secondNum), "=", str(result))
        firstNum = result
        result = None

    except ZeroDivisionError as e:
        print("Błąd:", e)
        reset = True