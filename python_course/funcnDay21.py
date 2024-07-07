##default argument

# def average(a=9, b=1):
#   print("the average of a and b is " , (a+b)/2 )

# average() #consider default values 9,1
# average(5) #it consider "a" as "5"
# average(b=9) #b is 5



# def average(a,b):
#   #print("the average of a and b is " , (a+b)/2 )
#   return (a+b)/2

# c = average(9,1)
# print(c)


# def average(a, b, c=1):
#   print("The average is ", (a + b + c) / 2)
# average(4, 6)

def average(*numbers):
  # print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i
  # print("Average is: ", sum / len(numbers))
  # return 7
  return sum / len(numbers)
c = average(5, 6, 7, 1)
print(c)


# # def name(**name):
# #   # print(type(name))
# #   print("Hello,", name["fname"], name["mname"], name["lname"])


# # name(mname="Buchanan", lname="Barnes", fname="James")
