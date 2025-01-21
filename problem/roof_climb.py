def climb(arr):
    # n = len(arr)
    count  = 0 
    # for roofs in range(0,n):
    for roofs in arr:
        if roofs % 3 == 0:
            count +=1 
    return count 

arr = list(map(int,input("Enter the roof of the houses seprated by space: ").split()))

print("Alice can reach to roof of ",climb(arr),"houses")