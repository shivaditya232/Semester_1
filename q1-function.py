products=[{"id":101,"name":"laptop","price":900,"stock":12},{"id":150,"name":"keyboard","price":25,"stock":85},{"id":205,"name":"monitor","price":180,"stock":30}]
x=int(input("enter the high range"))
y=int(input("enter the low range"))
L=[]
dict={}
for i in products:
    if y<i["price"]<x:
        L.append(i)
        
print(L)
