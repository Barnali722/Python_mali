vehcile = input("Enter type of vehvile (car,truck,motorcycle) : ")


if vehcile=="car":
    print("Toll fee amount : Rs.200")
if vehcile=="motorcycle":
    print("Toll fee amount : Rs.100")
else:
    wheels = int(input("Enter number of wheels : "))
    if wheels>3 and wheels<4:
        print("Toll fee amount : Rs.300 ")
    else:
        print("Toll fee amount :  Rs.500")