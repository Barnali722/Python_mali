def search(list, n):
    for i in range(len(list)):
        if list[i] == n:
            return i
    return -1


list = [10, 50, 30, 70, 90, 120, 150]
n = 70
result = search(list, n)

if result != -1:
    print(f"Element found at location :{result}")

else:
    print("Not Found")