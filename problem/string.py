#given string consist of words and spaces retrun the last lenth of last word in string
# s = " fly me to the moon "

def remove_spaces(s):
    s1 = s.strip()
    count = 0
    for ch in s1:
        if ch == " " :
            count = 0
        else:
            count += 1
    return count

s = input("Enter the string : ")
print(remove_spaces(s))






