# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# * 1. Starting with any positive integer, replace the number by the sum 
# of the squares of its digits.
# 2. Repeat the process until the number equals 1 (where it will stay), 
# or it loops endlessly in a cycle which does not include 1.
# 3. Those numbers for which this process ends in 1 are happy.
# # Return true if n is a happy number, and false if not.


def is_happy(n):
    seen = set()  # To keep track of numbers we've already seen
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit)**2 for digit in str(n))  # Sum of squares of digits
    return n == 1  # If we reach 1, it's a happy number

# Example usage:
n = int(input("enter the number: "))
print(is_happy(n))  # Output: True, because 19 is a happy number
