N=int(input("enter the number"))
L=[]
for i in range(1,N+1):
    if N%i==0:
        L.append(i)
print(L)
count=sum(L)
if N==count:
    print("it is a perfect number")
else:
    print("it is not a perfect number")
