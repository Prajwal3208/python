
def evenodd(arr):
    n = len(arr)
    str= ""
    for i in range(0,n):
        if arr[i]%2==0:
            str+=" even " 
        else :
            str+= " odd " 
    return str
arr = list(map(int,input("enter the array element seprate by space : ").split()))
print(evenodd(arr))