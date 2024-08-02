a = int(input("Enter the number: "))

def count_set_bits(n):
    count = 0
    while n > 0:
        # Check if the least significant bit is set
        count += n & 1
        # Shift bits to the right
        n >>= 1
    return count

print("least number after rearranging bit  :",(2*count_set_bits(a)) - 1 )
        
        
        
