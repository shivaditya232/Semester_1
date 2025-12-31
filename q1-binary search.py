x=int(input("Enter the id"))
products=[{"id":101,"name":"laptop","price":900,"stock":12},{"id":150,"name":"keyboard","price":25,"stock":85},{"id":205,"name":"monitor","price":180,"stock":30}]
upper=len(products)-1
lower=0

flag=True
while lower<=upper:
    mid=(upper+lower)//2
    if products[mid]["id"]==x:
        print(mid)
        flag=False
        break
    elif products[mid]["id"]<x:
        lower=mid+1
    elif products[mid]["id"]>x:
        upper=mid-1
if flag==True:
    print("Not Found")





