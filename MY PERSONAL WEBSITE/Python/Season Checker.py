def season_checker(month):
    autumn = ["January", "February", "March", "April"]
    summer = ["May", "June", "July", "August"]
    winter = ["September", "October", "November", "December"]
    for i in autumn:
        if month == i:
            print("It is Autumn Season")
    for j in summer:
        if month == j:
            print("It is Summer Season")
    for k in winter:
        if month == k:
            print("It is Winter Season")
        break
    else:
        print("Invalid Input")


month1 = input("Enter Month: ")
season_checker(month1)
