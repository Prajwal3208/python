'''You are provided with a string which has a sequence of 1s and Os. 
This sequence is the encoded version of a english word. 
You are supposed to write a program to decode the provided s
tring and find the original word. 
Each uppercase Alphabet is representing by a sequence of 1s.'''
def word(s):
    string =""
    splited_string = s.split('0')
    for i in splited_string :
        if i:
            letter_posi = len(i)
            letter = chr(ord('A')+(letter_posi-1))
            string += letter
    return string
s = str(input("Enter the string :"))
print(word(s))