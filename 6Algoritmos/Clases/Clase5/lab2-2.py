l=map(int,input().strip().split())
stri = ""
for i in l:
    if i == 1:
        stri += str(-1) + "\t"
        continue
    sum = 1
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            sum+=j
            if j != i // j:
                sum += i // j
    if sum == i:
        stri += str(0) + "\t"
    elif sum > i:
        stri += str(1) + "\t"
    else:
        stri += str(-1) + "\t"
print(stri)