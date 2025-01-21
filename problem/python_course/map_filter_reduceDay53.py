# # MAP 
# # def cube(x):
# #   return x * x * x


# # print(cube(2))

# l = [1, 2, 4, 6, 4, 3]
# # newl = []
# # for item in l:
# #   newl.append(cube(item))

# newl = list(map(lambda x: x*x*x, l))
# print(newl)


# #filter

# l = [1,2,4,6,4,3]
# new = list(filter(lambda x: x % 2 == 0 ,l))
# print(new)



# ## reduce
# from functools import reduce

# # List of numbers
# numbers = [1, 2, 3, 4, 5] 

# # Calculate the sum of the numbers using the reduce function
# def mysum(x, y):
#   return x + y
  
# sum = reduce(mysum, numbers)

# # Print the sum
# print(sum)