n=int(input("enter a number"))
for i in range(1,n+1):
    count=0
    for a in range(1,i+1):
    
        if i%a==0:
            count=count+1
        else:
            count=count
    if count<=2:
        print(i, "is a prime")
    else:
        print(i, "is a composite")
