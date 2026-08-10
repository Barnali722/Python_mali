import math

list1 = [2,4,7,9,10,16,21,25,30,36,77]
nonsqr_list = []
root_list = []
multi = []

for i in list1:
    if i >=0:
        root = math.isqrt(i)
        if root*root != i:
            nonsqr_list.append(i)

print(nonsqr_list)

for i in list1:
    if i >=0:
        root = math.isqrt(i)
        if root*root == i:
            root_list.append(root)

print(root_list)

l1 = len(nonsqr_list)
l2 = len(root_list)

if l1 == l2:
    for i in nonsqr_list:
        for j in root_list:
            multi = nonsqr_list*root_list
            multi.append(multi)
else:
    if l1>l2:
        for i in nonsqr_list:
            for j in root_list:
                root_list.insert(len(root_list),0)
            multi = nonsqr_list*root_list
            multi.append(multi)

print(multi)