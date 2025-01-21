# find the char "c" occurance in agiven string 
   # ex. string = 'prajwal'
    #     c = 'a'
    #     o/p = 2


def char(string):
    count = 0
    c = input("Enter character: ")
    for ch in string:
        if ch == c :
            count +=1
    return count

string = input("enter string : ")

print(char(string))


