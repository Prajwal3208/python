# his function uses dynamic programming to calculate the number of distinct ways 
# to climb a staircase of
#  n steps, where you can take either 1 or 2 steps at a time.
def stairs(n):
    if n == 1 or n == 0:  # Base case for 0 or 1 stairs
        return 1
    
    prev = 1
    prev2 = 1
    
    for i in range(2, n+1):
        current = prev + prev2
        prev = prev2
        prev2 = current
        
    return current


n = int(input("Enter the stair number: "))
print(stairs(n))
