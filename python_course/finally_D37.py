# def func1():
#   try:
#     l = [1, 5, 6, 7]
#     i = int(input("Enter the index: "))
#     print(l[i])
#     return 1
#   except:
#     print("Some error occurred")
#     return 0

#   finally:
#     print("I am always executed")
#   # print("I am always executed")


# x = func1()
# print(x)

try:
    a = int(input("Enter a number between 5 and 9: "))

    if 5 < a < 9:
        print(a * a)
    else:
        raise ValueError("The number entered is not between 5 and 9")
except Exception as e:
    print(e)
finally:
    print("Thank you")

