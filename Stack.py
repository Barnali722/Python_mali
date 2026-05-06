L = []
while True:
    c = int(input(''' 
                1 Push Elements 
                2 Pop Elements 
                3 Last Element 
                4 Display Stack 
                5 Exit
                6 pop through index\n'''))

    if c == 1:
        n = input("Enter The Value")
        L.append(n)
        print(L)
    elif c == 2:
        if len(L) == 0:
            print("Empty Stack")
        else:
            p = L.pop()
            print(p)
            print(L)

    elif c == 3:
        if len(L) == 0:
            print("Empty Stack")
        else:
            print("Last Stack Value", L[-1])

    elif c == 4:
        print("Display Stack", L)

    elif c == 5:
        break

    elif c == 6:
        print("before",len(L))
        if len(L) == 0:
            print("Empty Stack") 
        
        else: 
            print("after",len(L))
            d=L.pop(int(input("index no. : ")))
            print(d)
