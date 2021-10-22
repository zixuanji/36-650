def triangle(x):
    n = 1
    if (not isinstance(x, int)):
        return("Invalid Input")
    elif (x < 0):        
        return("Invalid Input")
    else:
        for i in range(1, x+1): 
            for j in range(1, i + 1):
                print(n, end='  ')  
                n = n +1
            print()

triangle(6)