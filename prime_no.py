mum=int(input("Enter a number: "))

for i in range(2,mum):
    if mum%i==0:
        print("Not a prime number")
        break
else:
        print("Prime")