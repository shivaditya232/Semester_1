products=[{"id":101,"name":"laptop","price":900,"stock":12},{"id":205,"name":"keyboard","price":25,"stock":85},{"id":150,"name":"monitor","price":180,"stock":30}]
for i in range(len(products)):
    for j in range(0,len(products)-i-1):
        if products[j]["price"]>products[j+1]["price"]:
            products[j],products[j+1]=products[j+1],products[j]
print(products)