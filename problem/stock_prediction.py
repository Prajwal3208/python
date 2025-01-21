#you working on a financial analysis tool whuch represent daily stock prices
# of a company over 
# timee.Each element in an integer array A of size N representing the closing price
# of the stock for that particaular day .your task is to fin d and return an integer 
# value representing the total number of days where where the stock market value is
# decrease indicating negative growth
def pre(arr):
    n = len(arr)
    count = 0
    if n <= 1:
        return 0

    for i in range(0,n-1):
        if arr[i] > arr[i+1]:
            count += 1
    return count
#arr = [2,3,1,4,5,2]  #direct arr input 
arr =list(map(int,input("Enter the element seprated by space : ").split())) # arr is user input
# b = int(input("enter the the no of elements is arr : ")) # take input 1 by 1 
# arr =[]
# for _ in range(b):
#     arr.append(int(input()))
print("graph decrising number = ", pre(arr))
    




