
Principal=0
rate=0
time=0

while Principal<=0:
    Principal = int(input("entre your principal: "))
    if Principal<0:
        print("Principal cannot be less than 0 or equal to zero.")

while rate<=0:
    rate = int(input("entre your rate: "))
    if rate<0:
        print("rate cannot be less than 0 or equal to zero.")

while time<=0:
    time = int(input("entre your time in years: "))
    if time<0:
        print("time cannot be less than 0 or equal to zero.")

Total= Principal*pow((1+rate/100),time)
print(f"your total balance after {time} years is: Rs.{Total:.2f}")
