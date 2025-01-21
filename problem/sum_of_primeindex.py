'''Given an array with 'N' elements, you are expected to find the sum
 of the values that are present in prime indexes of the array. 
 Note that the array index starts with 0 i.e. the position (index) on 
 the first array element is 0,
 the position of the next array element is 1 and so on.'''


def isprime(a):
    if a<=1:
        return False
    for i in range(2,int(a**0.5)+1):
        if a%i == 0:
            return False
    return True

def prime_sum(n):
    sum = 0
    for i in range(len(n)):
        if isprime(i):
            sum +=n[i]
    return sum

# n = [10,20,30,40,50,60,70,80,90,100]
n = list(map(int,input("enter the element of array seprated by space :").split()))

print(prime_sum(n))
