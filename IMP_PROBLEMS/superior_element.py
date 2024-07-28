# Problem statement
# In an array a superior element is one which is greater than all elements to its right, The rightmost element will always be considered as a superior element.
# You are given a function, Int FindNumberOfSuperiorElements(int* arr, int n);
# The function accepts an integer array 'arr' and its length 'n'. Implement the function to find and return the number of superior elements in array 'arr'.
# Assumptions:
# 1. N> 0.
# 2. Array index starts from

def superior(arr):
    n = len(arr)
    if n==0:
        return 0
    count = 0
    max_ele = float("-inf")
    
    for i in range(n-1,-1,-1):
        if arr[i]>max_ele:
            count +=1
            max_ele = arr[i]
            
    return count
arr =[7,9,5,2,8,7]
print(superior(arr))





# def superior_element(arr):
#     n = len(arr)
#     if n==0:
#         return 0
        
#     count = 0
#     superior = 0
#     for  i in range(n-1,-1,-1):
#         if  arr[i] > superior :
#             count += 1
#             superior = arr[i]
    
#     return count
# arr = list(map(int,input("Enter the element saperate by space :").split()))

# print(superior_element(arr))
