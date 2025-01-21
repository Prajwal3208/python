'''Problem Statement
You are given an array arr of length n. Find and print the element at the mid-index of arr ignoring all the indices at which negative numbers are present in the array.
Note:
﻿﻿In case there are two mid indices, print the element at the smaller index.
﻿﻿You may assume that there will be at least one positive number in arr.
Input Format:
The input consists of two lines:
﻿﻿The first line contains a single integer denoting n.
﻿﻿The second line contains n space-separated integers denoting arr.
The input will be read from the STDIN by the candidate
Output Format:
Print the element at the mid-index of arr ignoning all the indices at which negative numbers are present in the arra.
The output will be matched to the candidate's output printed on the STDOUT'''
def remove_negative(arr):
    arr1 = []
    for  i in range(len(arr)):
        if arr[i] >= 0:
            arr1.append(arr[i])
    return arr1

def middle_ele(a):
    arr1 = remove_negative(a)
    for i in range(len(arr1)):
        if i == len(arr1)//2:
            return arr1[i-1]
        

a = [12,-3,14,-56,77,13]
print(middle_ele(a))

