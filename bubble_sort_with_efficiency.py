l = [1,2,3,4,5,6,7,8,9]
n = len(l)
flap = True
for i in range(0,n):
    for j in range(0,n-1-i):
        if l[j]>l[j+1]:
            temp =l[j]
            l[j]=l[j+1]
            l[j+1]=temp
            flap =False
    if flap:
        break
print(l)
