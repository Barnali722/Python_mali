#Python claculator

operator=input("Enter an operator(+ - * /):")
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))

if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
else:
    print(num1/num2)

