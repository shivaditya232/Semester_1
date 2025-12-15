l=[2,5,1,3,4]
for i in range(len(l)):
    min=l[i]
    for j in range(i+1,len(l)):
        if l[j]<min:
            min=l[j]
            l[i],l[j]=l[j],l[i]
            
print(l)