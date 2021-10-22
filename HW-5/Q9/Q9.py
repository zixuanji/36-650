def palindrome(x):
    s, e = 0, len(x)-1
    if len(x)==1 : ##for string of odd number of length
        return True
    elif len(x)==0 : ##for string of even number of length
        return True
    elif x[s]!=x[e]:
        return False
    else:
        str_mid = x[s+1 : e] 
        return palindrome(str_mid)

a = "okko"
b = "kayak"
c = "hello"
d = "yiiyyiiy"

print(palindrome(a))
print(palindrome(b))
print(palindrome(c))
print(palindrome(d))