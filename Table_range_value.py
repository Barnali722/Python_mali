num=int(input("Enter a table number: "))
end=int(input("Enter end number: "))

for i in range(1,end+1):
    result=num*i
    print(f"{num}*{i}={result}")