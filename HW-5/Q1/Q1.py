def mtr_transpose(X):
    result=[]
    for j in range(len(X[0])):
        row=[]
        for i in range(len(X)):
            row.append(X[i][j])
        print(row)

            
A = [[10, 8],
    [2, 4],
    [1, 7]]

mtr_transpose(A)