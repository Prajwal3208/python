
def prime_num(n):

    sum = 0   
    for i in range(2,n+1):
        if i % 2 != 0:
            sum = sum + i
            i += 1 
    return sum
            
n = int(input("enter the number : "))
print(prime_num(n))

    
     
