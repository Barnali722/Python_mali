def binarySearch(list, n):
    left = 0
    right = len(list) - 1

    while left <= right:
        mid = (left + right) // 2

        if list[mid] == n:
            return mid

        if list[mid] < n:
            left = mid + 1
        else:
            right = mid - 1

    return -1


list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 9

result = binarySearch(list, x)

if result != -1:
    print("Found at index", result)
else:
    print("Not found")