n=int(input("Enter a number : "))
num=n
rev=0
while(n>0):
    rev=rev*10+n%10  #or num2=n%10,then rev=rev*10+num2
    n=n//10  #//means quatient in interger no decimal
if(rev==num):
    print("Pallindrom number")
else:
    print("Not Pallindrom number")