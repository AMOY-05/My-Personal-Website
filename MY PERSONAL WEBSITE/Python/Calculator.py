# CALCULATOR
print("*****CALCULATOR*****".center(45))
print("\t 1-Basic Mathematical Operation".upper())
print("\t 2-Conversion Operation".upper())
print("\t 3-Trigonometry Operation".upper())
act_vty = eval(input("Select your operation: "))
if act_vty == 1:
    print("***Basic Mathematical Operation***".upper().center(45))
    num1 = eval(input("Enter first number: "))
    op = input("Enter an operator: ")
    num2 = eval(input("Enter another number: "))
    if op == '+':
        print("num1 + num2 = ", num1 + num2)
    elif op == '-':
        print("num1 - num2 = ", num1 - num2)
    elif op == '*':
        print("num1 * num2 = ", num1 * num2)
    elif op == '/':
        print("num1 / num2 = ", num1 / num2)
    else:
        print("Invalid Operator")
elif act_vty == 2:
    print("***Conversion Operation***".upper().center(45))
    print("\t 1-Lb(s) to Kg")
    print("\t 2-Kg to Lb(s)")
    print("\t 3-Celsius to Fahrenheit")
    print("\t 4- Fahrenheit(F) to Celsius(C)")
    a = eval(input("Your Conversion Operation: "))
    if a == 1:
        lbs = eval(input("Enter weight in lbs: "))
        print("Your weight is ", lbs * 0.45, "kg")
    elif a == 2:
        kg = eval(input("Enter your weight in kg: "))
        print("Your weight is ", kg / 0.45, "lbs")
    elif a == 3:
        c = eval(input("Enter the Temperature in Celsius: "))
        print("The Equivalent Temperature in Fahrenheit is ", 9 / 5 * c + 32, "F")
    elif a == 4:
        f = eval(input("Enter the Temperature in Fahrenheit: "))
        print("The Equivalent Temperature in Celsius is ", 5 * f - 160 / 9, "C")
    else:
        print("Invalid Input, Please Try again".upper())
elif act_vty == 3:
    print("***Trigonometry Operation***".upper().center(45))
    k = input("Enter your angle(30 or 45 or 60 or 90 or 180 or 270 or 360): ")
    if k == "sin30":
        print("sin30 = 0.5")
    elif k == "sin45":
        print("sin45 = 0.7071")
    elif k == "sin60":
        print("sin60 = 0.8660")
    elif k == "sin90":
        print("sin90 = 1.000")
    elif k == "sin180":
        print("sin180 = 0.000")
    elif k == "sin270":
        print("sin270 = -1")
    elif k == "sin360":
        print("sin360 = 0.000")
    elif k == "cos30":
        print("cos30 = 0.8660")
    elif k == "cos45":
        print("cos45 = 0.7071")
    elif k == "cos60":
        print("cos60 = 0.50")
    elif k == "cos90":
        print("cos90 = 0.000")
    elif k == "cos180":
        print("cos180 = -1.000")
    elif k == "cos270":
        print("cos270 = 0.000")
    elif k == "cos360":
        print("cos360 = 1.000")
    elif k == "tan30":
        print("tan30 = 0.5774")
    elif k == "tan45":
        print("tan45 = 1")
    elif k == "tan60":
        print("tan60 = 1.732")
    elif k == "tan90":
        print("tan90 = infinity")
    elif k == "tan180":
        print("tan180 = 0.000")
    elif k == "tan270":
        print("tan270 = infinity")
    elif k == "tan360":
        print("tan360 = 0.000")
    else:
        print("Invalid Input")
else:
    print("The Option is not available or Invalid Input.Please Try Again")
