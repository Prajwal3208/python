s = "ABC"

def permitution(s):
    count = 0
    arr = ["a","e","i","o","u","A","E","I","O","U"]
    for i in s:
        for j in arr:
            if s[i]!=arr[j]:
                i+=1
                j+=1
                count+=1
    return count
print(permitution(s))

