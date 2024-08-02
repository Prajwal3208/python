# x = 5

# def fun():
#   x= 10
#   print(x)

# fun()
# print(x)

x = 5

def fun():
  global x
  x=5
  print(x)

fun()
print(x)
