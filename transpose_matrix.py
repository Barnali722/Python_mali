X = [[1, 2, 3],
     [4, 5, 6],
     ]

result = [[0, 0],
          [0, 0],
          [0, 0]]

for i in range(len(X)):

    for j in range(len(X[0])):
        result[j][i] = X[i][j]

for r in result:
    print(r)