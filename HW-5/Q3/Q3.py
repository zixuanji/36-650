## case 1: same length of strings
def check_1(strX, strY):
    num = 0
    for i in range(0, len(strX)):
        if strX[i]!=strY[i]:
            num = num +1
    if num > 1:
        return False
    return True

## case 2: strings of difference 1
## we should consider both replace and insert for
## count = count for different letter at same position
def check_2(shortStr, longStr):
    count = 0
    for i in range(0, len(longStr)):
        if ( (count==1 or count==0) and i==len(longStr)-1): ##only insert one value in between or at the end
            break
        if (longStr[i]!=shortStr[i] and count == 0): 
            count = count + 1
        if (shortStr[i]!=longStr[i+count]): # if not equal at ith & equal at i+1, suggest inserting a value
            return False
    return True

def one_edit(x, y):
    if len(x) == len(y):
        return check_1(x, y)
    if abs(len(x)-len(y))>1: ##differ more than one implying more than one edit
        return False
    if len(x) > len(y):
        return check_2(y, x)
    elif len(y) > len(x):
        return check_2(x, y)

a = "pale"
b = "ple"
c = "pales"
d = "bale"
e = "bake"

print(one_edit(a, b))
print(one_edit(c, a))
print(one_edit(a, d))
print(one_edit(a, e))

