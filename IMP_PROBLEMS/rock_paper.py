# a = input("Enter the input of 'A':")
# if (a.lower()== "paper"):
#     print("B: sizer")
# elif (a.lower()== "sizer"):
#     print("B: rock")
# elif (a.lower()== "rock"):
#     print("B: paper")
# else:
#     print("Invalid Input")
    

def winb(a):
    
    if (a.lower()== "paper"):
        print("B: sizer")
    elif (a.lower()== "sizer"):
        print("B: rock")
    elif (a.lower()== "rock"):
        print("B: paper")
    else:
        print("Invalid Input")
    
while True:
    a = input("Enter the input of 'A'('rock','paper','sizer') or 'quit' for exit:")
    if a.lower()== "quit":
        print("you are exited")
        break
    else :
        winb(a)
        
