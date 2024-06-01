def fxn(stng):
    oupt = stng[0]
    for i in range(1, len(stng)):
        if stng[i-1] == ' ':
            oupt += stng[i]
    oupt = oupt.upper()
    return oupt
inpt1 = input("Enter The Word: ")
print(fxn(inpt1))

