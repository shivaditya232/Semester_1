products=[{"id":101,"name":"laptop","price":900,"stock":12},{"id":150,"name":"keyboard","price":25,"stock":85},{"id":205,"name":"monitor","price":180,"stock":30}]
x=input("enter the name you want to search")
for i in products:
    if i["name"]==x:
        print("found")
