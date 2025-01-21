'''A googly prime number is defined as a number that is derived from the sum of its individual
digits. For example, if N = 43, the sum of its individual digits is 4+3 = 7, which is prime
making it a googly prime number. 4
Your task is to find whether the current number is googly prime number or not.'''

def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def digit_sum(a):
    sum = 0 
    while a>0:
        r = a% 10
        sum += r
        a = a//10
    return is_prime(sum)


a = int(input("enter the number N:"))
prime = digit_sum(a)
if prime == True:
    print( "GOGLY PRIME")
else:
    print("NOT GOGLY  PRIME ")