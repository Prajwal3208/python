# def sgpa_calculator(a,b):
#     sgpa = (b*2)-a
#     print("Sgpa of 2nd sem is: ",sgpa)
    
     
# a = float(input("enter the sgpa of 1st sem: "))
# b = float(input("enter the sgpa of hole year: "))

# sgpa_calculator(a,b)
# def cgpa_calculator(c,d,e,f):
#     cgpa = (c+d+e+f)/4
#     print("cgpa of 4 years is : ",cgpa)

def cgpa_calculator(*number):
    sum = 0 
    for i in number:
        sum = sum + i
    print("total cgpa is :", sum/len(number))
    

    
c =float(input("enter the sgpa of the 1st year: "))
d =float(input("enter the sgpa of the 2nd year: "))
e =float(input("enter the sgpa of the 3rd year: "))
f =float(input("enter the sgpa of the 4th year: "))

cgpa_calculator()