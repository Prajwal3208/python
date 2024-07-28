# It is Edward's birthday today. His friends have bought him a huge circular cake.
# Edward wants to find out the maximum number of pieces he can get by making exactly N straight vertical cuts on the cake.
# Your task is to write a function that returns the maximum number of pieces that can be obtained by making
# N number of cuts.
# Note: Since the answer can be quite large, modulo it by 1000000007 A
# Input Specification:
# input1: An integer N denoting the number of cuts
# Output Specification:
# Return the maximum number of pieces that can be obtained by making N cuts on the cake

def max_pieces(N):
    MOD = 1000000007
    # Calculate the number of pieces using the formula
    pieces = (N * (N + 1) // 2 + 1) % MOD
    return pieces

# Example usage
N = int(input("Enter the number of cuts: "))
print("Maximum number of pieces:", max_pieces(N))

    
