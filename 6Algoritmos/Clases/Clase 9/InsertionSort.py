lst=[5,2,4,6,1,3]
n=len(lst)
for i in range(1,n):
    k=lst[i]
    j=i-1
    while (j>-1 and lst[j]>k):
        lst[j+1]=lst[j]
        j-=1
    lst[j+1]=k
print(lst)