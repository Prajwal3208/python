a = [2,9,6,8,5,4,3]

for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
            
print(a)
