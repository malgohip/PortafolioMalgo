import math as mt

def findMinCrossingSubarray(A, low, mid, high):
    leftSum=float('inf')
    sum=0
    maxLeft=mid
    for i in range(mid, low-1, -1):
        sum+=A[i]
        if sum<leftSum:
            leftSum=sum
            maxLeft=i
    rightSum=float('inf')
    sum=0
    maxLeft=mid+1
    for j in range(mid+1,high+1):
        sum+=A[j]
        if sum<rightSum:
            rightSum=sum
            maxRight=j
    return (maxLeft, maxRight, leftSum+rightSum)

def findMinimumSubarray(A,low,high):
    print(*A[low:high + 1])
    if high==low:
        return (low, high, A[low])
    else:
        mid=(low+high)//2
        leftLow,leftHigh,leftSum=findMinimumSubarray(A,low,mid)
        rightLow,rightHigh,rightSum=findMinimumSubarray(A,mid+1,high)
        crossLow,crossHigh,crossSum=findMinCrossingSubarray(A,low,mid,high)
        if leftSum<=rightSum and leftSum<=crossSum:
            return (leftLow,leftHigh,leftSum)
        elif rightSum<=leftSum and rightSum<=crossSum:
            return (rightLow, rightHigh, rightSum)
        else:
            return (crossLow, crossHigh, crossSum)

l=list(map(int,input().strip().split()))
l,h,s=findMinimumSubarray(l,0,len(l)-1)
print(s)