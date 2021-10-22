punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

x = "Hello in 36-650, & other MSP courses."

def punct_remove(x):
    x_no_punc = ""
    for char in x:
        if char not in punctuations:
            x_no_punc = x_no_punc + char
    print(x_no_punc)

punct_remove(x)