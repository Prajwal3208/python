def magical_num(num):
    b = bin(num)[2:]
    c = b.count('0')
    if c % 2 != 0:
        return 1
    else :
        return 0
    
def magical_count(n):
    count = 0
    for i in range(1,n+1):
        if magical_num(i) == 1:
            count +=1
    return count
n = int(input("enter the number: "))   
print(magical_count(n))

    

# def magical_num(num):
#     b = bin(num)[2:]       # Convert number to binary and remove '0b' prefix
#     c = b.count('0')       # Count the number of '0's in the binary representation
#     if c % 2 != 0:         # Check if the count of '0's is odd
#         return 1
#     else:
#         return 0

# def mc(n):
#     count = 0
#     for i in range(1, n + 1):  # Iterate from 1 to n inclusive
#         if magical_num(i) == 1:
#             count += 1
#     return count  # Return the total count after the loop completes

# n = int(input("Enter the number: "))   
# print(mc(n))
