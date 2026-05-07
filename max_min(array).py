def max(list):
    for i in range(len(list)):
        if list[i] > list[i+1]:
            return list[i]

    return 0

def min_1(list):
    min2 = list[0]
    for j in list:
        if j < min2:
            min2 = j
    return min2


n= int(input("Enter a range : "))
list = []

for i in range(n):
    j = int(input("Enter an element : "))
    list.append(j)

print(list)

maximum = max(list)

if maximum != 0:
    print(f"The maximum element is : {maximum}")
else:
    print("The maximum element is 0")

print(f"Minimun : {min_1(list)}")
