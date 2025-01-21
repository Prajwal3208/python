def ispalindrom(s):
    
    string2 = s[::-1]
    if s == string2:
        return 1
    else :
        return 0
s = input("enter the string :")
print(ispalindrom(s))
