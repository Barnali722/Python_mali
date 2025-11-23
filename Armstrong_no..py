n=int(input("Enter the number"))
num2=n
arms=0
while(n>0):
    num = n%10
    arms += num**3
    n //= 10
if arms==num2:
        print("Armstrong number")
else:
        print("Not armstrong number")