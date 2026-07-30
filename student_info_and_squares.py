import pandas as pd
import numpy as np
import math

name =("Moni" , "Sreyasi" , "Liza" , "Debo" , "Barnali" , "Anubhav")
roll_no = (70, 78, 79, 72, 44, 13)

info = name + roll_no
print(info)

list1 = [2,4,7,9,10,16,21,25,30,36,77]
sqr_list = []

for i in list1:
    if i >=0:
        root = math.isqrt(i)
        if root*root == i:
            sqr_list.append(i)

print(sqr_list)