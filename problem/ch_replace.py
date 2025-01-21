'''Given string and two characters chi,ch2 as input,
 replace all occurences of ch with ch2 and ch2 with chi in the input string.'''

## simple
# strings =input("enter the string")
# ch1= 's'
# ch2= 'a'
# temp = "temprory"
# neew_str= strings.replace(ch1,temp).replace(ch2,ch1).replace(temp,ch2)
# print(neew_str)

##function

def swap_char(string,ch1,ch2):
    temp = "0"
    new_string = string.replace(ch1,temp).replace(ch2,ch1).replace(temp,ch2)

    return new_string
string = input("Enter the string :")
ch1 = input("Enter ch1 youwant to replace :")
ch2 = input("Enter ch2 you want to replace :")

print("Original string : ",string)
print("replaced string:",swap_char(string,ch1,ch2))