
# # a= 9
# # b= 8

# # gmean1 = (a*b)/(a+b)
# # print(gmean1)

# # c=10
# # d=11
# # gmean2 = (c*d)/(c+d)
# # print(gmean2)

# # e=10
# # f=11
# # gmean3 = (e*f)/(e+f)
# # print(gmean3)

### for this above we use function
def calculateGmean(a, b):
  mean = (a*b)/(a+b)
  print(mean)

def isGreater(a, b):
  if(a>b):
    print("First number is greater")
  else:
    print("Second number is greater or equal")


def isLesser(a, b): #for future #only pass not run
  pass

# a = 9
# b = 8
a = int(input("Enter the first number: "))
b = int(input("enter the second number: "))
calculateGmean(a,b)
isGreater(a,b)
