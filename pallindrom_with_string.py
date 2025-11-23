n=int(input("Enter a number: "))
n=str(n)
if n==n[::-1]:
    print(n,"is a pallindrome number")
else:
    print(n,"is not a pallindrome number")