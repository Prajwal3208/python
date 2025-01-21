def move_all_zero_toend(arr):
    n =len(arr)

    count = 0
    for i in range(n):
        if arr[i] !=0:
            arr[count],arr[i] = arr[i],arr[count]
            count += 1

    return arr

arr = [1,2,0,4,3,0,5,0]
print(move_all_zero_toend(arr))