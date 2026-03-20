#Prime Number
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
num = 67
if is_prime(num):
    print(f"{num} is a Prime Number")
else:
    print(f"{num} is not a Prime Number")