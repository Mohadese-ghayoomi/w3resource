def accept(s):
    Upper=0
    Lower=0
    for i in s:
        if i.isupper():
            Upper=Upper+1
        elif i.islower():
            Lower=Lower+1 
        else:
            pass
    print("Number of Lowercase Character is:",Lower)
    print("Number of Uppercase Character is:",Upper)

          
