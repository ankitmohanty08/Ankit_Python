a=[5,-3,4,-4,-1,8]

largest=max(a[0],a[1])
secondLargest=min(a[0],a[1])
n=len(a)

for i in range(2,n):
    if a[i]>largest:
        secondLargest=largest
        largest=a[i]
    elif a[i]>secondLargest and a[i]!=largest:
        secondLargest=a[i]  
        
print("Highest no. is:",largest)
print("Second highest no. is:",secondLargest)