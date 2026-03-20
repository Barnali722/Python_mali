def bubble_sort(list1):
    #n = len(list1)
    for i in range(0,len(list1)-1):
        for j in range(len(list1)-1):
            if list1[j]>list1[j+1]:
                temp = list1[j]
                list1[j]=list1[j+1]
                list1[j+1]=temp
            print(list1)
    return(list1)



list1 = [64,34,25,12,22,11,90]
print (f"Original list: {list1}")
bubble_sort(list1)
print(f"Sorted list 1: {list1}")