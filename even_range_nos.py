print("Enter numbers in range :")
start=int(input("start : "))
end=int(input("end : "))

for i in range(start,end+1):
    if(i%2==0):
        print(i)