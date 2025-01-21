# arr = [1,2,3,4,5,6,7,10]
'''Bob desires to buy N candies. 
The price of each candy is given in an array. 
Bob has amount of money. The best deal for him in the 
supermarket is that if the price of a candy is a multiple of 5 then he
 doesn't have to pay, for the rest he has to pay the amount mentioned in A[il,
   that is the exact amount
Input format:input1: Number of candies N
input2: Array of the price of candies 
input3: Amount of money MOuput Format:Return the maximum number of candies he can buy

'''

def amount(arr):
    count = 0
    sum=n
    arr1 = sorted(arr)
    for i in range(len(arr1)):
        if arr1[i] % 5 == 0:
            count +=1
            
        else:
            if arr1[i]<= sum:
                count +=1
                sum-=arr1[i]
    return count

arr = list(map(int,input("Enter the price seprated by space :").split()))
n = int(input("Enter your amount:"))

print(amount(arr))
