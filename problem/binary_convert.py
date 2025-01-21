# # n = int(input("enter the number : "))

# # print(bin(n))

# def int_to_binary(n):

#     binary = ""

#     if n == 0:
#         return "0"
    
#     while n > 0:
#         binary = str(n % 2) + binary
#         n = n // 2
#     return binary

# # Input from the user
# number = int(input("Enter an integer: "))
# binary = int_to_binary(number)
# print(f"Binary representation: {binary}")


def convert(n):

    binary = ""
    if n == 0:
        return 0
    while n>0 :

        binary = str(n % 2) + binary
        n = n // 2
    return binary
n = 5
print(convert(n))

