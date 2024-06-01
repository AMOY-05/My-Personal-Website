# USSD PROGRAMMING
acct_bal = 1000  # Account Balance
a = "*311#"  # Recharge
b = "*312#"  # Data Plans
c = "*303#"  # Borrow Airtime
d = "*310#"  # Account Balance
e = "*323#"  # Data Balance
f = "*321#"  # Me2U
n = input("Enter the ussd code: ")
if n == a: # Recharge
    net_work = input("Enter your network (MTN or Airtel): ")
    if net_work == "MTN" or "Airtel":
        re_much = eval(input("How much did you want to recharge: "))
        if re_much >= 25 and re_much <= acct_bal:
            print("Recharge Successful and you have " + str(acct_bal - re_much) + " left")
        else:
            print("Invalid Input")
elif n == b: # Data Plans
    net_work = input("Enter your network (MTN or Airtel): ")
    if net_work == "MTN" or "Airtel":
        print("40MB - #50")
        print("50MB - #50")
        dataPlans = input("")
