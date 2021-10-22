def star(x):
    d = x
    for i in range(1, x+1):
        for j in range(1, d+1):
            print(end=' ')
        d = d -1
        for k in range(1, i + 1):
            print("*", end=' ')
        print()
        
star(5)