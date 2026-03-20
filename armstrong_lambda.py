#Armstrong Number
is_armstrong = lambda n: n == sum(int(d)**len(str(n)) for d in str(n))
num = 153
if is_armstrong(num):
    print(f"{num} is an Armstrong Number")
else:
    print(f"{num} is not an Armstrong Number")