# ATM PROGRAM
print("Welcome to Ambassador Bank")
pin = int(input("Enter your pin: "))
amount = 50000
if pin == 1234:
    print("******TRANSACTIONS******".center(30).upper())
    print("\t 1-Withdraw")
    print("\t 2-Balance Enquiry")
    print("\t 3-Fast Cash")
    print("\t 4-Transfer")
    print("\t 5-Change your pin")
    c = int(input("Please choose transactions: "))
    if c == 1:
        w = int(input("Please enter your withdrawal amount: "))
        if w < amount:
            print("Please take your amount:", w)
        else:
            print("Insufficient Balance")

    elif c == 2:
        print("charges is 6.98")
        contd = input("wanna continue?(yes or no) ")
        if contd == "yes":
            print("Your available amount is ", amount - 6.98)
        elif contd == "no":
            print("Bye")
        else:
            print("Enter only yes or no")

    elif c == 3:
        print("\t 1. 2000")
        print("\t 2. 5000")
        print("\t 3. 10000")
        print("\t 4. 15000")
        print("\t 5. 20000")
        f = eval(input("Enter fast cash option: "))
        if f == 1 and 2000 < amount:
            print("Please take your 2000 cash")
        elif f == 2 and 5000 < amount:
            print("Please take your 5000 cash")
        elif f == 3 and 10000 < amount:
            print("Please take your 10000 cash")
        elif f == 4 and 15000 < amount:
            print("Please take your 15000 cash")
        elif f == 5 and 20000 < amount:
            print("Please take your 20000 cash")
        else:
            print("Insufficient Cash. Please try again")
    elif c == 4:
        acct_No = str(input("Enter the beneficiary account number: "))
        if len(str(acct_No)) == 10:
            i = eval(input("Enter amount you wish to be transferred: "))
            if i < amount and i % 100 == 0:
                print("Transaction Successful")
            else:
                print("Insufficient Balance")
        else:
            print("The beneficiary account number is greater or less than 10")
    elif c == 5:
        pin = eval(input("Enter your present pin: "))
        change_pin = int(input("Enter the new pin: "))
        if change_pin != pin:
            print(f"You have successfully change your pin: '{pin}' to {change_pin}")
        else:
            print("Input the pin again")
    else:
        print("Wrong choice. Try again")
else:
    print("Incorrect pin")

cont_d = input("Did you want to continue? ")
while cont_d:
    if cont_d == "yes":
        pin = int(input("Enter your pin: "))
        c = int(input("Please choose transactions: "))
        break
else:
    print("THANKS FOR BANKING WITH US")
