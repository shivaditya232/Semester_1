L=[1,2,3,4]
smax=0
max=0
for i in range(len(L)):
    if L[i]>max:
        smax=max
        max=L[i]
    if smax<L[i]<max:
        smax=L[i]
    else:
        smax=smax
        max=max
print(smax)