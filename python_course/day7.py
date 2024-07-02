#Calculator




# print(5*3)
# print(5+3)
# print(2-1)
# print(15/7)
# print(15//7)
# print(15%7)
# print(2**3)
# Create a calculator capable of performing addition, subtraction, multiplication and division operations on two numbers.
# Your program should format the output in a readable manner!
n = int(input("enter n1:"))
m = int(input("enter n2:"))

additoin = n + m 
print("addition of ", n ,"and" ,m ,"is equal to",additoin)

sub = n -  m
print("substraction of ", n ,"and" ,m ,"is equal to",sub)

mult = m*n
print("multiplication of ", n ,"and" ,m ,"is equal to",mult)

div = m/n
print("division of ", n ,"and" ,m ,"is equal to",div)

floor_div = m//n
print("floor div of ", n ,"and" ,m ,"is equal to",floor_div)

modulus = m%n
print("modulus of ", n ,"and" ,m ,"is equal to",modulus)

expo= m**n
print("expontial is equal to",expo)




