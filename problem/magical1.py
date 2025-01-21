# n = int(input("Enter the number : "))
# for i in range(1,n+1):
#     b = bin(i)[2:]
#     # for a in range(i):
#     #     if a == 0:
#     #         a == 1
#     #     else :
#     #         a == 2
#     #     a += 1
    
        
# print(f'the numer {b} is binary representation of {i} ')


def magical_num(num):
    # Convert to binary and remove the '0b' prefix
    b = bin(num)[2:]
    print(f"Binary representation of {num}: {b}")
    
    # Replace '0' with '1' and '1' with '2'
    a = ''.join(['1' if ch == '0' else '2' for ch in b])
    

    print(f"Modified binary string for {num}: {a}")
    
    # Calculate the sum of digits
    digit_sum = sum(int(i) for i in a)
    print(f"Sum of digits: {digit_sum}")
    
    # Return if the sum is odd
    return digit_sum % 2 != 0

def magical_count(n):
    count = 0
    for i in range(1, n + 1):
        if magical_num(i):
            count += 1
    return count

n = int(input("Enter the number: "))
print(f"Count of magical numbers: {magical_count(n)}")

# def magical_num(num):
#     b = bin(num)[2:]
#     a = b.replace('0','1').replace('1','2')
    
#     digit_sum = sum(int(i) for i in a)
#     return digit_sum % 2 != 0

# def magical_count(n):
#     count = 0
#     for i in range(1,n+1):
#         if magical_num(i):
#             count += 1
#     return count
# n = int(input("enter the number "))

# print(magical_count(n))

    